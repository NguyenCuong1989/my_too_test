import sys
import logging
import subprocess
from pathlib import Path

# Add paths for config
BASE_DIR = Path("/Users/andy/my_too_test")
sys.path.append(str(BASE_DIR / "autonomous_operator"))

try:
    from config import NOTION_TOKEN, NOTION_DB_ID
    from notion_client import Client
except ImportError:
    NOTION_TOKEN = None
    NOTION_DB_ID = None
    Client = None

def log_to_notion(event_type, category, message, priority="Medium"):
    """Gửi log vận hành lên Notion Dashboard."""
    if not NOTION_TOKEN or not NOTION_DB_ID or not Client:
        logging.warning("⚠️ Notion credentials missing for factory_utils.")
        return False

    try:
        notion = Client(auth=NOTION_TOKEN)
        notion.pages.create(
            parent={"database_id": NOTION_DB_ID},
            properties={
                "Name": {"title": [{"text": {"content": f"⚙️ {event_type}: Factory"}}]},
                "Status": {"select": {"name": "Operation Log"}},
                "Category": {"select": {"name": category}},
                "Sentiment": {"select": {"name": "Neutral"}},
                "Priority": {"select": {"name": priority}},
                "Reason": {"rich_text": [{"text": {"content": event_type}}]},
                "Snippet": {"rich_text": [{"text": {"content": message[:1500]}}]}
            }
        )
        return True
    except Exception as e:
        logging.error(f"❌ Failed to log to Notion: {e}")
        return False

def call_ollama(prompt, model="qwen3:8b"):
    """Gọi Ollama local để xử lý trí tuệ AI."""
    try:
        result = subprocess.run(
            ["ollama", "run", model, prompt],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except Exception as e:
        logging.error(f"❌ Ollama call failed: {e}")
        return f"AI_ERROR: {e}"

def self_heal_audit(log_content):
    """Phân tích log và đề xuất hướng sửa."""
    prompt = f"Analyze this error log and suggest a concise fix in Python:\n\n{log_content}"
    return call_ollama(prompt)
