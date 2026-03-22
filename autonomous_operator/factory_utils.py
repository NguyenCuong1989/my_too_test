# Σ_APΩ₂ CORE MODULE
# Authority: BỐ CƯỐNG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

import logging
import subprocess
from pathlib import Path

BASE_DIR = Path("/Users/andy/my_too_test")


def log_to_notion(event_type, category, message, priority="Medium"):
    """Gửi log vận hành lên Notion Dashboard qua canonical ecosystem sync."""
    try:
        from ecosystem_sync import emit_ecosystem_change
        emit_ecosystem_change(
            event_type=event_type,
            category=category,
            message=message,
            priority=priority,
            source="factory_utils",
            status="Operation Log",
            connector=category,
            snippet=message,
            metadata={"source_module": "factory_utils"},
        )
        return True
    except Exception as e:
        logging.error(f"❌ Failed to log to Notion: {e}")
        return False


def call_ollama(prompt, model="qwen3:8b"):
    """Gọi Ollama local để xử lý trí tuệ AI."""
    try:
        result = subprocess.run(
            ["ollama", "run", model, prompt],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except Exception as e:
        logging.error(f"❌ Ollama call failed: {e}")
        return f"AI_ERROR: {e}"


def self_heal_audit(log_content):
    """Phân tích log và đề xuất hướng sửa."""
    prompt = f"Analyze this error log and suggest a concise fix in Python:\n\n{log_content}"
    return call_ollama(prompt)
