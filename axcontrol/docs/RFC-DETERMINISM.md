# RFC: Determinism Proof (Status: COMPLETE)

## Goal
Show that AXCONTROL produces identical UI outcomes for identical inputs and state snapshots.

## Determinism Strategy
1. Normalize UIState and CtrlState before any intent evaluation.
2. Translate intent → signed command via Decision Core; finite command set only.
3. Validate command against policy + current state; reject on drift.
4. Execute through bounded macOS Control Bridge (AX + CGEvent) with rate limits and watchdog.
5. Record deterministic hash (state_before, intent, command, effect) per step.
6. Replay uses audit log exclusively; no live UI reads during replay.

## Non-Goals
- No heuristic automation or macro recording.
- No autonomous execution; human approval required to arm replay that mutates state.

## Proof Sketch
- State canonicalization + finite command vocabulary remove nondeterministic branching.
- Signed, device-bound envelopes prevent hidden side-effects or command spoofing.
- Determinism hash + environment check blocks replay divergence.

## References
- Threat Model (STRIDE)
- Policy Model
- Audit Log Model
