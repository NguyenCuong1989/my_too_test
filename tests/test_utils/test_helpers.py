"""
test_helpers.py — Unit tests for src/utils/helpers.py
"""

import json
from pathlib import Path

import pytest

from src.utils.helpers import load_json_file, save_json_file, parse_json_string, truncate


class TestLoadJsonFile:
    def test_loads_valid_json(self, tmp_json_file):
        data = {"key": "value", "number": 42}
        path = tmp_json_file(data)
        result = load_json_file(path)
        assert result == data

    def test_raises_for_missing_file(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            load_json_file(tmp_path / "nonexistent.json")

    def test_raises_for_invalid_json(self, tmp_path):
        bad = tmp_path / "bad.json"
        bad.write_text("{not valid json}", encoding="utf-8")
        with pytest.raises(json.JSONDecodeError):
            load_json_file(bad)

    def test_accepts_string_path(self, tmp_json_file):
        data = [1, 2, 3]
        path = tmp_json_file(data)
        result = load_json_file(str(path))
        assert result == data


class TestSaveJsonFile:
    def test_saves_dict(self, tmp_path):
        data = {"a": 1}
        dest = tmp_path / "out.json"
        save_json_file(data, dest)
        assert dest.exists()
        assert json.loads(dest.read_text()) == data

    def test_creates_parent_directories(self, tmp_path):
        dest = tmp_path / "nested" / "dir" / "out.json"
        save_json_file({"x": 2}, dest)
        assert dest.exists()

    def test_roundtrip(self, tmp_path):
        data = {"hello": "world", "nums": [1, 2, 3]}
        dest = tmp_path / "rt.json"
        save_json_file(data, dest)
        loaded = load_json_file(dest)
        assert loaded == data


class TestParseJsonString:
    def test_parses_plain_json(self):
        raw = '{"a": 1}'
        assert parse_json_string(raw) == {"a": 1}

    def test_strips_markdown_fences(self):
        raw = "```json\n{\"a\": 1}\n```"
        assert parse_json_string(raw) == {"a": 1}

    def test_raises_for_invalid_json(self):
        with pytest.raises(json.JSONDecodeError):
            parse_json_string("not json {")

    def test_parses_list(self):
        raw = "[1, 2, 3]"
        assert parse_json_string(raw) == [1, 2, 3]


class TestTruncate:
    def test_short_string_unchanged(self):
        assert truncate("hello") == "hello"

    def test_truncates_at_max_length(self):
        s = "a" * 3000
        result = truncate(s, max_length=2000)
        assert len(result) == 2000

    def test_custom_max_length(self):
        result = truncate("abcdefgh", max_length=4)
        assert result == "abcd"

    def test_empty_string(self):
        assert truncate("") == ""
