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
from adapters.macos_ax.safari import safari_context


def allow_action(
    role: str, action: str, label: str | None = None
) -> Tuple[bool, Optional[str]]:
    ctx = safari_context(role, label or "")
    zone = ctx.get("zone")
    if zone in {"ADDRESS_BAR", "WEB_CONTENT"}:
        return False, "forbidden_zone"
    allowed = action == "TAB"
    return allowed, None if allowed else "unsupported_action"
