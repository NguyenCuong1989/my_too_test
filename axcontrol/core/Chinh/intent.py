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
"""Intent object (data only).

Intent is high-level desired outcome; it is not executable. Produced by human or LLM (intent-only) and approved by human.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional


class IntentSource(str, Enum):
    HUMAN = "human"
    LLM = "llm"


@dataclass
class Intent:
    intent_id: str
    goal: str
    parameters: Dict[str, str]
    source: IntentSource
    rationale: Optional[str] = None
