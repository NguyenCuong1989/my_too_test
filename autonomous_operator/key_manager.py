# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

import os
from pathlib import Path

class GeminiKeyManager:
    def __init__(self, base_dir=None):
        self.base_dir = Path(base_dir or "/Users/andy/my_too_test")
        self.pool_file = self.base_dir / ".gemini_keys_pool"
        self.index_file = self.base_dir / ".gemini_key_index"
        self.active_key_file = self.base_dir / ".gemini_key"

    def _get_keys(self):
        if not self.pool_file.exists():
            return []
        keys = self.pool_file.read_text().splitlines()
        return [k.strip() for k in keys if k.strip()]

    def _get_current_index(self):
        if not self.index_file.exists():
            return 0
        try:
            return int(self.index_file.read_text().strip())
        except ValueError:
            return 0

    def get_active_key(self):
        keys = self._get_keys()
        if not keys: return None
        idx = self._get_current_index() % len(keys)
        return keys[idx]

    def rotate_key(self):
        keys = self._get_keys()
        if not keys: return None
        current_idx = self._get_current_index()
        next_idx = (current_idx + 1) % len(keys)
        with open(self.index_file, "w") as f:
            f.write(str(next_idx))
        new_key = keys[next_idx]
        with open(self.active_key_file, "w") as f:
            f.write(new_key)
        print(f"🔄 [GeminiKeyManager] Rotated to key index {next_idx} (Autonomous Recovery)")
        return new_key

if __name__ == "__main__":
    manager = GeminiKeyManager()
    active = manager.get_active_key()
    if active:
        print(f"Current Active Key: {active[:10]}...")
    else:
        print("No keys found in pool.")
