# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

import os
import sys
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent.parent.absolute()
STATE_DIR = BASE_DIR / "autonomous_operator" / "state"
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))
if str(BASE_DIR / "autonomous_operator") not in sys.path:
    sys.path.append(str(BASE_DIR / "autonomous_operator"))

# --- INTEGRATED SERVICE ECOSYSTEM (Master's Domain) ---
INTEGRATED_SERVICES = {
    "Canva": "https://www.canva.com",
    "Conductor": "https://www.conductor.com",
    "DataCamp": "https://www.datacamp.com",
    "DEWA": "https://www.dewa.gov.ae",
    "Figma": "https://www.figma.com",
    "Internshala": "https://internshala.com",
    "Lovable": "https://lovable.dev",
    "Malwarebytes": "https://www.malwarebytes.com",
    "Netlify": "https://www.netlify.com",
    "Network Solutions": "https://www.networksolutions.com",
    "Replit": "https://replit.com",
    "Stripe": "https://stripe.com",
    "Vercel": "https://vercel.com",
    "Airtable": "https://airtable.com",
    "Asana": "https://asana.com",
    "Atlassian Rovo": "https://www.atlassian.com/software/rovo",
    "B12": "https://www.b12.io",
    "Ace Knowledge Graph": "https://google.com", # Fixed broken placeholder
    "Jira": "https://nguyencuong2509.atlassian.net"
}

# --- LOGGING & STATE ---
LOG_DIR = BASE_DIR / "autonomous_operator" / "logs"

# Ensure directories exist
STATE_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Google Scopes
SCOPES = [
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/calendar.events',
    'https://www.googleapis.com/auth/drive.file'
]

# API Keys & Secrets
def get_secret(path):
    p = Path(path)
    if p.exists():
        return p.read_text().strip()
    return None

try:
    from .key_manager import GeminiKeyManager
except ImportError:
    from key_manager import GeminiKeyManager

try:
    from kernel.quota_guard_v1 import QuotaGuard
except ImportError:
    QuotaGuard = None

km = GeminiKeyManager()
quota_guard = QuotaGuard() if QuotaGuard else None


def get_gemini_api_key(task_class="cloud-optional"):
    if quota_guard:
        allow_cloud, _, _ = quota_guard.allow_cloud(task_class)
        if not allow_cloud:
            return None
    return os.environ.get("GEMINI_API_KEY") or km.get_active_key()


GEMINI_API_KEY = get_gemini_api_key()
NOTION_TOKEN = get_secret(BASE_DIR / "notion_secret.txt")
NOTION_DB_ID = get_secret(BASE_DIR / "notion_db_id.txt")

# Jira / Atlassian
JIRA_URL = "https://nguyencuong2509.atlassian.net"
JIRA_EMAIL = get_secret(BASE_DIR / "jira_email.txt")
JIRA_API_TOKEN = get_secret(BASE_DIR / "jira_token.txt")

# GitHub (Optional for Guardian Node)
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

# AI Engine Settings (Master's Rule: Ollama local first)
DEFAULT_AI_ENGINE = "ollama"
AI_MODEL = "qwen3:8b"

# Heartbeat Settings
HEARTBEAT_INTERVAL = 300 # 5 minutes

# Governance Settings
BALANCEHUB_URL = "http://localhost:8000"

# --- APO SOFTWARE FACTORY (0-Dollar System) ---
APO_EVENT_BUS_EMAIL = get_secret(BASE_DIR / ".apo_email_bus.txt")
APO_EVENT_BUS_PASS = get_secret(BASE_DIR / ".apo_email_bus_pass.txt") # App Password
APO_OPS_EMAIL = get_secret(BASE_DIR / ".apo_email_ops.txt")

# --- APΩ-PORTAL (Identity & Governance) ---
WP_CLIENT_ID = get_secret(BASE_DIR / ".wp_client_id.txt")
WP_CLIENT_SECRET = get_secret(BASE_DIR / ".wp_client_secret.txt")
PORTAL_WIKI_DB_ID = get_secret(BASE_DIR / ".portal_wiki_db_id.txt")

# --- APΩ TELEGRAM CONDUIT (Axis 1) ---
TELEGRAM_BOT_TOKEN = "8524726075:AAE2LB7rshE4hMyBrA5WjGFJvErZ2ml92mE"
