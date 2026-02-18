AXCONTROL — MVP OVERVIEW (R-31)
================================

Deterministic macOS UI Control System (MVP @ R-31)

AXCONTROL là gì?
- Hệ thống điều khiển UI macOS an toàn, kiểm soát.
- Mọi hành động đều ghi log, có thể kiểm tra và replay.
- AI không tự ý điều khiển; con người quyết định cuối.
- Chạy hoàn toàn local trên macOS, không phụ thuộc cloud.

Giá trị cốt lõi (tại sao khác biệt?)
- Deterministic: cùng dữ liệu đầu vào → cùng kết quả, không “đoán mò”.
- Audit & Replay: sổ cái đầy đủ; xem lại, phân tích nguyên nhân.
- Safety-first: danh mục lỗi rõ ràng và đường khôi phục; không hành động mù.
- Governance rõ ràng: thay đổi được kiểm soát, không vá nóng.
- Local-first: mất internet vẫn chạy; cloud chỉ là “gương soi”.

Người dùng & Vai trò
- Viewer: chỉ xem (logs, replay, trạng thái).
- Auditor: xem toàn bộ lịch sử, không can thiệp.
- Governor: phê duyệt thay đổi chính sách (trước khi chạy), không điều khiển runtime.
- Không có đăng nhập cloud, không điều khiển từ xa.

Cách hệ thống vận hành (tóm tắt)
1) Quan sát UI (AX của macOS).
2) Ra quyết định có kiểm soát (theo chính sách đã phê duyệt).
3) Ghi log chuẩn (sổ cái).
4) Replay/đối soát khi cần.
UI hiển thị chỉ để xem, không có nút điều khiển.

Những gì đã “khóa” trong MVP (R-31)
- Execution: không mở bề mặt thực thi mới.
- Control Plane: UI/API read-only.
- Governance: PCU/Release có quy trình phê duyệt rõ.
- Multi-User: phân quyền xem; không leo thang.
- Session: cách ly theo phiên; replay không lẫn.
- Retention: lưu trữ/archival rõ ràng.
- External Mirrors: GitHub/Asana/Notion chỉ đọc (đã kiểm chứng live).

Cloud dùng để làm gì?
- Không chạy hệ thống.
- Chỉ để soi: xem mã nguồn, lịch sử quyết định, checklist quản trị.
Mất cloud → AXCONTROL vẫn chạy bình thường.

Cách triển khai (user làm tay)
Chỉ 2 lệnh, không cấu hình phức tạp:
```
git clone https://github.com/<org>/axcontrol.git
cd axcontrol
python3 run_ax.py
```

Trạng thái MVP
- Determinism: ✔
- Audit & Replay: ✔
- Safety: ✔
- Governance: ✔
- Multi-User & Session Isolation: ✔
- SaaS drift: 0%

Khi nào mở rộng tiếp?
- Chỉ khi có nhu cầu thực tế (ví dụ: timeline trình bày cho kiểm toán).
- Hiện tại, MVP hoàn chỉnh và sẵn sàng sử dụng.

Ghi chú
- Thuần Phase 2 / vận hành, không mở thêm quyền, không thuật ngữ sâu.
- Có thể xuất bản PDF 1 trang hoặc slide 5 phút cho buổi review lãnh đạo (không kèm ở đây).
