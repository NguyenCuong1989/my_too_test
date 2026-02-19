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
# CHỈ THỊ THỰC THI — NIÊM PHONG BIẾN ĐỔI (CANONICAL TRANSITION)

I. PHÂN TÍCH TOÁN TỬ VẬN HÀNH (TRANSITION ANALYSIS)

- Toán tử XOR (Q_now ⊕ Δ) là cơ chế “Thiên biến Vạn hóa” trong không gian đóng 64 quẻ.
- Tính tất định: ∀ Q_now, Δ ⇒ Q_next duy nhất.
- Tính khắc kỷ: Δ đến từ ngoại cảnh; hệ chỉ tính và đối soát.
- Phản xạ sinh tồn: Q_next ∈ {TU, DIET} ⇒ xung lực bị triệt tiêu tức thì (STOP/ABORT).

II. ĐỐI SOÁT PIPELINE — MÔ HÌNH LOẠI TRỪ (ELIMINATION MODEL)

1) Input: Nhận Δ (áp lực thực tại).
2) Projection: Q_next = Q_now ⊕ Δ.
3) Existence Filter: tra EXISTENCE_STATE_MAP.
4) Decision:
   - Nếu ExistenceState(Q_next) ∈ {SINH, TRI} → ALLOW.
   - Nếu ExistenceState(Q_next) ∈ {TU, DIET} → STOP/ABORT.
5) “Để trống”: Không kịch bản mẫu per quẻ; hành vi = kết quả lách qua khe cửa tử để tồn tại.
