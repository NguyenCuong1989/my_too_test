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
#!/usr/bin/env bash
set -euo pipefail

echo "[1/3] compileall core..."
python3 -m compileall core >/dev/null

echo "[2/3] property check (XOR invariants)..."
python3 tools/verify_canon_properties.py

echo "[3/3] git status..."
git status --short

echo "HEALTH CHECK DONE."
