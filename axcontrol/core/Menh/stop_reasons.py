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
"""Enumerated STOP reasons (explicit)."""
from enum import Enum


class StopReason(str, Enum):
    VISION_MISMATCH = "vision_mismatch"
    UI_STATE_DRIFT = "ui_state_drift"
    POLICY_DENIAL = "policy_denial"
    PERMISSION_LOSS = "permission_loss"
    TIMING_VIOLATION = "timing_violation"
    HUMAN_ABORT = "human_abort"
    KILL_SWITCH = "Diet"
    TEXT_EDIT_BLOCKED = "text_edit_blocked"
    AX_LOST = "ax_lost"
    APP_SWITCH = "app_switch"
