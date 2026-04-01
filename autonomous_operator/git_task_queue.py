# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

"""
🧬 Git Task Queue — Distributed AI via Git
Không cần admin, không cần firewall, không cần network config.
MacBook đẩy task vào Git repo, Titan GT77 kéo về xử lý 120B, push kết quả lại.
"""

import json
import subprocess
import time
import logging
import hashlib
from datetime import datetime
from pathlib import Path

# --- CONFIG ---
# Repo riêng tư của Master, dùng để relay tasks
GIT_QUEUE_REPO = "https://github.com/NguyenCuong1989/DAIOF-Framework.git"
QUEUE_DIR = Path("/Users/andy/my_too_test/.ai_task_queue")
TASKS_PATH = QUEUE_DIR / "tasks"
RESULTS_PATH = QUEUE_DIR / "results"

logger = logging.getLogger("GitTaskQueue")

class GitTaskQueue:
    """
    Hàng đợi tác vụ qua Git — Không cần firewall hay quyền admin.
    """

    def __init__(self, queue_dir: Path = QUEUE_DIR):
        self.queue_dir = queue_dir
        self.tasks_dir = queue_dir / "tasks"
        self.results_dir = queue_dir / "results"
        self._ensure_dirs()

    def _ensure_dirs(self):
        self.tasks_dir.mkdir(parents=True, exist_ok=True)
        self.results_dir.mkdir(parents=True, exist_ok=True)

    def _git(self, *args, check=False):
        """Chạy git command trong queue directory"""
        try:
            result = subprocess.run(
                ["git"] + list(args),
                cwd=str(self.queue_dir),
                capture_output=True, text=True, check=check
            )
            return result.returncode == 0, result.stdout.strip()
        except Exception as e:
            logger.error(f"Git error: {e}")
            return False, ""

    def push_task(self, task_type: str, prompt: str, priority: str = "complex") -> str:
        """MacBook đẩy task vào queue (Git commit & push)"""
        task_id = hashlib.md5(f"{task_type}{prompt}{time.time()}".encode()).hexdigest()[:10]
        task = {
            "id": task_id,
            "type": task_type,
            "prompt": prompt,
            "priority": priority,
            "status": "pending",
            "created": datetime.now().isoformat(),
            "source": "MacBook-M2",
            "target": "Titan-GT77-120B"
        }

        task_file = self.tasks_dir / f"{task_id}.json"
        task_file.write_text(json.dumps(task, indent=2, ensure_ascii=False))
        logger.info(f"📤 Task queued: {task_id} [{task_type}]")

        # Git push (sẽ được Titan kéo về)
        self._git("add", str(task_file))
        self._git("commit", "-m", f"[TASK] {task_id}: {task_type}")
        ok, _ = self._git("push")
        if ok:
            logger.info(f"✅ Task {task_id} pushed to Git queue")
        else:
            logger.warning(f"⚠️ Git push failed — task saved locally")

        return task_id

    def get_result(self, task_id: str, timeout: int = 300) -> str | None:
        """MacBook đợi và lấy kết quả từ Titan"""
        result_file = self.results_dir / f"{task_id}.json"
        deadline = time.time() + timeout

        while time.time() < deadline:
            # Pull kết quả mới nhất
            self._git("pull", "--rebase")

            if result_file.exists():
                data = json.loads(result_file.read_text())
                if data.get("status") == "done":
                    logger.info(f"📥 Result received for {task_id}")
                    return data.get("result")

            time.sleep(10)  # Check mỗi 10 giây

        logger.warning(f"⏰ Timeout waiting for task {task_id}")
        return None


# ============================================================
# SCRIPT NÀY CHẠY TRÊN TITAN GT77
# Titan worker kéo task, xử lý bằng 120B model, đẩy kết quả
# ============================================================

TITAN_WORKER_SCRIPT = '''#!/usr/bin/env python3
"""
🤖 TITAN GT77 WORKER
Chạy script này trên Titan để tự động xử lý tasks từ MacBook.
Không cần admin, chỉ cần: git + ollama + python3
"""
import json, time, subprocess, ollama
from pathlib import Path

QUEUE_DIR = Path("C:/DAIOF_Queue")   # Titan local path
TASKS_DIR = QUEUE_DIR / "tasks"
RESULTS_DIR = QUEUE_DIR / "results"
MODEL = "YOUR_120B_MODEL_NAME"        # Điền tên model 120B của Titan

def process():
    while True:
        # Pull tasks mới
        subprocess.run(["git", "pull", "--rebase"], cwd=str(QUEUE_DIR))

        for task_file in TASKS_DIR.glob("*.json"):
            task = json.loads(task_file.read_text())
            if task.get("status") != "pending": continue

            print(f"🔥 Processing task: {task['id']} with {MODEL}")

            # Xử lý bằng 120B model
            try:
                resp = ollama.chat(
                    model=MODEL,
                    messages=[{"role": "user", "content": task["prompt"]}]
                )
                result_text = resp["message"]["content"]
                if "<think>" in result_text:
                    result_text = result_text.split("</think>")[-1].strip()
            except Exception as e:
                result_text = f"Error: {e}"

            # Ghi kết quả
            result = {"id": task["id"], "status": "done", "result": result_text}
            result_file = RESULTS_DIR / f"{task['id']}.json"
            result_file.write_text(json.dumps(result, ensure_ascii=False))

            # Đánh dấu task đã xong
            task["status"] = "processing"
            task_file.write_text(json.dumps(task))

            # Push kết quả về
            subprocess.run(["git", "add", "."], cwd=str(QUEUE_DIR))
            subprocess.run(["git", "commit", "-m", f"[RESULT] {task['id']}"], cwd=str(QUEUE_DIR))
            subprocess.run(["git", "push"], cwd=str(QUEUE_DIR))
            print(f"✅ Result pushed for {task['id']}")

        time.sleep(15)  # Kiểm tra mỗi 15 giây

if __name__ == "__main__":
    print("🤖 Titan GT77 Worker ACTIVE — Waiting for tasks...")
    process()
'''

def save_titan_worker():
    """Lưu script worker cho Master cài lên Titan"""
    worker_path = Path("/Users/andy/my_too_test/autonomous_operator/titan_worker.py")
    worker_path.write_text(TITAN_WORKER_SCRIPT, encoding='utf-8')
    logger.info(f"✅ Titan worker saved to: {worker_path}")
    return worker_path

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    save_titan_worker()
    print("📋 Titan worker script saved!")
    print("📌 Hướng dẫn cho Titan GT77:")
    print("   1. Clone repo về Titan: git clone <repo>")
    print("   2. Chạy: python titan_worker.py")
    print("   3. Titan sẽ tự kéo task, xử lý, push kết quả")
