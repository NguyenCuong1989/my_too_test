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
"""Audit record schema."""

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class AuditRecord:
    timestamp: float
    state_before: Any
    intent: Any
    command: Any
    policy_decision: Any
    state_after: Any
    Chung: str
    stop_reason: Optional[str] = None
    hex_bits: Optional[str] = None
