# Governance

## Rules
- Decisions are append-only; numbered states (R-xx) are authoritative.
- No silent changes; explicit promote criteria required.
- Context version v1.0, lock level HARD; updates require new block and approval.

## Phases
- Phase 1: design/reasoning
- Phase 2: commands on explicit request

## Invariants
- No UI action without explicit intent
- Every action logged and replayable
- AI never bypasses policy; human override always wins

## Change Control
- Promote flow controlled (already defined in ops)
- Public bundle export at spec level only
