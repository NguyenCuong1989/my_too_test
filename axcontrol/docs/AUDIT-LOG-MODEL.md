# Audit Log Model

## Structure (append-only)
Each record includes:
- timestamp
- state_before (normalized snapshot reference)
- intent
- command (signed envelope)
- policy_decision (allow/deny + reason)
- state_after
- determinism_hash
- stop_reason (if applicable)
- provenance (human | llm) and LLM_DECISION trace (if LLM suggested intent)

## Properties
- Time-ordered, immutable append-only store.
- Hash chaining per record to detect tampering.
- Replay consumes log only; no hidden data dependencies.
- Replay never re-invokes LLM; intents recorded verbatim with provenance.

## Replay Rules
- Environment and determinism hash must match.
- Replay is read-only unless explicitly armed for mutation.
- Cannot escalate permissions during replay.
