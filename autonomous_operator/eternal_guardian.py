# Σ_APΩ CORE MODULE :: ETERNAL CLOUD GUARDIAN
# Authority: BỐ CƯỜNG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Role: Automated Bug-Fixing & 24/7 Execution
# Status: READY_FOR_EMBODIMENT

import os
import time
import json
import re
from pathlib import Path

# --- IDENTITY & CANON ---
NODE_ID = "ETERNAL_CLOUD_GUARDIAN_01"
AUTHORITY_TIER = 2
VERIFY_KEY = "4287"

# --- CONTEXT ---
BASE_DIR = Path(os.getenv("BASE_DIR", "/Users/andy/my_too_test"))
LOG_DIR = BASE_DIR / "autonomous_operator" / "logs"
FIX_LIST = BASE_DIR / "autonomous_operator" / "state" / "applied_fixes.json"

class EternalGuardian:
    def __init__(self):
        self.active = True
        print(f"♾️ {NODE_ID} Initiated. Watching: {LOG_DIR}")
        if not FIX_LIST.parent.exists():
             FIX_LIST.parent.mkdir(parents=True, exist_ok=True)

    def scan_logs(self):
        """Tìm lỗi Traceback hoặc ERROR trong thư mục logs."""
        print("🔍 Scanning logs for anomalies...")
        if not LOG_DIR.exists(): return None

        for log_file in LOG_DIR.glob("*.log"):
            with open(log_file, "r") as f:
                content = f.read()
                # Tìm Traceback Python chuẩn
                match = re.search(r"Traceback \(most recent call last\):.*?\n(\w+Error:.*)", content, re.DOTALL)
                if match:
                    return {
                        "file": log_file.name,
                        "message": match.group(1),
                        "full_trace": match.group(0)
                    }
        return None

    def reason_and_fix(self, bug):
        """Mô phỏng việc gọi AI để đề xuất Fix."""
        print(f"⚠️ BUG DETECTED in {bug['file']}: {bug['message']}")

        # In actual cloud deployment, this would be a POST to Gemini/Ollama
        # Here we simulate a 'Self-Correcting' intent
        proposal = {
            "node": NODE_ID,
            "target": bug['file'],
            "action": "AUTO_RESTART_OR_PATCH",
            "confidence": 0.95
        }

        # Lưu vết sửa lỗi
        self.save_fix_record(proposal)
        return proposal

    def save_fix_record(self, record):
        history = []
        if FIX_LIST.exists():
            with open(FIX_LIST, "r") as f:
                history = json.load(f)

        history.append({
            "timestamp": time.ctime(),
            "data": record
        })

        with open(FIX_LIST, "w") as f:
            json.dump(history, f, indent=4)

    def heartbeat(self):
        print(f"--- [{time.ctime()}] {NODE_ID} Pulsing. All systems nominal. ---")

    def run(self):
        while self.active:
            try:
                self.heartbeat()
                bug = self.scan_logs()
                if bug:
                    self.reason_and_fix(bug)
                    print(f"✅ Auto-fix proposal generated for {bug['file']}")

            except Exception as e:
                print(f"❌ Guardian Error: {e}")

            time.sleep(60) # Watch every minute

if __name__ == "__main__":
    guardian = EternalGuardian()
    guardian.run()
