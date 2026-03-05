"""
File Deleter Skill (Synced)

Metadata:
- Author: AI OS Level 5
- Tags: filesystem, cleanup
"""

import json
from pathlib import Path

def run(payload: str) -> str:
    path = Path(payload.strip())
    if not path.exists():
        return json.dumps({"status": "failed", "error": "File not found"})
    try:
        path.unlink()
        return json.dumps({"status": "success", "deleted": str(path)})
    except Exception as e:
        return json.dumps({"status": "failed", "error": str(e)})
