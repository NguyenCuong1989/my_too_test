"""
helpers.py — General-purpose utility functions.
"""

import json
import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


def load_json_file(path: str | Path) -> Any:
    """Load and parse a JSON file.

    Args:
        path: Path to the JSON file.

    Returns:
        Parsed Python object.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"JSON file not found: {path}")
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def save_json_file(data: Any, path: str | Path, indent: int = 2) -> None:
    """Serialize *data* as JSON and write it to *path*.

    Args:
        data: Python object to serialize.
        path: Destination file path.
        indent: JSON indentation level (default 2).
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=indent, ensure_ascii=False)
    logger.debug("Saved JSON to %s", path)


def parse_json_string(raw: str) -> Any:
    """Parse a JSON string, stripping optional markdown code fences.

    Args:
        raw: Raw string, possibly wrapped in ```json … ```.

    Returns:
        Parsed Python object.

    Raises:
        json.JSONDecodeError: If the cleaned string is not valid JSON.
    """
    cleaned = raw.strip().replace("```json", "").replace("```", "").strip()
    return json.loads(cleaned)


def truncate(text: str, max_length: int = 2000) -> str:
    """Truncate *text* to at most *max_length* characters.

    Args:
        text: Input string.
        max_length: Maximum allowed length (default 2000).

    Returns:
        Truncated string.
    """
    return text[:max_length]
