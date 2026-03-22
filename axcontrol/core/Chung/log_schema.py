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
from typing import Any, Dict, Optional


@dataclass
class AuditRecord:
    timestamp: float
    state_before: Any
    intent: Any
    command: Any
    policy_decision: Any
    state_after: Any
    Chung: str
    timeline_id: Optional[str] = None
    identity_tuple: Optional[Dict[str, str]] = None
    proof_result: Optional[str] = None
    hash_prev: Optional[str] = None
    hash_curr: Optional[str] = None
    step_index: int = 0
    chained_hash: Optional[str] = None
    stop_reason: Optional[str] = None
    hex_bits: Optional[str] = None
    override_flag: bool = False
    kill_switch_active: bool = False
    evidence_level: int = 2  # Default to Level 2 (strong signal)
