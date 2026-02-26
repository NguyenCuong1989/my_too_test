import os
import base64
import json
import logging
from email.message import EmailMessage
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import ollama
from notion_client import Client

import sys
from pathlib import Path
try:
    from .config import SCOPES, GEMINI_API_KEY, NOTION_TOKEN, NOTION_DB_ID, BASE_DIR
    from .neural_link import NeuralLink
except (ImportError, ValueError):
    sys.path.append(str(Path(__file__).parent.parent))
    from config import SCOPES, GEMINI_API_KEY, NOTION_TOKEN, NOTION_DB_ID, BASE_DIR
    from neural_link import NeuralLink

class BizNode:
    # Local AI engine — unlimited, no API quota
    AI_MODEL = "qwen3:8b"

    def __init__(self):
        self.logger = logging.getLogger("BizNode")
        self.gmail_svc = None
        self.notion = Client(auth=NOTION_TOKEN) if NOTION_TOKEN else None
        self.link = NeuralLink()
        self.logger.info(f"🤖 BizNode using LOCAL AI: {self.AI_MODEL}")

    def authenticate(self):
        creds = None
        token_path = BASE_DIR / 'token.json'
        creds_path = BASE_DIR / 'credentials.json'

        if token_path.exists():
            creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not creds_path.exists():
                    self.logger.error("credentials.json not found!")
                    return False
                flow = InstalledAppFlow.from_client_secrets_file(str(creds_path), SCOPES)
                creds = flow.run_local_server(port=0, open_browser=False)
            with open(token_path, 'w') as token:
                token.write(creds.to_json())

        self.gmail_svc = build('gmail', 'v1', credentials=creds)
        return True

    def run_cycle(self):
        self.logger.info("Scanning for business emails...")
        if not self.gmail_svc:
            if not self.authenticate():
                self.logger.error("Authentication failed, skipping cycle.")
                return

        # Limit to 5 unread emails from the last 7 days to conserve quota
        query = 'is:unread (báo giá OR hợp tác OR "AI" OR DAIOF OR "business")'
        try:
            svc = self.gmail_svc
            if svc is None: return
            results = svc.users().messages().list(userId='me', q=query, maxResults=5).execute()
            messages = results.get('messages', [])

            if not messages:
                self.logger.info("No unread business emails pulse.")
                return

            for message in messages:
                self.process_message(message['id'])
        except Exception as e:
            self.logger.error(f"Gmail scan error: {e}")

    def process_message(self, msg_id):
        svc = self.gmail_svc
        if svc is None: return
        try:
            msg = svc.users().messages().get(userId='me', id=msg_id).execute()
            headers = msg['payload']['headers']
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "No Subject")
            snippet = msg.get('snippet', '')

            self.logger.info(f"Processing: {subject}")
            analysis = self.analyze_ai(subject, snippet)

            if analysis and analysis.get("is_lead"):
                self.logger.info(f"✨ Lead detected: {subject}")
                self.create_draft(msg_id, subject, analysis["suggested_reply"])
                if NOTION_DB_ID:
                    self.log_to_notion(subject, snippet, analysis)

            # Mark as read
            if self.gmail_svc:
                self.gmail_svc.users().messages().modify(
                    userId='me', id=msg_id, body={'removeLabelIds': ['UNREAD']}
                ).execute()
        except Exception as e:
            self.logger.error(f"Error processing message {msg_id}: {e}")

    def analyze_ai(self, subject, snippet):
        """Phân tích email bằng Ollama Local AI (qwen3:8b) — không cần quota"""
        prompt = f"""Bạn là trợ lý AI cao cấp của Master alpha_prime_omega.

Phân tích email sau và trả về JSON:
- Tiêu đề: {subject}
- Nội dung: {snippet}

Trả về ONLY valid JSON (không có text nào khác):
{{"is_lead": bool, "sentiment": "positive|neutral|negative", "suggested_reply": "...", "reason": "..."}}"""
        try:
            response = ollama.chat(
                model=self.AI_MODEL,
                messages=[{"role": "user", "content": prompt}],
                options={"temperature": 0.2}
            )
            raw = response['message']['content'].strip()
            # Strip thinking tags if model outputs them
            if '<think>' in raw:
                raw = raw.split('</think>')[-1].strip()
            raw = raw.replace('```json', '').replace('```', '').strip()
            return json.loads(raw)
        except Exception as e:
            self.logger.error(f"Ollama AI Analysis error: {e}")
            return None

    def create_draft(self, msg_id, subject, content):
        try:
            message = EmailMessage()
            message.set_content(content)
            message['Subject'] = f"Re: {subject}"

            if self.gmail_svc is None: return
            msg_detail = self.gmail_svc.users().messages().get(userId='me', id=msg_id).execute()
            headers = msg_detail['payload']['headers']
            to_email = next(h['value'] for h in headers if h['name'] == 'From')
            message['To'] = to_email

            encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
            body = {'message': {'raw': encoded_message, 'threadId': msg_detail['threadId']}}
            self.gmail_svc.users().drafts().create(userId='me', body=body).execute()
        except Exception as e:
            self.logger.error(f"Draft error: {e}")

    def log_to_notion(self, subject, snippet, analysis):
        """Ghi nhận lead vào Notion và hệ thống thần kinh liên kết"""
        try:
            # 1. Notion log
            if self.notion:
                self.notion.pages.create(
                    parent={"database_id": NOTION_DB_ID},
                    properties={
                        "Name": {"title": [{"text": {"content": subject}}]},
                        "Status": {"select": {"name": "New Lead"}},
                        "Sentiment": {"select": {"name": analysis["sentiment"].capitalize()}},
                        "Reason": {"rich_text": [{"text": {"content": analysis["reason"]}}]},
                        "Snippet": {"rich_text": [{"text": {"content": snippet[:2000]}}]}
                    }
                )

            # 2. Viral Link (Neural Pulse)
            self.link.send_pulse(
                node_name="BizNode",
                pulse_type="LEAD_DETECTED",
                content=f"Detected high-value lead: {subject}",
                intensity=0.9
            )

            # 3. Autonomous Task Creation
            self.link.add_autonomous_task(
                title=f"Follow up: {subject}",
                description=f"AI detected lead with sentiment {analysis['sentiment']}. Reason: {analysis['reason']}",
                action=f"Reply to {subject} via Gmail draft",
                priority=1 # HIGH
            )

            self.logger.info(f"📁 Lead '{subject}' Linked to Ecosystem.")
        except Exception as e:
            self.logger.error(f"Ecosystem logging error: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    node = BizNode()
    if node.authenticate():
        node.run_cycle()
