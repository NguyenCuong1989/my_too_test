"""
main.py — DAIOF application entry point.
"""

import logging
import os

from src.config.settings import GEMINI_API_KEY, GEMINI_MODEL, GOOGLE_SCOPES, LOG_FORMAT, LOG_LEVEL
from src.config.settings import GOOGLE_TOKEN_PATH, GOOGLE_CREDENTIALS_PATH
from src.config.settings import NOTION_TOKEN, NOTION_DB_ID
from src.core.coordinator import get_google_services, scan_emails


def _build_ai_client():
    """Initialise and return a Gemini AI client."""
    try:
        from google import genai  # type: ignore

        return genai.Client(api_key=GEMINI_API_KEY)
    except ImportError:
        logging.warning("google-genai not installed; AI features disabled.")
        return None


def _build_notion_client():
    """Initialise and return a Notion client (or None if not configured)."""
    if not NOTION_TOKEN:
        return None
    try:
        from notion_client import Client  # type: ignore

        return Client(auth=NOTION_TOKEN)
    except ImportError:
        logging.warning("notion-client not installed; Notion logging disabled.")
        return None


def main() -> None:
    """Run the DAIOF Business Hub."""
    logging.basicConfig(level=getattr(logging, LOG_LEVEL, logging.INFO), format=LOG_FORMAT)

    logging.info("DAIOF BUSINESS HUB — starting")

    gmail_svc, _ = get_google_services(
        GOOGLE_SCOPES,
        token_path=GOOGLE_TOKEN_PATH,
        credentials_path=GOOGLE_CREDENTIALS_PATH,
    )
    ai_client = _build_ai_client()
    notion_client = _build_notion_client()

    scan_emails(gmail_svc, ai_client, notion_client=notion_client, notion_db_id=NOTION_DB_ID)
    logging.info("DAIOF BUSINESS HUB — scan complete")


if __name__ == "__main__":
    main()
