╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                                           ║
║                        🔴 APΩ RUNTIME KERNEL - CORE CONTAINER DESIGN                                                                   ║
║                             Unified AI-OS Operating System Kernel                                                                      ║
║                                         2026-03-05 | CRITICAL                                                                          ║
║                                                                                                                                           ║
╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
1. WHY APΩ RUNTIME KERNEL IS CRITICAL
═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

CURRENT STATE:
├─ telegram_bot.py (standalone)
├─ factory_worker.py (standalone)
├─ command_router.py (utility)
├─ No unified orchestration
└─ Services have no communication protocol

PROBLEM:
├─ telegram_bot runs independently
├─ factory_worker runs independently
├─ AntigravityLoopController is in telegram_bot (coupled)
├─ No single control point
└─ Can't coordinate state transitions

SOLUTION: APΩ RUNTIME KERNEL
├─ Single unified container image
├─ Core orchestration engine
├─ Multi-process supervisor (telegram + factory)
├─ State machine management
├─ Inter-process communication
└─ Central logging & monitoring

BENEFIT:
├─ Single entrypoint
├─ Coordinated lifecycle
├─ Atomic state transitions
├─ Easy to scale/replicate
├─ Production-grade orchestration

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
2. APΩ RUNTIME KERNEL ARCHITECTURE
═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                         APΩ RUNTIME KERNEL CONTAINER                                                           │
│                         (apo-runtime-kernel:latest)                                                            │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                                 │
│  ┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐  │
│  │                    KERNEL SUPERVISOR (supervisord/systemd)                                               │  │
│  │                                                                                                          │  │
│  │  Process Management:                                                                                     │  │
│  │  ├─ telegram-bot process (Python)                                                                      │  │
│  │  ├─ factory-worker process (Python)                                                                    │  │
│  │  └─ health-checker process (Python)                                                                    │  │
│  │                                                                                                          │  │
│  │  Communication Bus (IPC):                                                                               │  │
│  │  ├─ Redis (localhost:6379)                                                                             │  │
│  │  └─ Shared memory (for state)                                                                          │  │
│  │                                                                                                          │  │
│  │  Orchestration:                                                                                         │  │
│  │  ├─ Process restart on failure                                                                         │  │
│  │  ├─ Health check monitoring                                                                            │  │
│  │  ├─ State synchronization                                                                              │  │
│  │  └─ Graceful shutdown                                                                                  │  │
│  │                                                                                                          │  │
│  └──────────────────────────────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                                                 │
│  ┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐  │
│  │                    KERNEL RUNTIME MANAGER                                                               │  │
│  │                                                                                                          │  │
│  │  Responsibilities:                                                                                       │  │
│  │  ├─ Initialize container                                                                               │  │
│  │  ├─ Start supervisor                                                                                   │  │
│  │  ├─ Monitor process health                                                                             │  │
│  │  ├─ Handle signals (SIGTERM, SIGKILL)                                                                 │  │
│  │  ├─ Manage state lifecycle                                                                             │  │
│  │  ├─ Collect metrics                                                                                    │  │
│  │  └─ Emit logs                                                                                          │  │
│  │                                                                                                          │  │
│  │  State Interface:                                                                                       │  │
│  │  ├─ GET /kernel/status → {"state": "RUNNING", ...}                                                    │  │
│  │  ├─ POST /kernel/state → {"goal": "...", "transition": "PLANNING"}                                     │  │
│  │  ├─ GET /kernel/logs → [...]                                                                          │  │
│  │  └─ GET /kernel/metrics → {...}                                                                        │  │
│  │                                                                                                          │  │
│  └──────────────────────────────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                                                 │
│  ┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐  │
│  │                    TELEMETRY & LOGGING AGGREGATOR                                                       │  │
│  │                                                                                                          │  │
│  │  Log Aggregation:                                                                                        │  │
│  │  ├─ Collect from all processes                                                                         │  │
│  │  ├─ Parse & structure logs                                                                             │  │
│  │  ├─ Stream to file (/logs/orchestrator.log)                                                            │  │
│  │  └─ Expose to Prometheus                                                                               │  │
│  │                                                                                                          │  │
│  │  Metrics Collection:                                                                                    │  │
│  │  ├─ CPU/Memory per process                                                                             │  │
│  │  ├─ Task execution metrics                                                                             │  │
│  │  ├─ State transition timing                                                                            │  │
│  │  └─ Error rates                                                                                        │  │
│  │                                                                                                          │  │
│  └──────────────────────────────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                                                 │
│  /app/ Directory Structure:                                                                                    │
│  ├─ apo_runtime_kernel.py .................. Main kernel entrypoint                                          │
│  ├─ kernel/                                                                                                   │
│  │  ├─ supervisor.py ..................... Process manager                                                 │
│  │  ├─ runtime_manager.py ................ State & lifecycle                                               │
│  │  ├─ telemetry.py ...................... Logging & metrics                                               │
│  │  ├─ ipc_bus.py ........................ Inter-process communication                                       │
│  │  └─ health_checker.py ................. Process health monitoring                                        │
│  ├─ telegram_bot.py ...................... Modified for kernel mode                                         │
│  ├─ factory_worker.py .................... Modified for kernel mode                                         │
│  ├─ command_router.py                                                                                        │
│  ├─ gemini_planner_bridge.py                                                                                │
│  ├─ task_injector.py                                                                                         │
│  ├─ tools/ .............................. Skill modules                                                      │
│  └─ requirements.txt ..................... All dependencies + supervisor                                    │
│                                                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
3. KERNEL STARTUP SEQUENCE
═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

docker run -d apo-runtime-kernel:latest

Execution Timeline:

1. Container starts (entrypoint: apo_runtime_kernel.py)
   ├─ Time: 0s
   └─ PID: 1 (apo_runtime_kernel.py)

2. Kernel Manager initializes
   ├─ Time: 0-1s
   ├─ Verify /app directory structure
   ├─ Load configuration
   ├─ Create IPC channels
   └─ Initialize state machine

3. Supervisor starts
   ├─ Time: 1-2s
   ├─ Start: telegram-bot process
   ├─ Start: factory-worker process
   ├─ Start: health-checker process
   └─ Begin process monitoring

4. Telegram Bot initializes
   ├─ Time: 2-5s
   ├─ Connect to Telegram API
   ├─ Load command router
   ├─ Initialize Gemini planner
   ├─ Set state: IDLE
   └─ Begin polling for messages

5. Factory Worker initializes
   ├─ Time: 2-5s
   ├─ Create /taskbus watchers
   ├─ Load skill modules
   ├─ Initialize state: POLLING
   └─ Begin task polling (2s interval)

6. Health Checker starts
   ├─ Time: 5-10s
   ├─ Monitor telegram-bot process
   ├─ Monitor factory-worker process
   ├─ Check task bus health
   ├─ Check log streaming
   └─ Emit metrics to Prometheus

7. Kernel Ready
   ├─ Time: 10s
   ├─ All processes healthy
   ├─ IPC channels open
   ├─ State: RUNNING
   └─ Status: READY FOR COMMANDS

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
4. KERNEL STATE MACHINE
═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

State Transitions:

┌──────────┐
│  INIT    │ (Container starting)
└────┬─────┘
     │ (all processes started)
     ▼
┌──────────────────┐
│  IDLE            │ (Waiting for commands)
│  ├─ telegram-bot: polling
│  ├─ factory-worker: polling
│  └─ health-checker: monitoring
└────┬──────────┬──────────┬──────────┐
     │          │          │          │
(goal cmd)   (direct task)  (error)  (shutdown)
     │          │          │          │
     ▼          ▼          ▼          ▼
┌──────────┐ ┌──────────┐ ┌────────┐ ┌──────────────┐
│ PLANNING │ │EXECUTING │ │ ERROR  │ │ SHUTTING_DOWN│
│ (Φ⁻¹)    │ │(tasks)   │ │(alert) │ │ (graceful)   │
└────┬─────┘ └────┬─────┘ └───┬────┘ └──────────────┘
     │            │           │         (cleanup)
(plan ready)  (drift check) (recover)    │
     │            │           │         ▼
     ▼            ▼           ▼      ┌──────────┐
  ┌──────────────────────────────┐  │ STOPPED  │
  │ OBSERVING                     │  └──────────┘
  │ (monitor task execution)      │
  └────┬────────────┬────────────┘
       │            │
   (success)    (failure)
       │            │
       ▼            ▼
  ┌─────────┐  ┌────────────┐
  │COMPLETED│  │DRIFT_DETECT│
  └────┬────┘  └─────┬──────┘
       │             │
   (cleanup)   (analysis)
       │             │
       └──────┬──────┘
              │
          (heal plan)
              │
              ▼
         ┌────────────┐
         │ HEALING    │
         │ (retry DAG)│
         └────┬───────┘
              │
         (retry ready)
              │
              ▼
         Back to PLANNING

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
5. DOCKERFILE.KERNEL (Multi-process Container)
═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

FROM python:3.11-slim

# Install supervisor for process management
RUN apt-get update && apt-get install -y --no-install-recommends \
    supervisor \
    curl \
    build-essential \
    gcc \
    rustc \
    cargo \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy all source files
COPY factory_worker.py .
COPY telegram_bot.py .
COPY command_router.py .
COPY gemini_planner_bridge.py .
COPY task_injector.py .
COPY log_streamer.py .
COPY apo_runtime_kernel.py .
COPY kernel/ ./kernel/
COPY tools/ ./tools/
COPY requirements.txt .

# Install Python dependencies
RUN python -m pip install --no-cache-dir -r requirements.txt

# Create supervisor config
COPY supervisord.conf /etc/supervisor/conf.d/

# Create necessary directories
RUN mkdir -p /taskbus/inbox /taskbus/processed /taskbus/failed \
    && mkdir -p /logs \
    && mkdir -p /app/tools

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:8080/kernel/status || exit 1

# Expose kernel API
EXPOSE 8080

# Run kernel manager as PID 1
ENTRYPOINT ["python", "apo_runtime_kernel.py"]

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
6. KERNEL PYTHON API
═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

apo_runtime_kernel.py (Main Entrypoint):

```python
#!/usr/bin/env python3
"""
APΩ Runtime Kernel - AI-OS Operating System Core
Unified orchestration engine for all runtime processes
"""

import os
import sys
import logging
import signal
import supervisor
from flask import Flask, jsonify
from kernel.supervisor import ProcessSupervisor
from kernel.runtime_manager import RuntimeManager
from kernel.telemetry import TelemetryCollector

logger = logging.getLogger("APΩ-Kernel")

class APOKernel:
    def __init__(self):
        self.supervisor = ProcessSupervisor()
        self.runtime_mgr = RuntimeManager()
        self.telemetry = TelemetryCollector()
        self.app = Flask(__name__)
        self._setup_routes()

    def _setup_routes(self):
        """Setup Flask API endpoints"""
        
        @self.app.route('/kernel/status')
        def status():
            return jsonify({
                "state": self.runtime_mgr.current_state.name,
                "uptime": self.runtime_mgr.uptime,
                "processes": self.supervisor.get_all_processes(),
                "healthy": self.supervisor.is_healthy()
            })

        @self.app.route('/kernel/logs')
        def logs():
            return jsonify({
                "logs": self.telemetry.get_logs(limit=100)
            })

        @self.app.route('/kernel/metrics')
        def metrics():
            return jsonify(self.telemetry.get_metrics())

        @self.app.route('/kernel/state/<new_state>', methods=['POST'])
        def transition_state(new_state):
            try:
                self.runtime_mgr.transition_to(new_state)
                return jsonify({"status": "ok", "state": new_state})
            except Exception as e:
                return jsonify({"error": str(e)}), 400

    def start(self):
        """Start kernel"""
        logger.info("🔴 APΩ Runtime Kernel starting...")
        
        # Start supervisor (manages processes)
        self.supervisor.start([
            ("telegram-bot", "python telegram_bot.py"),
            ("factory-worker", "python factory_worker.py"),
            ("health-checker", "python kernel/health_checker.py")
        ])

        # Start runtime manager
        self.runtime_mgr.start()

        # Start telemetry
        self.telemetry.start()

        # Start Flask API
        logger.info("🚀 Kernel API listening on 0.0.0.0:8080")
        self.app.run(host="0.0.0.0", port=8080, threaded=True)

    def shutdown(self):
        """Graceful shutdown"""
        logger.info("⏹️  Kernel shutting down...")
        self.supervisor.stop_all()
        self.runtime_mgr.stop()
        self.telemetry.stop()

if __name__ == "__main__":
    kernel = APOKernel()
    
    # Handle signals
    signal.signal(signal.SIGTERM, lambda s, f: kernel.shutdown())
    signal.signal(signal.SIGINT, lambda s, f: kernel.shutdown())
    
    # Start kernel
    kernel.start()
```

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
7. BENEFITS OF APΩ RUNTIME KERNEL
═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

✅ SINGLE CONTAINER IMAGE
├─ One `docker run` command to start entire system
├─ No service interdependencies in docker-compose
└─ Simpler deployment

✅ UNIFIED ORCHESTRATION
├─ Single control point for state management
├─ Coordinated process lifecycle
├─ Atomic transitions between states
└─ No race conditions between services

✅ PROCESS ISOLATION (but coordinated)
├─ Each process has separate memory space
├─ Failure in one process doesn't crash others
├─ Supervisor restarts failed processes
├─ Central health monitoring

✅ EASY SCALING
├─ Run multiple kernel instances
├─ Each instance: independent execution
├─ Load balancer routes Telegram commands
├─ Task bus shared across instances

✅ BETTER OBSERVABILITY
├─ Centralized logging from all processes
├─ Single health check endpoint
├─ Unified metrics collection
├─ Easier debugging

✅ PRODUCTION-GRADE
├─ Graceful shutdown handling
├─ Signal handling (SIGTERM, SIGKILL)
├─ Process restart on failure
├─ Resource limits enforcement
└─ Container-native design

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
8. MIGRATION PATH: SEPARATE → KERNEL
═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

CURRENT (Separate processes):
├─ Terminal 1: python factory_worker.py
├─ Terminal 2: python telegram_bot.py
└─ Terminal 3: (optional) tail logs

FUTURE (Kernel-based):
├─ docker run apo-runtime-kernel:latest
└─ Single entrypoint manages everything

TRANSITION:

Step 1: Create kernel files
├─ apo_runtime_kernel.py
├─ kernel/supervisor.py
├─ kernel/runtime_manager.py
├─ kernel/telemetry.py
└─ Dockerfile.kernel

Step 2: Test locally
├─ Build: docker build -f Dockerfile.kernel -t apo-runtime-kernel .
├─ Run: docker run -v /taskbus:/taskbus -v /logs:/logs apo-runtime-kernel
└─ Test: curl http://localhost:8080/kernel/status

Step 3: Integrate with docker-compose
├─ Add apo-kernel service
├─ Remove separate aios-worker service
├─ Add depends_on: aio-kernel

Step 4: Deploy
├─ docker-compose up
└─ All services start from single container

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
9. KERNEL DEPLOYMENT CHECKLIST
═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

PRE-DEPLOYMENT:
☐ Backup current data (PostgreSQL, Redis)
☐ Create .env file with secrets
☐ Create Dockerfile.kernel
☐ Create supervisord.conf
☐ Create kernel/ directory with all modules
☐ Update requirements.txt (add supervisor)
☐ Modify telegram_bot.py for kernel mode
☐ Modify factory_worker.py for kernel mode
☐ Test build locally
☐ Create docker-compose.unified.yml

DEPLOYMENT:
☐ Build kernel image: docker build -f Dockerfile.kernel -t apo-runtime-kernel .
☐ Test image: docker run ... (verify startup)
☐ Stop current stacks: docker-compose down
☐ Start unified stack: docker-compose -f docker-compose.unified.yml up

POST-DEPLOYMENT:
☐ Verify kernel status: curl http://localhost:8080/kernel/status
☐ Check logs: curl http://localhost:8080/kernel/logs
☐ Test Telegram commands
☐ Monitor metrics
☐ Performance profiling

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
✅ NEXT STEPS FOR BRO
═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

1. ✅ Review Design Analysis (DESIGN_REVIEW_AND_VALIDATION.md) - DONE

2. ⚠️ Approve APΩ Runtime Kernel Design (this document)
   ├─ Confirm: Single kernel container approach
   ├─ Confirm: Multi-process supervisor (supervisor.io or similar)
   ├─ Confirm: Unified state management
   └─ Confirm: Centralized logging

3. ⚠️ Decide Migration Path
   ├─ When: Immediate? Or test first?
   ├─ Downtime: Can we have 1-2 hours downtime?
   ├─ Backup: Should we keep old setup as fallback?
   └─ Testing: Staging environment first?

4. ⚠️ Prepare .env file
   ├─ TELEGRAM_BOT_TOKEN=...
   ├─ GEMINI_API_KEY=...
   ├─ JWT_SECRET=...
   ├─ DB_PASSWORD=...
   └─ Other secrets

5. THEN: Create Kernel Implementation
   ├─ Create apo_runtime_kernel.py
   ├─ Create kernel/ module
   ├─ Create Dockerfile.kernel
   ├─ Create docker-compose.unified.yml
   └─ Test thoroughly

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

🚀 APΩ RUNTIME KERNEL IS THE KEY TO PRODUCTION-READY DEPLOYMENT!

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
