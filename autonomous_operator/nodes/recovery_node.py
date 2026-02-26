import logging
import ollama
import sys
from pathlib import Path

class RecoveryNode:
    """Tự động kiểm tra sức khoẻ AI Engine — giờ dùng Ollama Local (offline, unlimited)"""

    AI_MODEL = "qwen3:8b"

    def __init__(self):
        self.logger = logging.getLogger("RecoveryNode")

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
            self.logger.info(f"✅ Ollama ({self.AI_MODEL}) is healthy. Response: {result[:30]}")
        except Exception as e:
            self.logger.error(f"❌ Ollama health check failed: {e}")
            self.logger.warning("Make sure Ollama is running: 'ollama serve'")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    node = RecoveryNode()
    node.run_cycle()
