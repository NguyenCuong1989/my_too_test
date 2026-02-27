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
        self.logger = logging.getLogger("BizService")
        self.services = [] # List of (gmail_svc, email_addr)
        self.notion = Client(auth=NOTION_TOKEN) if NOTION_TOKEN else None
        self.link = NeuralLink()
        self.logger.info(f"🏢 BizService (Direct Combat) using LOCAL AI: {self.AI_MODEL}")

    def authenticate_all(self):
        """Xác thực tất cả các tài khoản Gmail được cấu hình (token_*.json)"""
        self.services = []
        token_files = list(BASE_DIR.glob('token_*.json'))
        # If no specific tokens, try the default one
        if not token_files and (BASE_DIR / 'token.json').exists():
            token_files = [BASE_DIR / 'token.json']

        creds_path = BASE_DIR / 'credentials.json'
        if not creds_path.exists():
            self.logger.error("credentials.json not found! Cannot combat.")
            return False

        for t_file in token_files:
            try:
                creds = Credentials.from_authorized_user_file(str(t_file), SCOPES)
                if not creds or not creds.valid:
                    if creds and creds.expired and creds.refresh_token:
                        creds.refresh(Request())
                    else:
                        continue # Skip if requires interaction for now

                svc = build('gmail', 'v1', credentials=creds)
                profile = svc.users().getProfile(userId='me').execute()
                email = profile.get('emailAddress')
                self.services.append((svc, email))
                self.logger.info(f"✅ Authenticated: {email}")
            except Exception as e:
                self.logger.error(f"Failed to auth {t_file.name}: {e}")

        return len(self.services) > 0

    def run_cycle(self):
        self.logger.info("⚔️ Starting Direct Combat Scan...")
        if not self.services:
            if not self.authenticate_all():
                self.logger.error("No Gmail services authenticated. Check tokens.")
                return

        for svc, email in self.services:
            self.logger.info(f"📧 Scanning {email}...")
            self.scan_account(svc, email)

    def scan_account(self, svc, email):
        # Scan for unread business-intent emails
        query = 'is:unread (báo giá OR hợp tác OR "AI" OR "business")'
        try:
            results = svc.users().messages().list(userId='me', q=query, maxResults=10).execute()
            messages = results.get('messages', [])

            if not messages:
                self.logger.info(f"🍃 {email}: No new leads found.")
                return

            for message in messages:
                self.process_message(svc, email, message['id'])
        except Exception as e:
            self.logger.error(f"Gmail scan error on {email}: {e}")

    def process_message(self, svc, email, msg_id):
        try:
            msg = svc.users().messages().get(userId='me', id=msg_id).execute()
            headers = msg['payload']['headers']
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "No Subject")
            snippet = msg.get('snippet', '')

            self.logger.info(f"🔍 Analyzing: {subject} (for {email})")
            analysis = self.analyze_ai(subject, snippet)

            if analysis and analysis.get("is_lead"):
                self.logger.info(f"🎯 LEAD DETECTED: {subject}")
                self.create_draft(svc, msg_id, subject, analysis["suggested_reply"])

                # 🏢 SAAS EVENT LOGGING
                session_id = f"combat_{email.split('@')[0]}_{msg_id}"
                self.link.log_service_event(
                    service="BizService",
                    e_type="CAPABILITY_EXEC",
                    content=f"Lead detected on {email}: '{subject}'. Draft created.",
                    meta=json.dumps({"email": email, "msg_id": msg_id, "sentiment": analysis.get("sentiment")})
                )

                if NOTION_DB_ID:
                    self.log_to_notion(subject, snippet, analysis, email)

            # Mark as read
            svc.users().messages().modify(
                userId='me', id=msg_id, body={'removeLabelIds': ['UNREAD']}
            ).execute()
        except Exception as e:
            self.logger.error(f"Error processing message {msg_id} on {email}: {e}")

    def analyze_ai(self, subject, snippet):
        """Sử dụng AI để quyết định xem đây có phải là cơ hội kinh doanh không."""
        prompt = f"""Phân tích email:
Tiêu đề: {subject}
Nội dung: {snippet}

Trả về JSON:
{{"is_lead": bool, "sentiment": "positive|neutral|negative", "suggested_reply": "Chào Master, đây là... [soạn hướng phản hồi chuyên nghiệp]", "reason": "Tại sao AI nghĩ đây là lead"}}"""
        try:
            response = ollama.chat(
                model=self.AI_MODEL,
                messages=[{"role": "user", "content": prompt}]
            )
            raw = response['message']['content'].strip()
            if '<think>' in raw: raw = raw.split('</think>')[-1].strip()
            raw = raw.replace('```json', '').replace('```', '').strip()
            return json.loads(raw)
        except Exception as e:
            self.logger.error(f"AI Analysis error: {e}")
            return None

    def create_draft(self, svc, msg_id, subject, content):
        try:
            message = EmailMessage()
            message.set_content(content)
            message['Subject'] = f"Re: {subject}"

            msg_detail = svc.users().messages().get(userId='me', id=msg_id).execute()
            headers = msg_detail['payload']['headers']
            from_header = next((h['value'] for h in headers if h['name'] == 'From'), "")
            message['To'] = from_header

            encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
            body = {'message': {'raw': encoded_message, 'threadId': msg_detail['threadId']}}
            svc.users().drafts().create(userId='me', body=body).execute()
            self.logger.info(f"📝 Draft created for: {from_header}")
        except Exception as e:
            self.logger.error(f"Draft error: {e}")

    def log_to_notion(self, subject, snippet, analysis, email):
        """Sử dụng Notion làm Command Center duy nhất."""
        try:
            if self.notion:
                self.notion.pages.create(
                    parent={"database_id": NOTION_DB_ID},
                    properties={
                        "Name": {"title": [{"text": {"content": f"📧 Lead: {subject}"}}]},
                        "Status": {"select": {"name": "New Lead"}},
                        "Account": {"select": {"name": email}},
                        "Sentiment": {"select": {"name": analysis["sentiment"].capitalize()}},
                        "Reason": {"rich_text": [{"text": {"content": analysis["reason"]}}]},
                        "Snippet": {"rich_text": [{"text": {"content": f"From: {email}\n\n{snippet[:1000]}"}}]}
                    }
                )
                self.logger.info(f"📊 Notion Synced: {subject}")
        except Exception as e:
            self.logger.error(f"Notion logging error: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    node = BizNode()
    if node.authenticate_all():
        node.run_cycle()
