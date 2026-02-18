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
"""Safari policy."""

from adapters.macos_ax.safari import safari_context


def allow_action(role: str, label: str, action: str) -> bool:
    ctx = safari_context(role, label)
    zone = ctx.get("zone")
    if zone in {"ADDRESS_BAR", "WEB_CONTENT"}:
        return False
    return action == "TAB"
