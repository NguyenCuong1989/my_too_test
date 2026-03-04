import imaplib
import email
import asyncio
import logging
import sys
import os
import json
from datetime import datetime
from pathlib import Path

# Add paths for imports
BASE_DIR = Path("/Users/andy/my_too_test")
sys.path.append(str(BASE_DIR / "autonomous_operator"))
sys.path.append("/Users/andy/balancehub")

try:
    from config import LOG_DIR, HEARTBEAT_INTERVAL, APO_EVENT_BUS_EMAIL, APO_EVENT_BUS_PASS, NOTION_TOKEN, NOTION_DB_ID
    from app.core import apo_canon
    from notion_client import Client
except ImportError:
    LOG_DIR = Path("./logs")
    HEARTBEAT_INTERVAL = 300
    APO_EVENT_BUS_EMAIL = None
    APO_EVENT_BUS_PASS = None
    NOTION_TOKEN = None
    NOTION_DB_ID = None
    apo_canon = None
    Client = None

# Cấu hình LOG
LOG_DIR.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [APO_ORCHESTRATOR] [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(LOG_DIR / "apoctl_orchestrator.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

class ApoctlOrchestrator:
    def __init__(self):
        self.logger = logging.getLogger("APO_ORCHESTRATOR")
        self.logger.info("⚔️ AI AUTONOMOUS MAINTENANCE MESH: ORCHESTRATOR ACTIVATED")

        # Gmail Credentials from config
        self.imap_server = "imap.gmail.com"
        self.email_user = APO_EVENT_BUS_EMAIL
        self.email_pass = APO_EVENT_BUS_PASS

        # Notion Client
        self.notion = Client(auth=NOTION_TOKEN) if NOTION_TOKEN else None
        self.notion_db_id = NOTION_DB_ID

        self.is_running = False

    def connect_imap(self):
        """Kết nối tới Gmail Event Bus."""
        if not self.email_user or not self.email_pass:
            self.logger.warning("⚠️ Event Bus credentials missing. Operating in simulated mode.")
            return None
        try:
            mail = imaplib.IMAP4_SSL(self.imap_server)
            mail.login(self.email_user, self.email_pass)
            mail.select('inbox')
            return mail
        except Exception as e:
            self.logger.error(f"❌ IMAP Connection failed: {e}")
            return None

    async def poll_event_bus(self):
        """Đọc mail và phân loại sự kiện theo Σ_APΩ–COS."""
        self.logger.info("📡 Polling Event Bus (Gmail 1)...")
        mail = self.connect_imap()
        if not mail:
            return

        try:
            # Tìm các mail chưa đọc (UNSEEN)
            result, data = mail.search(None, 'UNSEEN')
            if result != 'OK':
                return

            for num in data[0].split():
                result, data = mail.fetch(num, '(RFC822)')
                if result != 'OK':
                    continue

                raw_email = data[0][1]
                msg = email.message_from_bytes(raw_email)
                subject = msg['Subject']
                sender = msg['From']

                # Get snippet
                snippet = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == 'text/plain':
                            snippet = part.get_payload(decode=True).decode()[:500]
                            break
                else:
                    snippet = msg.get_payload(decode=True).decode()[:500]

                self.logger.info(f"📨 New Alert: {subject} from {sender}")

                # Link to Notion
                await self.log_to_notion(subject, sender, snippet)

                # Logic phân loại (Topology Mapping)
                await self.route_event(subject, msg)

                # Mark as seen
                mail.store(num, '+FLAGS', '\\Seen')

        except Exception as e:
            self.logger.error(f"❌ Error polling email: {e}")
        finally:
            if mail:
                mail.logout()

    async def log_to_notion(self, subject, sender, snippet):
        """Ghi nhận sự kiện vào Notion Command Center."""
        if not self.notion or not self.notion_db_id:
            self.logger.warning("⚠️ Notion integration not configured.")
            return

        try:
            self.notion.pages.create(
                parent={"database_id": self.notion_db_id},
                properties={
                    "Name": {"title": [{"text": {"content": f"📬 Mail: {subject}"}}]},
                    "Status": {"select": {"name": "Inbox"}},
                    "Source": {"select": {"name": "Event Bus"}},
                    "Details": {"rich_text": [{"text": {"content": f"From: {sender}\nSnippet: {snippet}"}}]}
                }
            )
            self.logger.info(f"📊 Notion Task Created: {subject}")
        except Exception as e:
            self.logger.error(f"❌ Notion logging failed: {e}")

    async def route_event(self, subject, msg):
        """Định tuyến sự kiện dựa trên G (O -> E -> P -> L -> I -> F -> B)."""
        subject = subject.lower()

        # 𝒪: Origin (Triggers)
        if "github" in subject and "failed" in subject:
             await self.execute_canon_action("F", "GitHub Action Failure Detected")
             await self.execute_canon_action("E", "Triggering Self-Healing Audit")

        elif "vercel" in subject and "deployment" in subject:
             await self.execute_canon_action("P", "New Deployment Detected")

        elif "stripe" in subject:
             await self.execute_canon_action("I", "Payment Activity Detected")

        elif "lead" in subject or "collaboration" in subject or "hợp tác" in subject:
             await self.execute_canon_action("B", f"Potential Business Lead: {subject}")

    async def execute_canon_action(self, op_id, description):
            """Thực thi action theo đúng Protocol."""
            symbol = "UNKNOWN"
            if apo_canon:
                symbol = apo_canon.OPERATORS.get(op_id, {}).get("symbol", op_id)

            self.logger.info(f"⚡ [OP:{op_id}] {symbol} | Action: {description}")

            # Execute via CLI - mapping B (Biz) to biz_node trigger
            try:
                import subprocess
                if op_id == "B":
                     # Trigger BizNode specifically
                     cli_path = BASE_DIR / "autonomous_operator" / "nodes" / "biz_node.py"
                     subprocess.Popen(["python3", str(cli_path)])
                else:
                     cli_path = BASE_DIR / "autonomous_operator" / "apoctl_cli.py"
                     subprocess.run(["python3", str(cli_path), op_id, description], check=True)
            except Exception as e:
                self.logger.error(f"❌ Execution failed: {e}")

    async def main_loop(self):
        self.is_running = True
        while self.is_running:
            start_time = datetime.now()
            await self.poll_event_bus()

            # Chống drift: Run audit every loop (simulated as OP:L)
            await self.execute_canon_action("L", "Periodic Drift Detection Check")

            duration = datetime.now() - start_time
            self.logger.info(f"✅ Pulse complete (Duration: {duration})")
            await asyncio.sleep(HEARTBEAT_INTERVAL)

if __name__ == "__main__":
    orchestrator = ApoctlOrchestrator()
    try:
        asyncio.run(orchestrator.main_loop())
    except KeyboardInterrupt:
        orchestrator.logger.info("Stopping Orchestrator...")
        orchestrator.is_running = False
