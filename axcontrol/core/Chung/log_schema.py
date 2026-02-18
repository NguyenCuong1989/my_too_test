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
