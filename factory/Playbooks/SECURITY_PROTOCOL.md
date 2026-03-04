# 🛡️ SECURITY PROTOCOL — SOVEREIGN AXIS

Quy tắc bảo mật bắt buộc cho mọi sản phẩm ra lò từ nhà máy.

## 1. Credential Management

- **KHÔNG** bao giờ hard-code API Key hoặc Token.
- Sử dụng Environment Variables (`.env`) và đảm bảo đã có trong `.gitignore`.
- Dùng Service Account với nguyên tắc **Least Privilege** (Quyền tối thiểu).

## 2. Data Hardening

- Bật Cloud Logging Audit cho các hành động thay đổi dữ liệu (Data Write).
- Kiểm tra Firestore Rules: Chỉ cho phép ghi vào collection `leads` và chặn đọc public.

## 3. Deployment Safety

- Luôn chạy `gcloud auth list` để xác nhận đúng tài khoản trước khi deploy.
- Region định hướng: `asia-southeast1` (Singapore).
