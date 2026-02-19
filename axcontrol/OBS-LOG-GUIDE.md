# =============================================================================
# PROJECT: CANON-TO-SYSTEM DETERMINISTIC PROJECTION
# METHOD: D&R PROTOCOL (CLOSED)
#
# ORIGINATOR / CREATOR:
#   alpha_prime_omega
#
# STATUS:
#   OBS LOG GUIDE — V1
# =============================================================================

# MỤC ĐÍCH
- Đọc/giải thích log NDJSON từ observe_session (read-only).
- Không suy diễn, không hành động, không network.

# TRƯỜNG CHÍNH
- type: input | ax | human_state | system | llm
- ts: timestamp
- sub: key | mouse | copy | paste | start | end
- app, role, label: AX metadata
- hex: 6-bit từ state_projector (để tra SINH/TRI/TU/DIET)
- state: H0/H1/H2 (dựa trên mật độ event)
- model: ID model nếu ghi nhận LLM start/end

# CÁCH DÙNG TÓM TẮT NHANH
```
python3 tools/summarize_logs.py logs/observe_test.ndjson
```

# PROMPT KHUNG CHO LLM (LOCAL, NO ACTION)
“Bạn là trợ lý phân tích log. Dữ liệu NDJSON có trường type/ts/app/role/hex/state. 
Hãy:
- tóm tắt phân bố app/role/hex,
- nhận diện chuyển focus chính,
- thống kê thời gian H0/H1/H2.
Không đề xuất hành động. Không sinh lệnh.”
