# System Architecture

## Planes
- **Control Plane:** Human via mobile/web/CLI; submits intents, lifecycle commands; read-only log access.
- **Decision Core:** Single source of execution truth; validates intents → commands; enforces policy and state checks.
- **Execution Plane:** macOS-local bounded executor (AX + CGEvent); watchdog + rate limits; logs effects.
- **Observability Plane:** Trace, state diff, failure taxonomy; feeds audit log and status surfaces.

## Data Path (Deterministic Loop)
1. UIState normalized; CtrlState tracked.
2. Intent proposal (human/LLM) → validated against state and policy.
3. Signed command envelope produced; device-bound.
4. Executor performs bounded action; records effect + determinism hash.
5. Audit log append; STOP conditions evaluated; human override always wins.

## LLM Integration (sandboxed, intent-only)
- Local-only LLM (e.g., Ollama) generates *intent suggestions*; never emits executable actions.
- Guardrails: 200ms timeout, clamped intent schema, fallback to None; cannot override STOP.
- LLM decisions are logged as `LLM_DECISION` / `LLM_INTENT`; replay never re-calls LLM.
- Toggleable `LLM_MODE`; pipeline remains deterministic when LLM off.

## Replay Path
- Consumes audit log only; environment + hash must match; read-only unless explicitly armed.

## Bounded Integrations
- Vision: symbol extraction; non-authoritative.
- LLM: intent/strategy only; cannot emit executable actions.

## Safety & Governance
- Kill-switch local-only.
- Numbered states (R-xx) authoritative; decisions append-only.
- No runtime privilege escalation; no hidden side effects.
