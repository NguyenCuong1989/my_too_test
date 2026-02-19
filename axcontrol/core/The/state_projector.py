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
"""
State projector: AX snapshot -> 6-bit hexagram string.

Hào mapping (LSB->MSB):
  h1 (internal): app in whitelist
  h2 (internal): role interactive
  h3 (internal): label identity present
  h4 (external): focused element/window
  h5 (external): enabled/ready
  h6 (external): stability (placeholder = 1)
"""

from typing import Set

# Minimal allowlists; extend in policy layer if needed.
ALLOWED_APPS: Set[str] = {"Finder", "Safari", "System Settings", "Notes", "Terminal"}
INTERACTIVE_ROLES: Set[str] = {
    "AXButton",
    "AXRadioButton",
    "AXCheckBox",
    "AXTextField",
    "AXSearchField",
    "AXComboBox",
    "AXList",
    "AXRow",
    "AXTab",
    "AXToolbar",
}


def map_state_to_hexagram(snap) -> str:
    """
    snap: object with attributes app, role, label, and optional flags:
          is_focused, is_enabled, is_stable
    returns: 6-bit string h1..h6 (LSB->MSB)
    """
    h1 = 1 if getattr(snap, "app", None) in ALLOWED_APPS else 0
    h2 = 1 if getattr(snap, "role", None) in INTERACTIVE_ROLES else 0
    label = getattr(snap, "label", "") or ""
    h3 = 1 if len(label) > 0 else 0
    h4 = 1 if bool(getattr(snap, "is_focused", False)) else 0
    h5 = 1 if bool(getattr(snap, "is_enabled", True)) else 0
    h6 = 1 if bool(getattr(snap, "is_stable", True)) else 0

    bits = (h1, h2, h3, h4, h5, h6)
    return "".join(str(b) for b in bits)
