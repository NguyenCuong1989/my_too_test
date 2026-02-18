# AXCONTROL — Deterministic macOS UI Control System

## Mission
- Build a system-level macOS UI control plane that is deterministic, auditable, replayable, and always human-in-the-loop.
- AI provides intent proposals only; execution is policy-gated, signed, and bounded to local macOS authority.

## Core Properties
- Deterministic execution: state → intent → command → effect; deterministic hash per run.
- Audit-first: append-only logs with state_before/intent/command/policy_decision/state_after; replay drives recovery.
- Policy & permission gating: finite command set, signed envelopes, allow/deny + rate/time/UI-surface guards.
- Safety: watchdog, explicit STOP reasons, local kill-switch, no hidden side effects.

## Control & Trust Model
- Human → Mobile App (control plane) or CLI (local authority).
- AI → intent proposal only; never executes actions.
- Vision → symbol extraction only; non-authoritative.
- Trusted: Human user, macOS core, Decision Core. Semi-trusted: Mobile app UI. Untrusted: target apps, LLM, network.

## Scope (delivery targets)
- macOS Control Bridge (AX/CGEvent/window/app lifecycle)
- UI Event Engine + deterministic state machine
- Audit/Log/Replay engine
- Mobile control plane (iOS/Web)
- SDK/API surface (Python/TypeScript)
- Optional bounded Vision, optional LLM intent adapter

## Invariants (must never break)
- No UI action without explicit intent
- Every action logged and replayable
- AI cannot bypass policy; human override always wins
- Commands are signed, device-bound; no runtime privilege escalation

## Status (Feb 18, 2026)
- Public repo initialized; specs committed
- core/state present; decision & execution partial
- Control bridge and mobile app skeletons exist
- Real device test scripts exist; promote flow defined

## Working Rules
- Responses numbered R-xx are authoritative
- Phase 1: design/reasoning; Phase 2: commands on request
- Context is append-only; no silent changes

See `docs/` for locked specs and models. Implementation stubs in `core/` adhere to deterministic, audited execution with human-in-the-loop control.

## R-17 Checklist Anchors
- LLM: local-only (Ollama), intent suggestions with 200ms timeout, logged as `LLM_INTENT`, never executes actions.
- Default model now uses locally available `qwen3:8b`; adjust `LLM_CMD` in `core/decision/llm_strategy.py` if you change the local model.
- Real-device tests: System Settings (safe navigation) and Notes (text guard) run in TAB-first mode with explicit STOP reasons.
- AX observer + TAB-only emitter: STOP on AX loss/app switch; rate-limited; no Enter/click in safe mode.
- Packaging/signing: bundle as `.app`, codesign & notarize for Gatekeeper compliance (see `ops/release_checklist.md`).
