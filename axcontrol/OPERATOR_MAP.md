# =============================================================================
# PROJECT: CANON-TO-SYSTEM DETERMINISTIC PROJECTION
# METHOD: D&R PROTOCOL (CLOSED)
#
# ORIGINATOR / CREATOR:
#   alpha_prime_omega
#
# LEGAL ONTOLOGY:
#   This source file is a deterministic projection of a closed Canon.
#   Removal or alteration of this header voids legal and ontological validity.
#
# STATUS:
#   GENERATED — NON-AUTONOMOUS — NON-OWNERLESS
#
# TRACEABILITY:
#   Canon -> COG -> Projection(Π) -> Artifact
#
# =============================================================================
# BẢNG ÁNH XẠ TOÁN TỬ (FILE ↔ OPERATOR ROLE)

Canon (Hằng số, bất động)
- CANONICAL_CODEGEN_LAW.md           → IP_HEADER law
- CANON_TRANSITION.md               → XOR transition law
- CANON_HASH.md                     → Hash seal set
- docs/LEXICON_CANON_API_NAMING_LAW.md → Lexicon
- docs/PIPELINE_CANON.md            → Pipeline invariant
- docs/SYSTEM_SCOPE.md              → Scope boundary
- docs/INVARIANT_TESTS_R28.md       → Invariant spec
- docs/STATUS_R29.md                → State log
- core/canon/existence_state.py     → ExistenceState enum
- core/canon/existence_state_map.py → 64-state map (lookup)
- core/The/state_projector.py       → Π: AX snapshot → 6-bit
- core/Menh/stop_reasons.py         → Stop reason constants

Runtime (toán tử chuyển trạng thái)
- core/loop/Van.py                  → ControlLoop (filters + execution)
- core/bridge/http_server.py        → Snapshot bridge (input→decision)
- adapters/macos_ax/observer.py     → Observe
- input/keyboard.py                 → Emit TAB
- core/Menh/rate_limit.py           → Temporal gate
- apps/*                            → App policies

Tool/Test
- tools/generate_existence_map.py   → Build canonical map
- tools/verify_canon_properties.py  → Property check (XOR invariants)
- ops/ship_it.sh                    → Signing ritual (armed)

Docs (mô tả, không hằng)
- Remaining docs/ *.md              → Specs, threat model, UX, etc.
