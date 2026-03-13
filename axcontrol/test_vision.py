import sys
import os
from pathlib import Path
import json

sys.path.append(str(Path(__file__).resolve().parent))

try:
    from adapters.macos_ax import observer
    snap = observer.observe()
    if snap:
        data = {
            "app": snap.app,
            "role": snap.role,
            "label": snap.label,
            "value": snap.value,
            "window_title": snap.window_title
        }
        print(json.dumps({"status": "SUCCESS", "vision": data}, indent=2))
    else:
        print(json.dumps({"status": "FAILED", "reason": "No AX snapshot returned. Sandbox or Accessibility limits might be active."}, indent=2))
except Exception as e:
    print(json.dumps({"status": "ERROR", "reason": str(e)}, indent=2))
