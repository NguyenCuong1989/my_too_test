# Command Model

## Principles
- Finite command set; no 1:1 mapping to raw UI actions.
- Commands are signed, device-bound envelopes containing intent, state hash, and policy context.
- Validation precedes execution: policy gate + state consistency.
- LLM can propose intents, never commands; LLM output is clamped, timed-out (200ms), and logged (`LLM_INTENT`), then converted to commands only if policy allows.

## Envelope Fields (conceptual)
- command_id (uuid)
- intent_id
- normalized_state_hash
- command_type (enum)
- parameters (bounded, schema-validated)
- policy_context (rate, time, UI surface)
- signature (device-bound)
- provenance (human | llm); required for audit/replay; replay never re-calls LLM.
  - includes CLI provenance when using bounded shell tool.

## Flow
intent (human/LLM) → envelope build → policy evaluate → sign → executor dispatch → effect log (with determinism hash + STOP reason if any)

## New bounded command: CLI
- Purpose: read-only diagnostics (`pwd`, `ls`, `cat`, `head`, `tail` with limited flags).
- No pipes/redirects/subshells; metacharacters denied.
- Parameters: validated by `core/tools/shell_cli.py`; logged with stdout/stderr; policy can deny.

## Deny Reasons
- Policy denial (allowlist/rate/time/app boundary)
- State drift / determinism hash mismatch
- Permission loss
- Human abort or kill-switch
