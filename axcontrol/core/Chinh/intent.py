"""Intent object (data only).

Intent is high-level desired outcome; it is not executable. Produced by human or LLM (intent-only) and approved by human.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional


class IntentSource(str, Enum):
    HUMAN = "human"
    LLM = "llm"


@dataclass
class Intent:
    intent_id: str
    goal: str
    parameters: Dict[str, str]
    source: IntentSource
    rationale: Optional[str] = None
