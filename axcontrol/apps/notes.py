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
"""Notes policy with text guard."""

from core.Menh.stop_reasons import StopReason


def allow_action(role: str, action: str, label: str | None = None):
    """
    Returns tuple (allowed: bool, stop_reason: str|None)
    """
    if role == "AXTextArea":
        return False, StopReason.TEXT_EDIT_BLOCKED.value
    if action != "TAB":
        return False, None
    # TAB allowed across sidebar/list/toolbar elements
    if role in {"AXRow", "AXList", "AXListItem", "AXButton"}:
        return True, None
    return False, None
