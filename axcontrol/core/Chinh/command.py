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
"""Command envelope schema.

Finite command set; envelopes are signed and device-bound. No direct mapping to raw UI actions.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Any, Optional


class CommandType(str, Enum):
    CLICK = "click"
    TYPE = "type"
    SELECT = "select"
    NAVIGATE = "navigate"
    CONTROL = "control"  # start/pause/resume/stop/kill
    CLI = "cli"  # bounded shell tool


class AtomicStepType(Enum):
    MOUSE_MOVE = "mouse_move"
    MOUSE_CLICK = "mouse_click"
    KEY_DOWN = "key_down"
    KEY_UP = "key_up"
    WAIT_SETTLE = "wait_settle"
    AX_ACTION = "ax_action"


@dataclass
class AtomicStep:
    """Minimal unit of OS emission."""
    type: AtomicStepType
    target: Optional[str] = None  # UI element identifier or screen coord
    parameters: Dict[str, Any] = field(default_factory=dict)


@dataclass
class CommandEnvelope:
    """Validated, signed executable container."""
    command_id: str
    intent_id: str
    command_type: CommandType
    parameters: Dict[str, Any]
    normalized_state_hash: str
    policy_context: Dict[str, str]
    signature: str  # device-bound signature
    atomic_steps: List[AtomicStep] = field(default_factory=list)
