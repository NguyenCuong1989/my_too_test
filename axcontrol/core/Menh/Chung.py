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
"""Determinism hash helpers.

Computes per-step hash over state_before, intent, command, and effect to ensure replay equivalence.
"""

import hashlib
import json
from typing import Any, Optional


def compute_Chung(
    state_before: Any,
    intent: Any,
    command: Any,
    effect: Any,
    prev_Chung: Optional[str] = None,
) -> str:
    payload_dict = {
        "state_before": state_before,
        "intent": intent,
        "command": command,
        "effect": effect,
    }
    if prev_Chung:
        payload_dict["prev_Chung"] = prev_Chung

    payload = json.dumps(payload_dict, sort_keys=True, default=str).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()
