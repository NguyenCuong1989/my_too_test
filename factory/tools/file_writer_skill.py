"""
File Writer Skill (Synced)

Metadata:
- Author: AI OS Level 5 Cognitive Scheduler
- Tags: filesystem, io, storage
"""

import json
from pathlib import Path

def run(payload: str) -> str:
    try:
        lines = payload.strip().split("\n", 1)
        if len(lines) < 2:
            return json.dumps({"status": "failed", "error": "Invalid format."})
        file_path = Path(lines[0].strip())
        content = lines[1]
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return json.dumps({"status": "success", "path": str(file_path.absolute()), "bytes_written": len(content)})
    except Exception as e:
        return json.dumps({"status": "failed", "error": str(e)})
