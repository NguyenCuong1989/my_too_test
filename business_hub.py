import os.path
import base64
import json
from email.message import EmailMessage

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import googleapiclient.errors
from google import genai
from notion_client import Client

# 1. CẤU HÌNH API
SCOPES = [
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/calendar.events',
    'https://www.googleapis.com/auth/drive.file'
]

# AI SDK setup (New Free Tier Project)
GEMINI_API_KEY = "AIzaSyA4phW8utb9qRXjbbO0vGv4o2GZsZ7stGo"
client_ai = genai.Client(api_key=GEMINI_API_KEY)

# Notion Config
NOTION_TOKEN = open("/Users/andy/my_too_test/notion_secret.txt").read().strip()
NOTION_DB_ID = None
if os.path.exists("/Users/andy/my_too_test/notion_db_id.txt"):
    NOTION_DB_ID = open("/Users/andy/my_too_test/notion_db_id.txt").read().strip()

notion = Client(auth=NOTION_TOKEN)

def get_google_services():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0, open_browser=False)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    gmail = build('gmail', 'v1', credentials=creds)
    calendar = build('calendar', 'v3', credentials=creds)
    return gmail, calendar

def analyze_and_draft_reply(gmail_service, msg_id, subject, snippet, body_content=""):
    """Dùng Gemini AI để phân tích email và tạo bản nháp trả lời"""
    prompt = f"""
    Bạn là một trợ lý kinh doanh cao cấp cho Master alpha_prime_omega (Nguyễn Đức Cường).
    Dự án trọng tâm: DAIOF-Framework (Hệ sinh thái công nghiệp AI), HyperAI Phoenix, Kinh doanh giải pháp AI Agents.

    Nội dung Email nhận được:
    Tiêu đề: {subject}
    Nội dung tóm tắt: {snippet}
    Nội dung chi tiết: {body_content}

    Hãy trả về JSON duy nhất với cấu trúc:
    {{
        "is_lead": boolean,
        "sentiment": "positive/neutral/negative",
        "suggested_reply": "Nội dung phản hồi tinh tế, chuyên nghiệp",
        "reason": "Giải thích ngắn gọn"
    }}
    """

    try:
        response = client_ai.models.generate_content(
            model='models/gemini-2.5-flash',
            contents=prompt
        )

        # Parse JSON
        analysis = json.loads(response.text.strip().replace('```json', '').replace('```', ''))

        if analysis.get("is_lead"):
            print(f"✨ [AI] Phát hiện khách hàng tiềm năng: {subject}")
            create_draft(gmail_service, msg_id, subject, analysis["suggested_reply"])
            return analysis
    except Exception as e:
        print(f"⚠️ Lỗi phân tích AI cho '{subject}': {e}")
    return None

def create_draft(service, msg_id, subject, content):
    """Tạo bản nháp email trả lời"""
    try:
        message = EmailMessage()
        message.set_content(content)
        message['Subject'] = f"Re: {subject}"

        msg_detail = service.users().messages().get(userId='me', id=msg_id).execute()
        headers = msg_detail['payload']['headers']
        to_email = next(h['value'] for h in headers if h['name'] == 'From')
        message['To'] = to_email

        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        create_message = {'message': {'raw': encoded_message, 'threadId': msg_detail['threadId']}}

        service.users().drafts().create(userId='me', body=create_message).execute()
        print(f"📝 Đã tạo bản nháp trả lời cho: {to_email}")
    except Exception as e:
        print(f"❌ Lỗi tạo bản nháp: {e}")

def log_to_notion(subject, snippet, analysis):
    """Ghi nhận lead vào Notion database"""
    try:
        notion.pages.create(
            parent={"database_id": NOTION_DB_ID},
            properties={
                "Name": {"title": [{"text": {"content": subject}}]},
                "Status": {"select": {"name": "New Lead"}},
                "Sentiment": {"select": {"name": analysis["sentiment"].capitalize()}},
                "Reason": {"rich_text": [{"text": {"content": analysis["reason"]}}]},
                "Snippet": {"rich_text": [{"text": {"content": snippet[:2000]}}]}
            }
        )
        print("📁 Đã lưu thông tin Lead vào Notion.")
    except Exception as e:
        print(f"⚠️ Không thể lưu vào Notion: {e}")

def scan_emails(gmail_service):
    print("🤖 DAIOF AI AGENT đang rà soát hòm thư...")
    query = 'is:unread (báo giá OR hợp tác OR "AI" OR DAIOF OR "business")'
    try:
        results = gmail_service.users().messages().list(userId='me', q=query).execute()
        messages = results.get('messages', [])

        if not messages:
            print("📭 Không có thư mới cần xử lý.")
            return

        for message in messages:
            msg = gmail_service.users().messages().get(userId='me', id=message['id']).execute()
            headers = msg['payload']['headers']
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "No Subject")
            snippet = msg.get('snippet', '')

            print(f"📩 Đang xử lý: {subject}")
            analysis = analyze_and_draft_reply(gmail_service, message['id'], subject, snippet)

            if analysis:
                print(f"🚀 Phân loại: {analysis['reason']}")
                if NOTION_DB_ID:
                    log_to_notion(subject, snippet, analysis)

            # Đánh dấu đã đọc để tránh xử lý lại
            gmail_service.users().messages().modify(
                userId='me', id=message['id'], body={'removeLabelIds': ['UNREAD']}
            ).execute()
    except Exception as e:
        print(f"❌ Lỗi quét email: {e}")

if __name__ == '__main__':
    print("🔥 DAIOF BUSINESS HUB v2.5 (MODERN AI) ACTIVATED")
    try:
        gmail_svc, cal_svc = get_google_services()
        scan_emails(gmail_svc)
        print("✅ Đã hoàn thành đợt rà soát.")
    except Exception as e:
        print(f"❌ Lỗi khởi động: {e}")
