"""
conftest.py — Shared pytest fixtures for the DAIOF test suite.
"""

import json
import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch


# ---------------------------------------------------------------------------
# Gmail / Google API stubs
# ---------------------------------------------------------------------------

@pytest.fixture
def mock_gmail_service():
    """Return a minimal Gmail service stub.

    Uses ``return_value`` chaining to avoid incrementing call counts during
    fixture setup — keeping each test's assertion state clean.
    """
    service = MagicMock()

    msg = {
        "id": "msg1",
        "threadId": "thread1",
        "snippet": "Short snippet",
        "payload": {
            "headers": [
                {"name": "Subject", "value": "Test Subject"},
                {"name": "From", "value": "sender@example.com"},
            ]
        },
    }

    # Wire up return values without calling the methods (preserves call counts)
    users_mock = service.users.return_value
    messages_mock = users_mock.messages.return_value
    messages_mock.list.return_value.execute.return_value = {"messages": [{"id": "msg1"}]}
    messages_mock.get.return_value.execute.return_value = msg
    messages_mock.modify.return_value.execute.return_value = {}
    users_mock.drafts.return_value.create.return_value.execute.return_value = {"id": "draft1"}

    return service


@pytest.fixture
def mock_ai_client():
    """Return a minimal Gemini AI client stub."""
    client = MagicMock()
    analysis = {
        "is_lead": True,
        "sentiment": "positive",
        "suggested_reply": "Thank you for your interest.",
        "reason": "Enquiry about our AI services.",
    }
    response = MagicMock()
    response.text = json.dumps(analysis)
    client.models.generate_content.return_value = response
    return client, analysis


@pytest.fixture
def mock_notion_client():
    """Return a minimal Notion client stub."""
    client = MagicMock()
    client.pages.create.return_value = {"id": "page1"}
    return client


# ---------------------------------------------------------------------------
# Filesystem helpers
# ---------------------------------------------------------------------------

@pytest.fixture
def tmp_json_file(tmp_path):
    """Write a temporary JSON file and return its path."""
    def _write(data, filename="data.json"):
        p = tmp_path / filename
        p.write_text(json.dumps(data), encoding="utf-8")
        return p
    return _write
