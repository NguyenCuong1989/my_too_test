import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from core.loop.control_loop import run

os.environ["AXCONTROL_SIM"] = "1"

if __name__ == "__main__":
    records = run(iterations=3)
    print("records:", len(records))
