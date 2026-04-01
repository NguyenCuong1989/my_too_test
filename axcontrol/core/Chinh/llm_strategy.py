# =============================================================================
# PROJECT: CANON-TO-SYSTEM DETERMINISTIC PROJECTION
# METHOD: D&R PROTOCOL (CLOSED)
#
# ORIGINATOR / CREATOR:
#   alpha_prime_omega
#
# LEGAL ONTOLOGY:
#   This source file is a deterministic projection of a closed Canon.
#   Removal or alteration of this header voids legal and ontological validity.
#
# STATUS:
#   GENERATED — NON-AUTONOMOUS — NON-OWNERLESS
#
# TRACEABILITY:
#   Canon -> COG -> Projection(Π) -> Artifact
#
# =============================================================================
"""
LLM intent strategy (local-only, API-based).

- Uses local Ollama API to suggest intents.
- Enforces 2.0s timeout and deterministic fallback to None.
- Replay must not re-invoke the LLM.
"""

import json
import urllib.request
from typing import Optional, Dict

from .intent import Intent, IntentSource

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen3:8b"
TIMEOUT_S = 2.0


def build_system_prompt() -> str:
    return (
        "You propose high-level intents for macOS UI control. "
        "Do not output actions. Output ONLY valid JSON with keys: intent_id, goal, parameters. "
        "Example: {\"intent_id\": \"open-safari\", \"goal\": \"Open Safari browser\", \"parameters\": {}} "
        "Keep it deterministic and minimal."
    )


def suggest_intent(context: Dict[str, str]) -> Optional[Intent]:
    """
    Returns an Intent or None via HTTP API. Deterministic fallback on any error/timeout.
    """
    payload = {
        "model": MODEL_NAME,
        "prompt": f"System: {build_system_prompt()}\nContext: {json.dumps(context)}\nIntent JSON:",
        "stream": False,
        "format": "json"
    }

    try:
        req = urllib.request.Request(
            OLLAMA_API_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=TIMEOUT_S) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            raw_response = res_data.get("response", "")
            data = json.loads(raw_response)

            return Intent(
                intent_id=data.get("intent_id", "ai-intent"),
                goal=data.get("goal", ""),
                parameters=data.get("parameters", {}) or {},
                source=IntentSource.LLM,
                rationale=data.get("rationale"),
            )
    except Exception as e:
        print(f"DEBUG: LLM API error: {e}")
        return None
