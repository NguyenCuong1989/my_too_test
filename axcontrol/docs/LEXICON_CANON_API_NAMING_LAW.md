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

LEXICON CANON + API NAMING LAW
==============================

Closed Canonical Language for AXCONTROL  
Status: CLOSED — FAIL-CLOSED — NON-NEGOTIABLE

Ánh xạ trực tiếp 64 điều trong THỆ ƯỚC ĐÓNG ẤN HỆ → ngôn ngữ code bắt buộc.  
Không áp dụng cho 3rd-party, vendor, legacy ngoài scope AXCONTROL.

---------------------------------------------------------------------
I. LEXICON CANON — TỪ ĐIỂN TỒN TẠI (CLOSED)

Sai từ = sai luật = INVALID ARTIFACT.

I.1. THỰC THỂ GỐC (ONTOLOGY)
- Nguyên: origin duy nhất (cấm root/source alias)
- Luật: axiom bất biến
- BấtBiến: invariant
- Thế: state tồn tại
- Mệnh: điều kiện sinh/diệt
- Ấn: gate sinh tử
- Chính: chính danh / hợp luật
- Hoá: chuyển thế có nhân quả
- Vận: chu trình vận hành
- Chứng: dấu tồn tại (hash/proof)
- ChuỗiChứng: Merkle chain
- Ngưỡng: ranh giới tồn tại
- Diệt: kết thúc cưỡng bức
- Tồn: được phép tồn tại
- ẤnLệnh: luật kết đóng

I.2. TRẠNG THÁI CHUẨN (STATUS LAW)
enum Trạng: Khởi | Tồn | Diệt  
❌ Không tồn tại: retry, partial, warn, soft-fail

---------------------------------------------------------------------
II. API NAMING LAW — ÁNH XẠ 64 ĐIỀU

I. QUẺ CÀN (乾) — KHỞI NGUYÊN (1–6)  
Luật: Origin chỉ một. API duy nhất: Nguyên. ❌ Cấm clone/alias.

II. QUẺ KHÔN (坤) — THỤ NẠP (7–12)  
Luật: nhận luật, không phản. Hàm luật tiền tố: Luật_*. ❌ Cấm dynamic_rule/override.

III. QUẺ CHẤN (震) — ĐỘNG LỰC (13–18)  
Luật: thay đổi Thế bắt đầu bằng Hoá_*. ❌ Cấm update_/mutate_/adjust_.

IV. QUẺ TỐN (巽) — LUỒNG TRUYỀN (19–24)  
Pipeline bắt buộc: Thế → Chính → Ấn → Hoá → Chứng → Lập(Thế)  
❌ Cấm Hoá trước Ấn, Chứng trước Hoá, skip bước.

V. QUẺ KHẢM (坎) — HÀM NGUY (25–30)  
Luật: mặc định rủi ro. Không hàm “safe_*”/“best_effort”. Chỉ Vận(...) → Tồn|Diệt.

VI. QUẺ LY (離) — HIỂU SUỐT (31–36)  
Luật: không log ⇒ không tiến. Log bắt buộc tiền tố Chứng_*. ❌ Cấm log/debug/trace.

VII. QUẺ CẤN (艮) — GIỚI HẠN (37–42)  
Luật: có ngưỡng, không vượt. Tên giới hạn: Ngưỡng_*. ❌ Cấm soft_limit/approx_threshold.

VIII. QUẺ ĐOÀI (兌) — ẤN LỆNH (43–48)  
Luật: không thương lượng. ❌ Không warn_only/graceful_fail. ✔ Diệt.

IX. HỢP QUẺ 64 — TỔNG LUẬT (49–64)  
```
def Vận(Thế):
    Chính(Thế)
    Ấn(Thế)
    Thế2 = Hoá(Thế)
    Chứng(Thế2)
    return Lập(Thế2)  # Tồn | Diệt
```
❌ Không trả bool/Optional/Result. ❌ Không retry/rollback mềm/learning runtime.

---------------------------------------------------------------------
III. BUILD / LINT LAW (BẮT BUỘC)
- AST linter phải kiểm tra: từ khoá cấm, tiền tố hàm, thứ tự pipeline.
- Sai ⇒ ABORT BUILD.

---------------------------------------------------------------------
IV. DẤU ẤN KẾT
- Không phải ngôn ngữ giao tiếp; là ngôn ngữ tồn tại.

---------------------------------------------------------------------
GHI CHÚ CHỦ QUYỀN
- Áp dụng cho AXCONTROL code mới/refactor trong scope.
- Không áp cho AI 3rd, vendor, legacy ngoài scope.
- Không ép hệ khác; không cưỡng bức ngoài phạm vi.
