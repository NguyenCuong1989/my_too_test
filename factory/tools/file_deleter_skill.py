# Σ_APΩ₂ CORE MODULE
# Authority: BỐ CƯỐNG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

"""
File Deleter Skill (Synced)

Metadata:
- Author: AI OS Level 5
- Tags: filesystem, cleanup
"""

import json
from pathlib import Path

def run(payload: str = None) -> str:
    if not payload:
        return json.dumps({"status": "failed", "error": "No payload provided"})

    try:
        try:
            data = json.loads(payload)
            path_str = data.get("file_path") or data.get("path") or payload.strip()
        except json.JSONDecodeError:
            path_str = payload.strip()

        if not path_str:
            return json.dumps({"status": "failed", "error": "No file path provided"})

        path = Path(path_str)
        if not path.exists():
            return json.dumps({"status": "failed", "error": f"File not found: {path_str}"})

        if not path.is_file():
            return json.dumps({"status": "failed", "error": f"Path is not a file: {path_str}. Use directory_deleter for directories."})

        path.unlink()
        return json.dumps({"status": "success", "deleted": str(path)})
    except Exception as e:
        return json.dumps({"status": "failed", "error": str(e)})

if __name__ == "__main__":
    print(run())
