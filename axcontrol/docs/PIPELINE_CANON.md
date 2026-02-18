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
# PIPELINE CANON (BẮT BUỘC)

Thế → Chính → Ấn → Hoá → Chứng → Lập | Diệt

Invariants:
- Không bypass bất kỳ bước nào.
- Không Hoá trước Ấn, không Chứng trước Hoá.
- Không async escape; mỗi vòng kết thúc ở Tồn (Lập) hoặc Diệt.
- Không retry, fallback, soft-fail.

Entry points (CLI / HTTP / UI bridge) MUST start at Vận and end at Tồn|Diệt.
