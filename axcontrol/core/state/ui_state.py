"""UIState schema.

Represents normalized, replayable snapshot of the visible macOS UI relevant to a command.
No raw pixels; identifiers are stable across runs for determinism.
"""
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class UIElement:
    role: str
    title: Optional[str]
    identifier: str  # stable deterministic id
    enabled: bool
    focused: bool
    bounds: tuple[int, int, int, int]  # x, y, w, h


@dataclass
class Window:
    app: str
    title: Optional[str]
    identifier: str
    focused: bool
    elements: List[UIElement] = field(default_factory=list)


@dataclass
class UIState:
    windows: List[Window]
    timestamp: float
    hash: Optional[str] = None  # set by determinism hash step
