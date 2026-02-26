import os
import subprocess
import time
from pathlib import Path

# Base directory
BASE_DIR = Path("/Users/andy/my_too_test")
LAUNCH_SCRIPT = BASE_DIR / "start_daiof.sh"
PID_FILE = BASE_DIR / "autonomous_operator" / "state" / "orchestrator.pid"
LOG_FILE = BASE_DIR / "autonomous_operator" / "logs" / "eternal_monitor.log"

def is_running(pid):
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False

def monitor():
    print(f"♾️ Eternal Monitor started for DAIOF...")
    while True:
        try:
            should_restart = False
            if PID_FILE.exists():
                pid = int(PID_FILE.read_text().strip())
                if not is_running(pid):
                    print(f"⚠️ Process {pid} found dead. Restarting...")
                    should_restart = True
            else:
                print(f"⚠️ No PID file found. Initializing...")
                should_restart = True

            if should_restart:
                subprocess.run(["bash", str(LAUNCH_SCRIPT)], cwd=str(BASE_DIR))
                with open(LOG_FILE, "a") as f:
                    f.write(f"[{time.ctime()}] 🔄 System restarted by Eternal Monitor\n")

        except Exception as e:
            print(f"❌ Monitor Error: {e}")

        time.sleep(60) # Watch every minute

if __name__ == "__main__":
    monitor()
