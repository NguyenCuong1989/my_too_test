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
# R-28.1 INVARIANT TEST DESIGN (FORMAL SPEC)

Test Axioms
- Test mô phỏng Thế/Intent, không mô phỏng người.
- Đánh giá Hash/State/Reason; không dựa vào text UI.
- Sai = Diệt; không soft-fail, không retry.

Common TestCase Form
- Input: Thế (canonical), Ý định
- Precondition: StateProof/locked flag (nếu có)
- Action: Vận(Thế, Ý định)
- Expected: Result (Tồn|Diệt|STOP), Reason (nếu có), DeterminismHash (nếu Tồn)
- Forbidden: mọi outcome khác

Group A — Determinism
- A1 SAME INPUT ⇒ SAME HASH: /cli pwd, SIM=1, hash1 == hash2, ALLOW, executor=SHELL.
- A2 DIFFERENT INPUT ⇒ DIFFERENT HASH: Thế_A (app=Finder) vs Thế_B (app=Terminal), cùng intent; hash phải khác.

Group B — State Drift
- B1 UI DRIFT KILL: Sau Chính(StateProof_A), đổi UI rồi Hoá → STOP reason=STATE_DRIFT, no execution.
- B2 NO DRIFT ⇒ ALLOW: Không đổi UI → Tồn, hash present.

Group C — Causality Lock
- C1 DOUBLE COMMIT KILL: Snapshot locked → Vận lần nữa → STOP reason=CAUSALITY_VIOLATION.
- C2 SINGLE COMMIT OK: Thế chưa locked → Lập → locked=true.

Group D — Lexicon Sovereignty
- D1 NON-LEXICON INTENT: Free text không map Lexicon → STOP reason=LEXICON_VIOLATION; no Chính/Hoá.
- D2 VALID LEXICON INTENT: /cli mkdir logs → qua pipeline; ALLOW/STOP theo luật; hash present.

Meta-Invariants
- M1 No soft path: không retry, không warn-only.
- M2 Auditability: mỗi snapshot đủ bằng chứng cho tranh chấp (hash + reason).

Execution Notes (không code)
- Transport: POST /chat (bridge, SIM=1 để tránh AX side effect).
- Assertions: cấu trúc snapshot, hash equality/inequality, reason enums.
- Freeze points: Entry (lexicon), Post-Chính (decision freeze), Post-Lập (locked_state, hash final).
