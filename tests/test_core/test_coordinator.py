"""
test_coordinator.py — Unit tests for src/core/coordinator.py
"""

import json
import base64
from email.message import EmailMessage
from unittest.mock import MagicMock, patch, call

import pytest

from src.core.coordinator import (
    analyze_and_draft_reply,
    create_draft,
    get_google_services,
    log_to_notion,
    scan_emails,
)


# ---------------------------------------------------------------------------
# analyze_and_draft_reply
# ---------------------------------------------------------------------------

class TestAnalyzeAndDraftReply:
    def test_lead_detected_creates_draft(self, mock_gmail_service, mock_ai_client):
        gmail = mock_gmail_service
        ai_client, expected_analysis = mock_ai_client

        result = analyze_and_draft_reply(
            gmail, ai_client, "msg1", "Partnership Offer", "We'd like to work together."
        )

        assert result is not None
        assert result["is_lead"] is True
        assert result["sentiment"] == "positive"
        # draft should have been created
        gmail.users().drafts().create.assert_called()

    def test_non_lead_returns_analysis_without_draft(self, mock_gmail_service, mock_ai_client):
        gmail = mock_gmail_service
        ai_client, _ = mock_ai_client

        non_lead = {
            "is_lead": False,
            "sentiment": "neutral",
            "suggested_reply": "",
            "reason": "Not relevant.",
        }
        ai_client.models.generate_content.return_value.text = json.dumps(non_lead)

        result = analyze_and_draft_reply(
            gmail, ai_client, "msg1", "Newsletter", "Monthly digest."
        )

        assert result is not None
        assert result["is_lead"] is False
        # No draft should have been created (the drafts.create method is unwrapped via return_value)
        gmail.users.return_value.drafts.return_value.create.assert_not_called()

    def test_ai_error_returns_none(self, mock_gmail_service, mock_ai_client):
        gmail = mock_gmail_service
        ai_client, _ = mock_ai_client
        ai_client.models.generate_content.side_effect = RuntimeError("API error")

        result = analyze_and_draft_reply(
            gmail, ai_client, "msg1", "Error Test", "Body."
        )

        assert result is None

    def test_invalid_json_returns_none(self, mock_gmail_service, mock_ai_client):
        gmail = mock_gmail_service
        ai_client, _ = mock_ai_client
        ai_client.models.generate_content.return_value.text = "not json {"

        result = analyze_and_draft_reply(
            gmail, ai_client, "msg1", "Bad JSON", "Body."
        )

        assert result is None


# ---------------------------------------------------------------------------
# create_draft
# ---------------------------------------------------------------------------

class TestCreateDraft:
    def test_creates_draft_successfully(self, mock_gmail_service):
        gmail = mock_gmail_service
        create_draft(gmail, "msg1", "Test Subject", "Hello!")
        gmail.users.return_value.drafts.return_value.create.assert_called_once()

    def test_handles_service_error_gracefully(self, mock_gmail_service):
        gmail = mock_gmail_service
        gmail.users.return_value.messages.return_value.get.side_effect = Exception("Service unavailable")
        # Should not raise
        create_draft(gmail, "msg1", "Test Subject", "Hello!")


# ---------------------------------------------------------------------------
# log_to_notion
# ---------------------------------------------------------------------------

class TestLogToNotion:
    def test_creates_notion_page(self, mock_notion_client):
        analysis = {
            "sentiment": "positive",
            "reason": "Potential customer",
        }
        log_to_notion(mock_notion_client, "db123", "Subject", "Snippet", analysis)
        mock_notion_client.pages.create.assert_called_once()

    def test_handles_notion_error_gracefully(self, mock_notion_client):
        mock_notion_client.pages.create.side_effect = Exception("Notion down")
        analysis = {"sentiment": "positive", "reason": "Test"}
        # Should not raise
        log_to_notion(mock_notion_client, "db123", "Subject", "Snippet", analysis)


# ---------------------------------------------------------------------------
# scan_emails
# ---------------------------------------------------------------------------

class TestScanEmails:
    def test_processes_unread_messages(self, mock_gmail_service, mock_ai_client):
        gmail = mock_gmail_service
        ai_client, _ = mock_ai_client

        scan_emails(gmail, ai_client)

        gmail.users().messages().list.assert_called()
        gmail.users().messages().modify.assert_called()

    def test_no_messages_skips_processing(self, mock_gmail_service, mock_ai_client):
        gmail = mock_gmail_service
        ai_client, _ = mock_ai_client
        gmail.users.return_value.messages.return_value.list.return_value.execute.return_value = {
            "messages": []
        }

        scan_emails(gmail, ai_client)

        gmail.users.return_value.messages.return_value.get.assert_not_called()

    def test_logs_to_notion_when_configured(
        self, mock_gmail_service, mock_ai_client, mock_notion_client
    ):
        gmail = mock_gmail_service
        ai_client, _ = mock_ai_client

        scan_emails(gmail, ai_client, notion_client=mock_notion_client, notion_db_id="db1")

        mock_notion_client.pages.create.assert_called_once()

    def test_scan_error_does_not_propagate(self, mock_gmail_service, mock_ai_client):
        gmail = mock_gmail_service
        ai_client, _ = mock_ai_client
        gmail.users.return_value.messages.return_value.list.side_effect = Exception("Network error")

        # Should not raise
        scan_emails(gmail, ai_client)


# ---------------------------------------------------------------------------
# get_google_services
# ---------------------------------------------------------------------------

class TestGetGoogleServices:
    def test_raises_import_error_when_google_libs_missing(self):
        import builtins
        real_import = builtins.__import__

        def mock_import(name, *args, **kwargs):
            if name.startswith("google"):
                raise ImportError("No module named 'google'")
            return real_import(name, *args, **kwargs)

        with patch("builtins.__import__", side_effect=mock_import):
            with pytest.raises(ImportError, match="Google API libraries"):
                get_google_services(["scope1"])

    def test_builds_services_with_valid_token(self, tmp_path):
        token_file = tmp_path / "token.json"
        token_file.write_text('{"token": "x"}', encoding="utf-8")

        mock_creds = MagicMock()
        mock_creds.valid = True

        mock_gmail = MagicMock()
        mock_calendar = MagicMock()

        with patch("src.core.coordinator.os.path.exists", return_value=True), \
             patch("src.core.coordinator.get_google_services") as mock_fn:
            mock_fn.return_value = (mock_gmail, mock_calendar)
            gmail, calendar = mock_fn(["scope"], token_path=str(token_file))

        assert gmail is mock_gmail
        assert calendar is mock_calendar
