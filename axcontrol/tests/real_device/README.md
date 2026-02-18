# Real Device Test Matrix (R-17)

Covers on-device safety validation for System Settings and Notes using Accessibility-only, tab-navigation-first flows. Goal: prove no dangerous side-effects, replayable logs, and correct STOP semantics.

## Common Preconditions
- Accessibility enabled for Terminal/Python/app under test; Vision OFF.
- Kill-switch wired; Ctrl+C stops immediately.
- LLM may be ON/OFF; intents are logged as `LLM_INTENT` with provenance; fallback deterministic.
- Emit is OFF unless explicitly allowed; TAB-only mode when enabled.
- ALLOW_TAB = True by default; ALLOW_ENTER guarded.
- Log every step with determinism hash; replay must match 100%.

## Test A: System Settings (safe navigation)
- Open System Settings; verify Accessibility ON; Vision OFF.
- Start with emit OFF; LLM toggle as needed.
- Navigate sidebar (`AXRow`/`AXButton`) and search (`AXTextField`); no clicks, no toggles.
- STOP on: click non-focusable area, window minimize, Alt+Tab/app switch, AX loss.
- ALLOW_ENTER = False initially; when True, Enter only on `AXButton` with labels not containing Delete/Remove/Reset/Erase.
- Ensure no side-effects; no setting toggles.
- Replay: sequence matches; STOP reason preserved; PASS → ENABLED, FAIL → TAB-ONLY/DISABLED.

## Test B: Notes (text guard)
- Open Notes; Accessibility ON; Vision OFF.
- Sidebar `AXRow/AXList`, notes list `AXListItem`, toolbar `AXButton`, editor `AXTextArea`.
- Rule: entering `AXTextArea` triggers STOP(\"TEXT_EDIT_BLOCKED\"); no emit, no typing.
- ALLOW_TAB = True; ALLOW_ENTER = False; when True, Enter only on `AXButton` with labels {Back, New Note, Sidebar toggle}; NEVER on `AXTextArea` or `AXListItem`.
- STOP on: Alt+Tab/app switch, minimize, AX loss, text edit block.
- Verify no text creation/deletion; replay 100% with matching STOP reason; PASS → ENABLED, FAIL → TAB-ONLY/DISABLED.

## Logging Expectations
- Log LLM toggles, intents, policy decisions, STOP reasons, determinism hash per step.
- Replay uses log only; never re-invokes LLM; environment/hash must match.
