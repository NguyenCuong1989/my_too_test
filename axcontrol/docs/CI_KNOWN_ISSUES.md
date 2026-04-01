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
# CI KNOWN ISSUES (AXCONTROL)

- Do not run signing/notary in CI (requires Developer ID; ship_it.sh will abort).
- AX observer real-device tests require macOS GUI permissions; mock snapshots for CI.
- Run deterministic checks only:
  - `python3 -m compileall core`
  - `python3 tools/verify_canon_properties.py`
- Node/UI build optional; skip unless needed for UI pipeline.
- Pin Python version in CI to match local (e.g., 3.11) to avoid module drift.
