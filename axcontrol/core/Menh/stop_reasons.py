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
