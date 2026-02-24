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
from __future__ import annotations

from typing import Tuple, Optional


def allow_action(
    role: str, action: str, label: str | None = None
) -> Tuple[bool, Optional[str]]:
    # Finder safe mode: allow TAB navigation only
    allowed = action == "TAB"
    return allowed, None if allowed else "unsupported_action"
