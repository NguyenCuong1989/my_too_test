"""
test_main.py — Unit tests for src/main.py entry point.
"""

import logging
from unittest.mock import MagicMock, patch

import pytest


class TestMain:
    def _run_main_with_mocks(self, ai_client=None, notion_client=None):
        """Helper that patches all external dependencies and calls main()."""
        mock_gmail = MagicMock()
        mock_calendar = MagicMock()

        with patch("src.main.get_google_services", return_value=(mock_gmail, mock_calendar)), \
             patch("src.main._build_ai_client", return_value=ai_client or MagicMock()), \
             patch("src.main._build_notion_client", return_value=notion_client), \
             patch("src.main.scan_emails") as mock_scan:
            from src.main import main
            main()
            return mock_scan

    def test_main_calls_scan_emails(self):
        mock_scan = self._run_main_with_mocks()
        mock_scan.assert_called_once()

    def test_main_passes_notion_client_when_configured(self):
        notion = MagicMock()
        mock_scan = self._run_main_with_mocks(notion_client=notion)
        _, kwargs = mock_scan.call_args
        assert kwargs.get("notion_client") is notion

    def test_main_passes_none_notion_when_not_configured(self):
        mock_scan = self._run_main_with_mocks(notion_client=None)
        _, kwargs = mock_scan.call_args
        assert kwargs.get("notion_client") is None


class TestBuildAiClient:
    def test_returns_none_when_google_genai_missing(self):
        import builtins
        real_import = builtins.__import__

        def mock_import(name, *args, **kwargs):
            if name.startswith("google"):
                raise ImportError("No module")
            return real_import(name, *args, **kwargs)

        with patch("builtins.__import__", side_effect=mock_import):
            from importlib import reload
            import src.main as main_module
            # Should gracefully return None when google.genai is not importable
            result = main_module._build_ai_client()
        assert result is None

    def test_returns_client_when_api_key_set(self):
        mock_client = MagicMock()
        mock_genai = MagicMock()
        mock_genai.Client.return_value = mock_client

        with patch.dict("sys.modules", {"google": MagicMock(), "google.genai": mock_genai}):
            from importlib import reload
            import src.main as main_module
            reload(main_module)
            result = main_module._build_ai_client()

        assert result is not None


class TestBuildNotionClient:
    def test_returns_none_when_no_token(self):
        with patch("src.main.NOTION_TOKEN", ""):
            from importlib import reload
            import src.main as main_module
            reload(main_module)
            with patch("src.main.NOTION_TOKEN", ""):
                result = main_module._build_notion_client()
            assert result is None

    def test_returns_client_when_token_set(self):
        mock_notion_client_instance = MagicMock()
        mock_notion_module = MagicMock()
        mock_notion_module.Client.return_value = mock_notion_client_instance

        with patch("src.main.NOTION_TOKEN", "valid_token"), \
             patch.dict("sys.modules", {"notion_client": mock_notion_module}):
            from importlib import reload
            import src.main as main_module
            reload(main_module)
            with patch("src.main.NOTION_TOKEN", "valid_token"):
                result = main_module._build_notion_client()

        assert result is mock_notion_client_instance
