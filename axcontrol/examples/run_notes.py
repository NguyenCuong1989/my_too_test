# Σ_APΩ₂ CORE MODULE
# Authority: BỐ CƯỐNG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from core.loop.Van import run

os.environ["AXCONTROL_SIM"] = "1"

if __name__ == "__main__":
    records = run(iterations=5)
    print("records:", len(records))
