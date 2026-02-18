# Failure Taxonomy

## Explicit Failure Modes
- Vision mismatch
- UI state drift
- Policy denial
- Permission loss
- Timing violation
- Human abort
- Kill-switch trigger
- Text edit blocked (when entering guarded editors like Notes)
- AX loss or app switch during guarded navigation

## Handling Rules
- Stop → log → await human decision
- No auto-retry without explicit approval
- Record stop_reason and determinism hash in audit log

## Recovery
- Replay allowed only with environment + hash match
- Resume requires human approval; policy re-evaluation mandatory
