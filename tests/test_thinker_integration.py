# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

import sys
import os
from pathlib import Path

# Add paths to sys.path
BASE_DIR = Path("/Users/andy/my_too_test")
sys.path.append(str(BASE_DIR / "autonomous_operator"))
sys.path.append(str(BASE_DIR / "hyperai_phoenix"))
sys.path.append(str(BASE_DIR / "hyperai_phoenix/app/brain"))

from thinker import StrategicThinker

def test_thinker_key_loading():
    print("🧪 Testing StrategicThinker Key Integration...")

    # Initialize Thinker
    thinker = StrategicThinker(config_path="/Users/andy/my_too_test/hyperai_phoenix/configs")

    # Verify the key loaded from KeyManager
    print(f"Thinker Active Key: {thinker.api_key[:10]}...")

    # Verify it matches the current index in pool
    from key_manager import GeminiKeyManager
    km = GeminiKeyManager(base_dir=BASE_DIR)
    current_pool_key = km.get_active_key()

    if thinker.api_key == current_pool_key:
        print("✅ Thinker successfully loaded the key from GeminiKeyManager pool.")
    else:
        print("❌ Thinker failed to load the correct key from pool.")

if __name__ == "__main__":
    test_thinker_key_loading()
