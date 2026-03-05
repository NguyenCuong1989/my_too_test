# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

#!/usr/bin/env python3
"""
Σ_APΩ₂ RUNTIME KERNEL - Unified AI-OS Operating System Kernel
Architecture: D&R Protocol v2.0
Master Coordinator for Telegram Bot and Factory Worker.
"""
import os
import sys
import time
import subprocess
import logging
import signal
from pathlib import Path

# --- CONFIGURATION ---
BASE_DIR = Path("/Users/andy/my_too_test").resolve()
LOG_FILE = BASE_DIR / "logs" / "kernel_master.log"
PROCESSES = {
    "factory_worker": BASE_DIR / "factory" / "factory_worker.py",
    "telegram_bot": BASE_DIR / "factory" / "telegram_bot.py"
}

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [KERNEL] - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()]
)

class APOKernel:
    def __init__(self):
        self.active_processes = {}
        self.running = True

    def start_process(self, name, script_path):
        """Khởi chạy một tiến trình con và giám sát."""
        logging.info(f"🚀 Starting {name}: {script_path}")
        proc = subprocess.Popen([sys.executable, str(script_path)],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        self.active_processes[name] = proc
        return proc

    def check_health(self):
        """Kiểm tra trạng thái sống của các tiến trình."""
        for name, proc in list(self.active_processes.items()):
            if proc.poll() is not None:
                logging.error(f"💀 Process {name} DIED with exit code {proc.returncode}")
                # Restart logic
                self.start_process(name, PROCESSES[name])

    def shutdown(self, signum, frame):
        """Tắt hệ thống an toàn."""
        logging.info("🛑 Shutdown signal received. Closing all neural links...")
        self.running = False
        for name, proc in self.active_processes.items():
            proc.terminate()
        sys.exit(0)

    def run(self):
        logging.info("🏛️ Σ_APΩ₂ RUNTIME KERNEL INITIALIZED")
        signal.signal(signal.SIGINT, self.shutdown)
        signal.signal(signal.SIGTERM, self.shutdown)

        # Khởi chạy ban đầu
        for name, path in PROCESSES.items():
            if not Path(path).exists():
                logging.warning(f"⚠️ Skip {name}: File not found at {path}")
                continue
            self.start_process(name, path)

        # Loop giám sát vô hạn
        while self.running:
            self.check_health()
            time.sleep(10)

if __name__ == "__main__":
    # Đảm bảo thư mục log tồn tại
    (BASE_DIR / "logs").mkdir(exist_ok=True)
    kernel = APOKernel()
    kernel.run()
