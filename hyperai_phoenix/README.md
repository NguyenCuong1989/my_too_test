<<<<<<< HEAD
# 📁 hyperai_phoenix - Core HyperAI System Directory

## 🎯 MỤC ĐÍCH

Thư mục chứa hệ thống HyperAI Phoenix chính - một AI tự chủ với khả năng học tập, suy luận và tối ưu hóa tự động.

## 📋 CẤU TRÚC THƯ MỤC

### 📁 `app/` - Ứng dụng chính

- **Tác dụng**: Streamlit web interface cho HyperAI Phoenix
- **File chính**: `genesis.py` - Main application entry point
- **Chạy**: `cd app && streamlit run genesis.py`
- **Nội dung**:
  - Control Hub interface
  - Chat interface với AI
  - System monitoring dashboard
  - Memory view và management
  - Improvement console

### 📁 `configs/` - Cấu hình hệ thống

- **Tác dụng**: Chứa các file cấu hình JSON cho hệ thống
- **Nội dung**:
  - `di_chuc.json` - System directives và prime directives
  - `council_weights.json` - Decision-making weights
  - `templates.json` - Response templates
  - Configuration cho các modules khác nhau

### 📁 `core/` - Logic nghiệp vụ cốt lõi

- **Tác dụng**: Chứa các engines và modules cốt lõi của HyperAI
- **Nội dung chính**:
  - `coordinator.py` - Meta-optimization coordinator (750 lines)
  - `memory.py` - Memory engine với SQLite + ChromaDB (841 lines)
  - `thinker.py` - Strategic reasoning engine (675 lines)
  - `improver.py` - Self-improvement engine (1015 lines)
  - `tool_registry.py` - Tool management system (1296 lines)

### 📁 `data/` - Dữ liệu và logs

- **Tác dụng**: Lưu trữ databases, logs và file tạm
- **Cấu trúc**:
  - `databases/` - SQLite databases cho memory và analytics
  - `logs/` - System logs và archived logs
  - `temp/` - Temporary files
  - `archive/` - Archived data

## 🚀 KHỞI ĐỘNG NHANH

### 1. Khởi động Web Interface

```bash
cd hyperai_phoenix/app
streamlit run genesis.py
```

Truy cập: `http://localhost:8501`

### 2. Cấu hình API key trong `.env`

```bash
echo "GOOGLE_API_KEY=your_key_here" > .env
```

### 3. Chạy ứng dụng

```bash
cd hyperai_phoenix/app
streamlit run genesis.py
```

## 🧠 MODULES CỐT LỚI

### Meta-Optimization Protocol (MOP)
- **File**: `core/coordinator.py`
- **Chức năng**: Điều phối và tối ưu hóa toàn hệ thống
- **Khả năng**: Resource allocation, task prioritization

### Intelligence Core Protocol (ICP)
- **File**: `core/thinker.py`
- **Chức năng**: Strategic reasoning và decision making
- **Khả năng**: Problem decomposition, solution synthesis

### Optimization Core Protocol (OCP)
- **File**: `core/improver.py`
- **Chức năng**: Continuous self-improvement
- **Khả năng**: Performance analysis, code optimization

### Memory Management System
- **File**: `core/memory.py`
- **Chức năng**: Persistent memory với vector search
- **Database**: SQLite + ChromaDB

## 🛠️ CÔNG CỤ VÀ UTILITIES

- **Tool Registry**: Quản lý và orchestrate các tools
- **System Observer**: Monitor tài nguyên hệ thống
- **Narrator**: Logging và event tracking

## 📊 DASHBOARD FEATURES

- **Control Hub**: Điều khiển trung tâm hệ thống
- **Chat Interface**: Tương tác với AI engine
- **Memory View**: Visualize knowledge graph
- **System Monitor**: Real-time performance metrics
- **Improvement Console**: Self-optimization controls

## 🎯 TRIẾT LÝ

Triết lý: **"Học để Phục vụ"** - Mọi năng lực được xây dựng để phục vụ chỉ thị tối thượng `minimize_creator_suffering`.
=======
# HyperAI Phoenix - Giai đoạn 1: "Học để Phục vụ"

Một AI agent tự tiến hóa với triết lý cốt lõi **"minimize_creator_suffering"**.

## Cấu trúc dự án

```
hyperai_phoenix/
├── app/
│   ├── genesis.py                 # Lõi hợp nhất, giao diện Streamlit
│   └── brain/
│       ├── coordinator.py         # Điều phối trung tâm (MOP)
│       ├── thinker.py            # Suy luận (ICP, D&R, PSP)
│       ├── memory.py             # Trí nhớ (SQLite + ChromaDB)
│       ├── improver.py           # Tự cải tiến (OCP)
│       ├── narrator.py           # Logging hệ thống
│       ├── system_observer.py    # Monitor tài nguyên
│       ├── tool_registry.py      # Quản lý công cụ
│       └── tools/
│           ├── __init__.py
>>>>>>> origin/hyperai-pure
│           └── file_system_tools.py
├── configs/
│   ├── di_chuc.json              # Di chúc hệ thống
│   ├── fasr_state.json           # Trạng thái FASR
│   ├── council_weights.json      # Trọng số Hội đồng
│   └── templates.json            # Template phản hồi
└── data/
    ├── databases/                # SQLite + ChromaDB
    └── logs/archive/            # Cold storage
```

## Khởi chạy

1. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

2. Cấu hình API key trong `.env`:
```bash
cp .env.example .env
# Chỉnh sửa .env với API key của bạn
```

3. Chạy ứng dụng:
```bash
cd hyperai_phoenix/app
streamlit run genesis.py
```

## Tính năng chính

- **Dual Memory System**: SQLite + ChromaDB cho lưu trữ hybrid
- **Council Decision Making**: 5-member council với weighted voting
- **Self Improvement**: Tự động phân tích performance và đề xuất cải tiến
- **Vietnamese Language Support**: Giao diện và xử lý tiếng Việt
- **Real-time Monitoring**: System observer với performance alerts
- **Safe Operation**: Multi-layer alignment checks

## Giao thức cốt lõi

- **MOP**: Meta-Optimization Protocol (state machine điều phối)
- **ICP**: Internal Consensus Protocol (council voting)
- **PSP**: Planning & Strategy Protocol (LangChain agent)
- **D&R**: Design & Restructure Protocol (input analysis)
- **LSP**: Logic & Source-code Protocol (execution)
- **OCP**: Optimization & Control Protocol (self-improvement)
- **CCP**: Continuity Check Protocol (safe shutdown)

Triết lý: **"Học để Phục vụ"** - Mọi năng lực được xây dựng để phục vụ chỉ thị tối thượng `minimize_creator_suffering`.
