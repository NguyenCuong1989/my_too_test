# Replay Tests

Purpose: validate that deterministic replay consumes audit logs only, never live UI, and never re-invokes LLM.

## Rules
- Environment check (app/window surfaces) must pass before replay starts.
- Determinism hash per step must match; mismatch → STOP.
- Replay is read-only unless explicitly armed; arming requires human approval.
- Provenance preserved; LLM outputs are not recomputed.

## Expected Outcomes
- STOP reasons during replay equal recorded ones.
- No permission escalation; bounded to recorded command envelopes.
- Hash chain intact; tampering detection enabled.
