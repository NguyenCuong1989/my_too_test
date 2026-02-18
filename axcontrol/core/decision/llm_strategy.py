"""
LLM intent strategy (local-only, sandboxed).

- Uses local LLM (e.g., Ollama) to suggest intents.
- Enforces 200ms timeout and deterministic fallback to None.
- Never emits executable actions; cannot override STOP.
- Replay must not re-invoke the LLM.
"""

import json
import subprocess
from typing import Optional, Dict

from .intent import Intent, IntentSource


LLM_CMD = ["ollama", "run", "qwen3:8b"]  # uses locally available model; adjust if needed
TIMEOUT_S = 0.2


def build_system_prompt() -> str:
    return (
        "You propose high-level intents for macOS UI control. "
        "Do not output actions. Schema: {intent_id, goal, parameters}. "
        "Keep it deterministic and minimal."
    )


def suggest_intent(context: Dict[str, str]) -> Optional[Intent]:
    """
    Returns an Intent or None. Deterministic fallback on any error/timeout.
    """
    try:
        prompt = json.dumps({"system": build_system_prompt(), "context": context})
        raw = subprocess.run(
            LLM_CMD,
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            timeout=TIMEOUT_S,
            check=False,
        ).stdout.decode("utf-8", errors="ignore")
    except Exception:
        return None

    try:
        data = json.loads(raw)
        return Intent(
            intent_id=data.get("intent_id", ""),
            goal=data.get("goal", ""),
            parameters=data.get("parameters", {}) or {},
            source=IntentSource.LLM,
            rationale=data.get("rationale"),
        )
    except Exception:
        return None
