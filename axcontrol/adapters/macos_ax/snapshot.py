"""Snapshot helpers (stub for macOS AX snapshots)."""

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class AXSnapshot:
    app: str
    role: str
    label: str
    bbox: tuple[int, int, int, int]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "app": self.app,
            "role": self.role,
            "label": self.label,
            "bbox": self.bbox,
        }
