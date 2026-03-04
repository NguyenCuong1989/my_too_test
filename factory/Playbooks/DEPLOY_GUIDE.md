# 🚀 DEPLOYMENT GUIDE — UNIFIED SYSTEM

Tài liệu hướng dẫn triển khai các thành phần trong hệ sinh thái DAIOF.

## 1. Firebase Portfolio (Hosting)

Đảm bảo sếp đã cài `firebase-tools` và login.

```bash
cd factory/FirebasePortfolio
firebase login
firebase deploy --only hosting
```

## 2. Go Backend (Cloud Run)

Sử dụng gcloud CLI để đẩy lên region `asia-southeast1`.

```bash
cd factory/go-template
gcloud run deploy go-factory-node \
    --source . \
    --region asia-southeast1 \
    --allow-unauthenticated
```

## 3. Web Dashboard (Standard Web)

Deploy lên Firebase Hosting hoặc Cloud Run (Containerized).

## 4. MCP Router (Nervous System)

Chạy local hoặc trong một container riêng tư để điều phối Tool.
