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
# R-29 STATUS

- Legal skeleton: READY
- Identity: EXTERNAL / NOT PRESENT
- Signing: ARMED / BLOCKED BY CANON

# RUNTIME STATE

- Runtime: SEALED
- Lexicon: CLOSED
- Pipeline: FAIL-CLOSED
- Drift: KILLED
- Causality: LOCKED

# R-30 INCARNATION LOGIC (PREP)
- Discovery Mode: ACTIVE via /discover-identity
- Search Space: Apple Portal UI text layer only
- Verification: Strict regex ^Developer ID Application: .+ \\([A-Z0-9]{10}\\)$
- Identity Storage: In-memory session (volatile)
- User Confirmation: MANDATORY (no auto-sign)
- Guardrails: single attempt, TAB/ENTER only, T_guard=5s, STOP on ambiguity/timeouts
