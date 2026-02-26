import os
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent.parent.absolute()
STATE_DIR = BASE_DIR / "autonomous_operator" / "state"

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
    "Ace Knowledge Graph": "https://ace-kg.com" # Placeholder
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

GEMINI_API_KEY = "AIzaSyA4phW8utb9qRXjbbO0vGv4o2GZsZ7stGo" # Primary
NOTION_TOKEN = get_secret(BASE_DIR / "notion_secret.txt")
NOTION_DB_ID = get_secret(BASE_DIR / "notion_db_id.txt")

# GitHub (Optional for Guardian Node)
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

# Heartbeat Settings
HEARTBEAT_INTERVAL = 300 # 5 minutes
