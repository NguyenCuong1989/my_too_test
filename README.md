# my_too_test

An autonomous AI ecosystem orchestrating multiple intelligent sub-systems for self-improving task execution, UI control, and distributed operations.

## 🌐 Project Mission

Build a modular, autonomous AI platform that minimizes friction and maximizes value through self-learning agents, deterministic UI automation, and robust orchestration infrastructure.

## 🏗️ Architecture Overview

```
my_too_test/
├── hyperai_phoenix/        # Core autonomous AI agent (HyperAI Phoenix)
├── axcontrol/              # Deterministic macOS UI control system
├── DAIOF-Framework/        # Distributed AI Orchestration Framework
├── autonomous_operator/    # Distributed cluster & operator bridge
├── balancehub/             # Load balancing & resource hub
├── src/                    # Shared source utilities
├── tests/                  # Test suite
├── Dockerfile              # Container image definition
├── docker-compose.yml      # Multi-service orchestration
└── compose.yaml            # Production compose config
```

## 📦 Modules

### 🔥 HyperAI Phoenix (`hyperai_phoenix/`)
Self-evolving AI agent with core philosophy **"minimize_creator_suffering"**.

- **Streamlit web interface** for control, chat, memory, and monitoring
- **Dual Memory System**: SQLite + ChromaDB hybrid storage
- **Council Decision Making**: 5-member council with weighted voting
- **Self-Improvement Engine**: Automatic performance analysis and optimization
- **Core Protocols**: MOP, ICP, PSP, D&R, LSP, OCP, CCP

See [`hyperai_phoenix/README.md`](hyperai_phoenix/README.md) for details.

### 🖥️ AXCONTROL (`axcontrol/`)
Deterministic macOS UI control system — sealed, auditable, human-in-the-loop.

- AI provides **intent proposals only**; execution is policy-gated and signed
- Append-only audit logs with full replay capability
- Finite command set with allow/deny policy guards
- macOS AX/CGEvent bridge + mobile control plane (iOS/Web)

See [`axcontrol/README.md`](axcontrol/README.md) for details.

### ⚙️ DAIOF-Framework (`DAIOF-Framework/`)
Distributed AI Orchestration Framework — the backbone for multi-agent task scheduling and execution.

### 🤖 Autonomous Operator (`autonomous_operator/`)
Distributed cluster workers and orchestration bridge.

- `orchestrator_v3.py` — multi-node task orchestration
- `titan_worker.py` — distributed worker nodes
- `neural_link.py` — inter-agent communication
- `eternal_monitor.py` — continuous system health monitoring

### ⚖️ BalanceHub (`balancehub/`)
Resource balancing and load distribution across the cluster.

## 🚀 Quick Start

### Docker (Recommended)

```bash
# Clone the repository (including submodules)
git clone --recurse-submodules https://github.com/NguyenCuong1989/my_too_test.git
cd my_too_test

# Configure environment
cp .env.example .env
# Edit .env with your API keys

# Start all services
docker-compose up --build
```

### Local Development

```bash
# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r DAIOF-Framework/requirements.txt

# Run the main entry point
python3 src/main.py
```

### HyperAI Phoenix (Streamlit UI)

```bash
cd hyperai_phoenix/app
streamlit run genesis.py
# Open http://localhost:8501
```

### AXCONTROL (macOS)

```bash
cd axcontrol
# Health check
python3 -m compileall core && python3 tools/verify_canon_properties.py
# Run CI
make ci
```

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| AI / LLM | Google Gemini, Ollama (local, `qwen3:8b`) |
| Web UI | Streamlit |
| Memory | SQLite, ChromaDB |
| Orchestration | Docker, docker-compose |
| macOS Automation | AX API, CGEvent |
| Mobile Control | iOS / Web client |
| Package Management | pip, venv |

## 🧪 Testing

```bash
# Run the test suite
python3 -m pytest tests/
```

## 🤝 Contributing

1. Fork the repository and create a feature branch from `main`.
2. Follow existing code style and add tests for new behaviour.
3. Ensure all tests pass and linting is clean before opening a pull request.
4. Open a pull request with a clear description of changes.

## 📄 License

Licensing for this project is currently under review and will be documented in a future update. Until a formal license is added, all rights are reserved.
