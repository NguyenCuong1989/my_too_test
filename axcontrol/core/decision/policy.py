"""Policy decision data structures.

Policies are evaluated before execution; deny is terminal for the step.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class PolicyOutcome(str, Enum):
    ALLOW = "allow"
    DENY = "deny"


@dataclass
class PolicyVerdict:
    outcome: PolicyOutcome
    reason: Optional[str] = None
    rate_limit_remaining: Optional[int] = None
