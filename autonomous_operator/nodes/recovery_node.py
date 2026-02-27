import logging
import ollama
import sys
from pathlib import Path

# Thêm path để import từ DAIOF-Framework
BASE_DIR = Path("/Users/andy/my_too_test")
sys.path.append(str(BASE_DIR / "autonomous_operator"))
from neural_link import NeuralLink

class RecoveryNode:
    """Tự động kiểm tra sức khoẻ AI Engine — giờ dùng Ollama Local (offline, unlimited)"""

    AI_MODEL = "qwen3:8b"

    def __init__(self):
        self.logger = logging.getLogger("RecoveryNode")
        self.link = NeuralLink()

    def run_cycle(self):
        self.logger.info("🩺 Checking LOCAL AI Engine (Ollama) Health...")
        self.test_ollama()

    def test_ollama(self):
        try:
            response = ollama.chat(
                model=self.AI_MODEL,
                messages=[{"role": "user", "content": "Reply with just: OK"}],
                options={"temperature": 0.0, "num_predict": 10}
            )
            result = response['message']['content'].strip()
            msg = f"✅ Ollama ({self.AI_MODEL}) is healthy. Response: {result[:30]}"
            self.logger.info(msg)
            self.link.log_service_event("RecoveryNode", "STATUS", msg)
        except Exception as e:
            err_msg = f"❌ Ollama health check failed: {e}"
            self.logger.error(err_msg)
            self.logger.warning("Make sure Ollama is running: 'ollama serve'")
            self.link.log_service_event("RecoveryNode", "SYSTEM_ERROR", err_msg)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    node = RecoveryNode()
    node.run_cycle()
