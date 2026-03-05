"""
settings.py — Application configuration.

Values are read from environment variables when available, with sensible
defaults for local development.
"""

import os
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE_DIR: Path = Path(os.getenv("DAIOF_BASE_DIR", str(Path(__file__).resolve().parents[2])))

# ---------------------------------------------------------------------------
# Google API
# ---------------------------------------------------------------------------
GOOGLE_SCOPES: list[str] = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/calendar.events",
    "https://www.googleapis.com/auth/drive.file",
]
GOOGLE_TOKEN_PATH: str = os.getenv("GOOGLE_TOKEN_PATH", "token.json")
GOOGLE_CREDENTIALS_PATH: str = os.getenv("GOOGLE_CREDENTIALS_PATH", "credentials.json")

# ---------------------------------------------------------------------------
# AI
# ---------------------------------------------------------------------------
GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "models/gemini-2.5-flash")

# ---------------------------------------------------------------------------
# Notion
# ---------------------------------------------------------------------------
NOTION_TOKEN: str = os.getenv("NOTION_TOKEN", "")
NOTION_DB_ID: str | None = os.getenv("NOTION_DB_ID", None)

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# ---------------------------------------------------------------------------
# DAIOF installation directory (used by diagnostic and synergy modules)
# ---------------------------------------------------------------------------
DAIOF_INSTALL_DIR: Path = Path(os.getenv("DAIOF_INSTALL_DIR", "/Users/andy/my_too_test"))
