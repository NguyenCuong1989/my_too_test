# =============================================================================
# PROJECT: CANON-TO-SYSTEM DETERMINISTIC PROJECTION
# METHOD: D&R PROTOCOL (CLOSED)
#
# ORIGINATOR / CREATOR:
#   alpha_prime_omega
#
# STATUS:
#   OBSERVATION GAP REPORT — V1
# =============================================================================

# PIPELINE ĐANG CÓ (OK)
- AX snapshot (observer) hoạt động thực địa.
- State projector → hex_bits (6-bit) và existence filter (STOP TU/DIET).
- Drift / causality lock, lexicon closed, ontology guard (mandatory bits).
- Audit hash (Chung) + hex_bits trong AuditRecord.
- Property check R-34: 0/4096 violation.
- Health check script: compileall + property check.

# PIPELINE THIẾU / NOT OK (ĐỂ QUAN SÁT)
- Chưa có logger thụ động (input/focus/copy/paste) → chưa phân loại H0/H1/H2.
- Bridge/UI chưa xuất hex_bits ra snapshot; UI chưa hiển thị stop=ontological_violation.
- Projector: h6 (stability) = 1 cố định; chưa đo biến động thực.
- Không log LLM interaction (start/end, model) trong observation mode.
- No CI workflow tối giản (compileall + property check) khai báo; CI_KNOWN_ISSUES có nhưng chưa có workflow file.
- UI client chưa đồng bộ field mới (hex_bits, ontological stops).

# ĐỀ MỤC TIẾP CẬN (CHỈ ĐỂ THEO DÕI, CHƯA THỰC THI)
- Implement tools/observe_session.py (passive logger) theo OBS-SCHEMA.
- Expose hex_bits in bridge snapshot; minimal UI render.
- (Nếu cần) add stability metric to projector h6.
- Add CI workflow minimal (compileall + verify_canon_properties) if CI re-enabled.
