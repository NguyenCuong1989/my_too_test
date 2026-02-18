# State Model

## UIState (external)
- Windows, elements, bounds, roles, labels, focus, enabled state
- Normalized identifiers (no raw pixel data)

## CtrlState (internal)
- Session lifecycle (idle/armed/executing/paused/stopped)
- Policy counters (rate limits, time guards)
- Determinism hash for last executed step
- Watchdog status and stop reason (if any)

## Loop
1. Capture + normalize UIState.
2. Update CtrlState with policy + timing context.
3. Evaluate intent → command; check determinism hash stability; LLM intents are clamped and timed-out.
4. Execute bounded action; update state_after; log.

## Replay
- Uses recorded state_before + commands; no live UI read; never calls LLM during replay.
- Requires environment match + hash match; stop_reason must align for deterministic verification.
