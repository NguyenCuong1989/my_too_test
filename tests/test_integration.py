"""
test_integration.py — Integration-level tests for the DAIOF src/ package.

These tests exercise multiple modules together using mocks for external services.
"""

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from src.utils.helpers import load_json_file, save_json_file, parse_json_string
from src.config import settings as cfg
from src.core.coordinator import analyze_and_draft_reply, scan_emails


class TestSettingsIntegration:
    def test_google_scopes_is_list(self):
        assert isinstance(cfg.GOOGLE_SCOPES, list)
        assert len(cfg.GOOGLE_SCOPES) > 0

    def test_base_dir_is_path(self):
        assert isinstance(cfg.BASE_DIR, Path)


class TestHelpersAndCoordinatorIntegration:
    """Ensure helpers work correctly when feeding data into coordinator functions."""

    def test_parse_json_string_feeds_into_analysis(self):
        raw = json.dumps(
            {
                "is_lead": True,
                "sentiment": "positive",
                "suggested_reply": "Thank you!",
                "reason": "Partnership enquiry.",
            }
        )
        parsed = parse_json_string(raw)
        assert parsed["is_lead"] is True

    def test_json_roundtrip_with_analysis_data(self, tmp_path):
        data = {"leads": [{"subject": "Test", "sentiment": "positive"}]}
        dest = tmp_path / "leads.json"
        save_json_file(data, dest)
        loaded = load_json_file(dest)
        assert loaded["leads"][0]["subject"] == "Test"


class TestScanEmailsIntegration:
    def test_full_scan_with_notion_logging(
        self, mock_gmail_service, mock_ai_client, mock_notion_client
    ):
        gmail = mock_gmail_service
        ai_client, _ = mock_ai_client
        notion = mock_notion_client

        scan_emails(gmail, ai_client, notion_client=notion, notion_db_id="db_test")

        # Verify email was marked as read
        gmail.users().messages().modify.assert_called()
        # Verify Notion page was created
        notion.pages.create.assert_called_once()

    def test_full_scan_without_notion(self, mock_gmail_service, mock_ai_client):
        gmail = mock_gmail_service
        ai_client, _ = mock_ai_client

        scan_emails(gmail, ai_client)

        gmail.users().messages().modify.assert_called()
