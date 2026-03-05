"""
coordinator.py — Business Hub Coordinator (refactored from business_hub.py)

Handles email scanning, AI-powered draft replies, and Notion logging.
"""

import os
import base64
import json
from email.message import EmailMessage


def get_google_services(scopes, token_path="token.json", credentials_path="credentials.json"):
    """Authenticate and return Gmail and Calendar service clients."""
    try:
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build

        creds = None
        if os.path.exists(token_path):
            creds = Credentials.from_authorized_user_file(token_path, scopes)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(credentials_path, scopes)
                creds = flow.run_local_server(port=0, open_browser=False)
            with open(token_path, "w") as token:
                token.write(creds.to_json())

        gmail = build("gmail", "v1", credentials=creds)
        calendar = build("calendar", "v3", credentials=creds)
        return gmail, calendar
    except ImportError as exc:
        raise ImportError("Google API libraries are required. Install google-api-python-client.") from exc


def analyze_and_draft_reply(gmail_service, ai_client, msg_id, subject, snippet, body_content=""):
    """Use Gemini AI to analyse an email and create a draft reply when a lead is detected."""
    prompt = f"""
    You are a senior business assistant.

    Incoming email:
    Subject: {subject}
    Summary: {snippet}
    Body: {body_content}

    Return ONLY a JSON object with the structure:
    {{
        "is_lead": boolean,
        "sentiment": "positive/neutral/negative",
        "suggested_reply": "Professional reply content",
        "reason": "Short explanation"
    }}
    """

    try:
        response = ai_client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt,
        )
        analysis = json.loads(
            response.text.strip().replace("```json", "").replace("```", "")
        )
        if analysis.get("is_lead"):
            print(f"[AI] Potential lead detected: {subject}")
            create_draft(gmail_service, msg_id, subject, analysis["suggested_reply"])
        return analysis
    except Exception as exc:
        print(f"[WARNING] AI analysis failed for '{subject}': {exc}")
    return None


def create_draft(service, msg_id, subject, content):
    """Create an email draft reply via the Gmail API."""
    try:
        message = EmailMessage()
        message.set_content(content)
        message["Subject"] = f"Re: {subject}"

        msg_detail = service.users().messages().get(userId="me", id=msg_id).execute()
        headers = msg_detail["payload"]["headers"]
        to_email = next(h["value"] for h in headers if h["name"] == "From")
        message["To"] = to_email

        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        create_message = {
            "message": {"raw": encoded_message, "threadId": msg_detail["threadId"]}
        }
        service.users().drafts().create(userId="me", body=create_message).execute()
        print(f"[INFO] Draft reply created for: {to_email}")
    except Exception as exc:
        print(f"[ERROR] Failed to create draft: {exc}")


def log_to_notion(notion_client, db_id, subject, snippet, analysis):
    """Record a detected lead in a Notion database."""
    try:
        notion_client.pages.create(
            parent={"database_id": db_id},
            properties={
                "Name": {"title": [{"text": {"content": subject}}]},
                "Status": {"select": {"name": "New Lead"}},
                "Sentiment": {"select": {"name": analysis["sentiment"].capitalize()}},
                "Reason": {"rich_text": [{"text": {"content": analysis["reason"]}}]},
                "Snippet": {"rich_text": [{"text": {"content": snippet[:2000]}}]},
            },
        )
        print("[INFO] Lead saved to Notion.")
    except Exception as exc:
        print(f"[WARNING] Could not save to Notion: {exc}")


def scan_emails(gmail_service, ai_client, notion_client=None, notion_db_id=None):
    """Scan unread emails, analyse with AI, and optionally log leads to Notion."""
    print("[INFO] Scanning inbox for potential leads...")
    query = 'is:unread (quote OR partnership OR "AI" OR DAIOF OR "business")'
    try:
        results = gmail_service.users().messages().list(userId="me", q=query).execute()
        messages = results.get("messages", [])

        if not messages:
            print("[INFO] No new messages to process.")
            return

        for message in messages:
            msg = gmail_service.users().messages().get(userId="me", id=message["id"]).execute()
            headers = msg["payload"]["headers"]
            subject = next(
                (h["value"] for h in headers if h["name"] == "Subject"), "No Subject"
            )
            snippet = msg.get("snippet", "")

            print(f"[INFO] Processing: {subject}")
            analysis = analyze_and_draft_reply(
                gmail_service, ai_client, message["id"], subject, snippet
            )

            if analysis:
                print(f"[INFO] Classification: {analysis['reason']}")
                if notion_client and notion_db_id:
                    log_to_notion(notion_client, notion_db_id, subject, snippet, analysis)

            gmail_service.users().messages().modify(
                userId="me",
                id=message["id"],
                body={"removeLabelIds": ["UNREAD"]},
            ).execute()
    except Exception as exc:
        print(f"[ERROR] Email scan failed: {exc}")
