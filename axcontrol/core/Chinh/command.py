"""Command envelope schema.

Finite command set; envelopes are signed and device-bound. No direct mapping to raw UI actions.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Dict


class CommandType(str, Enum):
    CLICK = "click"
    TYPE = "type"
    SELECT = "select"
    NAVIGATE = "navigate"
    CONTROL = "control"  # start/pause/resume/stop/kill
    CLI = "cli"  # bounded shell tool


@dataclass
class CommandEnvelope:
    command_id: str
    intent_id: str
    command_type: CommandType
    parameters: Dict[str, str]
    normalized_state_hash: str
    policy_context: Dict[str, str]
    signature: str  # device-bound signature
