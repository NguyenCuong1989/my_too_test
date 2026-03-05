# Autonomous Organism System

A self-operating, self-healing, self-improving ecosystem that functions as a
unified biological entity.

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  MASTER ORCHESTRATOR                    │
│                   (main_organism.py)                    │
│  • Supervises all subsystems via heartbeat monitoring   │
│  • Coordinates inter-component communication            │
│  • Triggers self-healing on failures                    │
│  • Manages full organism lifecycle                      │
└──────────┬──────────┬──────────┬──────────┬────────────┘
           │          │          │          │
    ┌──────▼─┐  ┌─────▼──┐ ┌────▼───┐ ┌───▼──────────┐
    │HyperAI │  │AXCONTROL│ │Factory │ │ Autonomous   │
    │Phoenix │  │Decision │ │Exec    │ │ Operator     │
    │Intel.  │  │Engine   │ │Layer   │ │ Perception   │
    └────────┘  └────────┘ └────────┘ └──────────────┘
           │          │          │          │
    ┌──────▼──────────▼──────────▼──────────▼────────────┐
    │            SELF-HEALING FRAMEWORK                   │
    │  FailureDetector → RecoveryManager → StateStore     │
    └─────────────────────────────────────────────────────┘
           │
    ┌──────▼─────────────────────────────────────────────┐
    │            MONITORING & ANALYTICS                  │
    │   MetricsCollector · HealthIndicator · Dashboard   │
    └────────────────────────────────────────────────────┘
```

---

## Components

| Component | Path | Role |
|-----------|------|------|
| **Master Orchestrator** | `main_organism.py` | Central brain; lifecycle management |
| **Intelligence Hub** | `hyperai_phoenix/` | Learning, pattern recognition, optimisation |
| **Decision Engine** | `axcontrol/` | Deterministic state mgmt, policy execution |
| **Execution Layer** | `factory/` | Tool orchestration, MCP server management |
| **Perception System** | `autonomous_operator/` | Environment monitoring, anomaly detection |
| **Self-Healing** | `self_healing/` | Failure detection, auto-recovery, state store |
| **Monitoring** | `monitoring/` | Real-time metrics, health indicators, dashboard |

---

## Autonomous Capabilities

| Capability | Status |
|------------|--------|
| 🤖 Self-Aware – health monitoring & anomaly detection | ✅ |
| 🔄 Self-Healing – auto-recovery without human intervention | ✅ |
| 📈 Self-Improving – pattern learning & optimisation | ✅ |
| 🧬 Self-Evolving – daily evolution cycles | ✅ |
| 🌐 Self-Coordinating – event-driven inter-component messaging | ✅ |
| ⚡ Self-Scaling – Docker health checks & auto-restart | ✅ |
| 🛡️ Self-Protecting – audit trails & integrity checks | ✅ |
| 📊 Self-Reporting – JSON dashboards & evolution logs | ✅ |

---

## GitHub Actions Workflows

| Workflow | Schedule | Purpose |
|----------|----------|---------|
| `health_monitor.yml` | Every 5 min | Probe all subsystems |
| `self_healing.yml` | On health failure | Auto-fix detected issues |
| `performance_optimization.yml` | Hourly | Analyse & report performance |
| `evolution_cycle.yml` | Daily 02:00 UTC | Record evolution cycle |
| `full_diagnostics.yml` | Weekly Sunday 03:00 UTC | Full system diagnostics |
| `no-drift-gate.yml` | Every push / PR | Determinism invariants |

---

## Quick Start

```bash
# Clone
git clone https://github.com/NguyenCuong1989/my_too_test.git
cd my_too_test

# Run the master orchestrator (single process)
python3 main_organism.py

# Run with Docker (full stack)
docker compose up -d

# Run tests
python3 -m unittest tests.test_organism -v
cd axcontrol && AXCONTROL_SIM=1 python3 -m unittest tests.test_bridge_no_drift -v
```

---

## Self-Healing Framework

```python
from self_healing import FailureDetector, RecoveryManager, StateStore

detector = FailureDetector(failure_threshold=3)
manager  = RecoveryManager(max_attempts=5)
store    = StateStore("data/state.json")

# Record health signals
detector.record("my_service", healthy=True)

# Detect and heal
failing = detector.detect_failures()
results = await manager.heal_all(failing)

# Persist state snapshots
store.snapshot_subsystem("my_service", {"config": ...})
```

---

## Monitoring

```python
from monitoring import MetricsCollector, HealthIndicator, Dashboard

metrics   = MetricsCollector()
indicator = HealthIndicator("organism")
dashboard = Dashboard("data/")

# Record metrics
metrics.gauge("cpu_pct").record(42.3)
metrics.counter("healing_actions").increment()

# Run health checks
indicator.add_check("db", lambda: (True, "connected"))
report = indicator.run()          # {"level": "green", ...}

# Render dashboard
dashboard.render(subsystems={...}, metrics_snapshot=metrics.snapshot())
```

---

## Contributors

If you'd like to contribute, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

**Last Updated**: 2026-03-05 UTC
