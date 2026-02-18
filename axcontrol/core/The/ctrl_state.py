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
