# Policy Model

## Principles
- Static allow/deny plus context-aware constraints.
- Applied before execution; deny is terminal for the step.

## Controls
- UI surface allowlist (per app/role)
- App allowlist + boundaries
- Rate limits per domain/action
- Time-based guards

## Evaluation
1. Gather policy context from CtrlState (rate counters, time, app).
2. Validate command envelope parameters against schemas.
3. Apply rules in deterministic order; produce allow/deny + reason.
4. Emit policy_decision into audit log.

## Safety
- No runtime privilege escalation.
- Human override always wins.
