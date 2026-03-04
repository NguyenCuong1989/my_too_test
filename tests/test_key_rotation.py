import sys
import os
from pathlib import Path

# Add paths to sys.path
BASE_DIR = Path("/Users/andy/my_too_test")
sys.path.append(str(BASE_DIR / "autonomous_operator"))

from key_manager import GeminiKeyManager

def test_rotation():
    print("🧪 Starting Key Rotation Test...")
    manager = GeminiKeyManager(base_dir=BASE_DIR)

    # 1. Check initial state
    initial_key = manager.get_active_key()
    initial_idx = int(manager.index_file.read_text().strip())
    print(f"Initial Key (Partial): {initial_key[:10]}... (Index: {initial_idx})")

    # 2. Perform rotation
    print("🔄 Rotating key...")
    new_key = manager.rotate_key()
    new_idx = int(manager.index_file.read_text().strip())

    print(f"New Key (Partial): {new_key[:10]}... (Index: {new_idx})")

    # 3. Verify
    if initial_key != new_key and int(new_idx) != int(initial_idx):
        print("✅ SUCCESS: Key rotated successfully.")
    else:
        print("❌ FAILED: Key did not change or index remained the same.")

    # 4. Check legacy sync
    legacy_key = (BASE_DIR / ".gemini_key").read_text().strip()
    if legacy_key == new_key:
        print("✅ SUCCESS: Legacy .gemini_key synchronized.")
    else:
        print("❌ FAILED: Legacy .gemini_key out of sync.")

if __name__ == "__main__":
    test_rotation()
