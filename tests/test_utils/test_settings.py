"""
test_settings.py — Unit tests for src/config/settings.py
"""

import os
from pathlib import Path
from unittest.mock import patch

import pytest

import src.config.settings as settings


class TestSettings:
    def test_google_scopes_non_empty_list(self):
        assert isinstance(settings.GOOGLE_SCOPES, list)
        assert len(settings.GOOGLE_SCOPES) > 0

    def test_base_dir_is_path_instance(self):
        assert isinstance(settings.BASE_DIR, Path)

    def test_gemini_model_default(self):
        assert "gemini" in settings.GEMINI_MODEL.lower()

    def test_log_level_is_string(self):
        assert isinstance(settings.LOG_LEVEL, str)

    def test_env_override_for_gemini_key(self):
        with patch.dict(os.environ, {"GEMINI_API_KEY": "test_key_123"}):
            import importlib
            import src.config.settings as s
            importlib.reload(s)
            assert s.GEMINI_API_KEY == "test_key_123"

    def test_env_override_for_log_level(self):
        with patch.dict(os.environ, {"LOG_LEVEL": "DEBUG"}):
            import importlib
            import src.config.settings as s
            importlib.reload(s)
            assert s.LOG_LEVEL == "DEBUG"
