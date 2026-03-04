import sys
from pathlib import Path

BASE_DIR = Path("/Users/andy/my_too_test")
sys.path.append(str(BASE_DIR / "autonomous_operator"))
sys.path.append(str(BASE_DIR / "autonomous_operator/nodes"))

from key_manager import GeminiKeyManager

def test_key_manager_integration():
    print("🧪 Testing GeminiKeyManager integration in system...")
    km = GeminiKeyManager(base_dir=BASE_DIR)

    # Check if we can rotate and get the key
    current_key = km.get_active_key()
    print(f"Current Pool Key: {current_key[:10]}...")

    # Simulate a rotation
    km.rotate_key()
    new_key = km.get_active_key()
    print(f"Rotated Pool Key: {new_key[:10]}...")

    if current_key != new_key:
        print("✅ SUCCESS: Autonomous Key Rotation confirmed.")
    else:
        print("❌ FAILED: Key rotation did not work.")

if __name__ == "__main__":
    test_key_manager_integration()
