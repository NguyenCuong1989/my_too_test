# Σ_APΩ₂ CORE MODULE
# Authority: BỐ CƯỐNG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

import sys
from pathlib import Path

# Thêm đường dẫn để import được KeyManager
sys.path.append("/Users/andy/my_too_test/autonomous_operator")

from key_manager import GeminiKeyManager

def patch_thinker():
    file_path = "/Users/andy/my_too_test/hyperai_phoenix/app/brain/thinker.py"
    content = Path(file_path).read_text()

    # 1. Thêm import nếu chưa có
    if "from key_manager import GeminiKeyManager" not in content:
        content = "from key_manager import GeminiKeyManager\n" + content

    # 2. Cập nhật __init__ để dùng KeyManager
    # Tìm đoạn khởi tạo api_key cũ và thay thế
    old_init_key = "self.api_key = os.getenv('GOOGLE_API_KEY')"
    new_init_key = "self.key_manager = GeminiKeyManager(); self.api_key = self.key_manager.get_active_key() or os.getenv('GOOGLE_API_KEY')"
    content = content.replace(old_init_key, new_init_key)

    Path(file_path).write_text(content)
    print(f"✅ Integrated GeminiKeyManager into {file_path}")

if __name__ == "__main__":
    patch_thinker()
