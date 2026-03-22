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
"""CtrlState schema.

Tracks control-plane lifecycle, policy counters, and determinism hash for the last step.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class SessionStatus(str, Enum):
    IDLE = "idle"
    ARMED = "armed"
    EXECUTING = "executing"
    PAUSED = "paused"
    STOPPED = "stopped"


@dataclass
class CtrlState:
    status: SessionStatus
    Chung: Optional[str] = None
    rate_counter: int = 0
    last_app: Optional[str] = None
    last_ui_surface: Optional[str] = None
    last_stop_reason: Optional[str] = None
