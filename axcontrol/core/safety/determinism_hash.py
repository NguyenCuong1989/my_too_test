"""Determinism hash helpers.

Computes per-step hash over state_before, intent, command, and effect to ensure replay equivalence.
"""

import hashlib
import json
from typing import Any


def compute_determinism_hash(state_before: Any, intent: Any, command: Any, effect: Any) -> str:
    payload = json.dumps(
        {
            "state_before": state_before,
            "intent": intent,
            "command": command,
            "effect": effect,
        },
        sort_keys=True,
        default=str,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()
