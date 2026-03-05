# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

#!/usr/bin/env python3
"""
🤖 TITAN GT77 WORKER — v2.0 (Auto-Discovery)
Chạy script này trên Titan để tự động xử lý tasks từ MacBook.
Không cần admin, không cần firewall — chỉ cần: git + ollama + python3

Setup 1 lần:
  pip install ollama
  git clone https://github.com/NguyenCuong1989/DAIOF-Framework.git C:\DAIOF_Queue

Chạy:
  python titan_worker.py
"""
import json
import time
import subprocess
import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [Titan-Worker] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

try:
    import ollama
except ImportError:
    logging.error("Missing: pip install ollama")
    sys.exit(1)

from pathlib import Path

# --- CONFIG (Tự động detect đường dẫn theo vị trí script) ---
# Vì Titan đã có DAIOF-Framework, queue nằm ngay trong repo
QUEUE_DIR = Path(__file__).parent.parent  # Gốc repo DAIOF-Framework
TASKS_DIR = QUEUE_DIR / ".ai_queue" / "tasks"
RESULTS_DIR = QUEUE_DIR / ".ai_queue" / "results"

def get_model():
    """Tự động phát hiện model mạnh nhất đang có trên Titan"""
    try:
        models = ollama.list()
        names = [m['name'] for m in models.get('models', [])]
        logging.info(f"🧠 Available models: {names}")
        # Ưu tiên model to nhất theo tên
        for candidate in ['llama3:70b', 'qwen2.5:72b', 'qwen3:32b', 'mistral:7b', 'qwen3:8b']:
            if any(candidate in n for n in names):
                return candidate
        return names[0] if names else "qwen3:8b"
    except Exception as e:
        logging.error(f"Cannot list models: {e}")
        return "qwen3:8b"

def git_sync(action: str):
    """Pull hoặc push repository"""
    try:
        if action == "pull":
            subprocess.run(["git", "pull", "--rebase"], cwd=str(QUEUE_DIR),
                           capture_output=True, timeout=30)
        elif action == "push":
            subprocess.run(["git", "add", "."], cwd=str(QUEUE_DIR), timeout=15)
            subprocess.run(["git", "commit", "-m", f"[TITAN] Result {time.strftime('%H:%M:%S')}"],
                           cwd=str(QUEUE_DIR), capture_output=True, timeout=15)
            subprocess.run(["git", "push"], cwd=str(QUEUE_DIR), capture_output=True, timeout=30)
    except Exception as e:
        logging.warning(f"Git {action} warning: {e}")

def process_task(task: dict, model: str) -> str:
    """Xử lý task bằng Ollama 120B"""
    logging.info(f"🔥 Processing: {task['id']} | type: {task.get('type','unknown')}")
    try:
        resp = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": task["prompt"]}],
            options={"temperature": 0.3}
        )
        result = resp["message"]["content"]
        # Loại bỏ thẻ <think> nếu có (CoT models)
        if "<think>" in result:
            result = result.split("</think>")[-1].strip()
        logging.info(f"✅ Done: {task['id']} ({len(result)} chars)")
        return result
    except Exception as e:
        logging.error(f"Model error: {e}")
        return f"[ERROR] {e}"

def main():
    TASKS_DIR.mkdir(parents=True, exist_ok=True)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    model = get_model()
    logging.info(f"🤖 Titan GT77 Worker ACTIVE | Model: {model}")
    logging.info(f"📂 Queue: {QUEUE_DIR}")
    logging.info("⏳ Waiting for tasks from MacBook...")

    while True:
        try:
            # 1. Kéo task mới từ Git
            git_sync("pull")

            processed_any = False
            for task_file in TASKS_DIR.glob("*.json"):
                try:
                    task = json.loads(task_file.read_text(encoding='utf-8'))
                except:
                    continue

                if task.get("status") != "pending":
                    continue

                # 2. Xử lý task
                task["status"] = "processing"
                task_file.write_text(json.dumps(task, ensure_ascii=False))

                result_text = process_task(task, model)

                # 3. Ghi kết quả
                result_file = RESULTS_DIR / f"{task['id']}.json"
                result_file.write_text(json.dumps({
                    "id": task["id"],
                    "type": task.get("type"),
                    "status": "done",
                    "result": result_text,
                    "processed_by": f"Titan-GT77 ({model})",
                    "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S')
                }, ensure_ascii=False, indent=2))

                # 4. Đánh dấu task complete
                task["status"] = "complete"
                task_file.write_text(json.dumps(task, ensure_ascii=False))

                processed_any = True

            # 5. Push kết quả lên Git nếu có task mới
            if processed_any:
                git_sync("push")
                logging.info("📤 Results pushed to Git")

        except KeyboardInterrupt:
            logging.info("Worker stopped by user.")
            break
        except Exception as e:
            logging.error(f"Worker error: {e}")

        time.sleep(15)

if __name__ == "__main__":
    main()
