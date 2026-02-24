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
import time
import hashlib
import json
from typing import Any

from .ui_state import UIState, Window, UIElement


def normalize_ui_state(raw_snapshot: Any) -> UIState:
    """Convert raw platform snapshot into normalized UIState.

    Determinism requirements:
    - Stable identifiers across runs
    - Remove non-deterministic fields
    - No raw pixel or PII leakage
    """
    # Phase 2 implementation: map Snapshot to canonical UIState
    # The observer currently provides a flattened "focused element" view.

    # h-stable ID generation
    element_id = f"{raw_snapshot.app}:{raw_snapshot.role}:{raw_snapshot.label}"

    elem = UIElement(
        role=raw_snapshot.role,
        title=raw_snapshot.label,
        identifier=element_id,
        enabled=True,  # Default to True as simulation/basic observer implies interactive
        focused=True,
        bounds=raw_snapshot.bbox,
    )

    win = Window(
        app=raw_snapshot.app,
        title=None,
        identifier=raw_snapshot.app,
        focused=True,
        elements=[elem],
    )

    state = UIState(windows=[win], timestamp=time.time())

    # Compute deterministic fingerprint (excluding timestamp)
    fingerprint_data = {
        "app": win.app,
        "elements": [{"id": e.identifier, "role": e.role} for e in win.elements],
    }
    state.hash = hashlib.sha256(
        json.dumps(fingerprint_data, sort_keys=True).encode("utf-8")
    ).hexdigest()

    return state
