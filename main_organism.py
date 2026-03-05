"""
AUTONOMOUS ORGANISM SYSTEM - Master Orchestrator

Supervises all subsystems, coordinates communication,
triggers self-healing, and manages the full lifecycle
of the autonomous organism.
"""

import asyncio
import json
import logging
import os
import signal
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths & logging
# ---------------------------------------------------------------------------

BASE_DIR = Path(__file__).parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

STATE_FILE = DATA_DIR / "organism_state.json"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_DIR / "organism.log"),
    ],
)
logger = logging.getLogger("ORGANISM")


# ---------------------------------------------------------------------------
# Subsystem registry
# ---------------------------------------------------------------------------

class SubsystemStatus:
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    FAILED = "failed"
    UNKNOWN = "unknown"


class Subsystem:
    """Lightweight descriptor for a tracked subsystem."""

    def __init__(self, name: str, module_path: str | None = None):
        self.name = name
        self.module_path = module_path
        self.status = SubsystemStatus.UNKNOWN
        self.last_heartbeat: float = 0.0
        self.error_count: int = 0
        self.restart_count: int = 0
        self.metrics: dict = {}

    def record_heartbeat(self) -> None:
        self.last_heartbeat = time.time()
        self.status = SubsystemStatus.HEALTHY
        self.error_count = 0

    def record_error(self, reason: str = "") -> None:
        self.error_count += 1
        self.status = SubsystemStatus.FAILED if self.error_count >= 3 else SubsystemStatus.DEGRADED
        logger.warning("Subsystem %s error #%d: %s", self.name, self.error_count, reason)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "status": self.status,
            "last_heartbeat": self.last_heartbeat,
            "error_count": self.error_count,
            "restart_count": self.restart_count,
            "metrics": self.metrics,
        }


# ---------------------------------------------------------------------------
# Self-Healing engine (inline minimal version)
# ---------------------------------------------------------------------------

class SelfHealingEngine:
    """Detects failures and triggers recovery procedures."""

    HEARTBEAT_TIMEOUT = 120  # seconds

    def __init__(self, organism: "MasterOrchestrator"):
        self.organism = organism
        self.logger = logging.getLogger("SELF_HEALER")

    async def assess(self) -> list[str]:
        """Return names of subsystems that need healing."""
        now = time.time()
        ill = []
        for name, sub in self.organism.subsystems.items():
            if sub.status == SubsystemStatus.FAILED:
                ill.append(name)
            elif not sub.last_heartbeat or (now - sub.last_heartbeat) > self.HEARTBEAT_TIMEOUT:
                sub.status = SubsystemStatus.DEGRADED
                ill.append(name)
        return ill

    async def heal(self, subsystem_name: str) -> bool:
        """Attempt to restore a failing subsystem."""
        sub = self.organism.subsystems.get(subsystem_name)
        if not sub:
            return False
        self.logger.info("🔧 Healing subsystem: %s (restart #%d)", subsystem_name, sub.restart_count + 1)
        try:
            await asyncio.sleep(0.1)  # simulate restart delay
            sub.restart_count += 1
            sub.error_count = 0
            sub.status = SubsystemStatus.HEALTHY
            sub.last_heartbeat = time.time()
            self.logger.info("✅ Subsystem %s restored.", subsystem_name)
            return True
        except Exception as exc:
            self.logger.error("❌ Failed to heal %s: %s", subsystem_name, exc)
            return False

    async def run_healing_cycle(self) -> dict:
        """One full assessment + heal cycle."""
        ill = await self.assess()
        results = {}
        for name in ill:
            results[name] = await self.heal(name)
        return results


# ---------------------------------------------------------------------------
# Intelligence Hub stub (delegates to hyperai_phoenix when available)
# ---------------------------------------------------------------------------

class IntelligenceHub:
    """Wraps the HyperAI Phoenix intelligence layer."""

    def __init__(self):
        self.logger = logging.getLogger("INTELLIGENCE_HUB")
        self._patterns: list[dict] = []
        self._learning_cycles: int = 0

    def ingest_metrics(self, metrics: dict) -> None:
        """Feed new metrics into the learning loop."""
        self._patterns.append({"ts": time.time(), **metrics})
        # Keep rolling window
        if len(self._patterns) > 1000:
            self._patterns = self._patterns[-500:]

    def run_learning_cycle(self) -> dict:
        """Analyse patterns and return optimisation recommendations."""
        self._learning_cycles += 1
        healthy = sum(1 for p in self._patterns if p.get("overall_status") == SubsystemStatus.HEALTHY)
        total = max(len(self._patterns), 1)
        health_ratio = healthy / total
        recommendations = []
        if health_ratio < 0.8:
            recommendations.append("Increase self-healing frequency")
        if self._learning_cycles % 10 == 0:
            recommendations.append("Evolution cycle due – trigger optimization workflow")
        return {
            "cycle": self._learning_cycles,
            "health_ratio": round(health_ratio, 3),
            "pattern_count": len(self._patterns),
            "recommendations": recommendations,
        }


# ---------------------------------------------------------------------------
# Monitoring & analytics
# ---------------------------------------------------------------------------

class MonitoringHub:
    """Collects and exposes real-time metrics."""

    def __init__(self):
        self.logger = logging.getLogger("MONITORING")
        self._snapshots: list[dict] = []

    def capture(self, subsystems: dict[str, Subsystem]) -> dict:
        snapshot = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "overall_status": self._overall(subsystems),
            "subsystems": {n: s.to_dict() for n, s in subsystems.items()},
        }
        self._snapshots.append(snapshot)
        if len(self._snapshots) > 200:
            self._snapshots = self._snapshots[-100:]
        return snapshot

    @staticmethod
    def _overall(subsystems: dict[str, Subsystem]) -> str:
        statuses = [s.status for s in subsystems.values()]
        if all(st == SubsystemStatus.HEALTHY for st in statuses):
            return SubsystemStatus.HEALTHY
        if any(st == SubsystemStatus.FAILED for st in statuses):
            return SubsystemStatus.FAILED
        return SubsystemStatus.DEGRADED

    def latest_report(self) -> dict:
        return self._snapshots[-1] if self._snapshots else {}

    def write_dashboard(self, path: Path) -> None:
        report = self.latest_report()
        try:
            path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        except OSError as exc:
            self.logger.warning("Could not write dashboard: %s", exc)


# ---------------------------------------------------------------------------
# Master Orchestrator
# ---------------------------------------------------------------------------

class MasterOrchestrator:
    """
    The central brain of the Autonomous Organism System.

    Responsibilities:
    - Supervise all subsystems via heartbeat monitoring
    - Coordinate inter-subsystem communication
    - Trigger self-healing when failures detected
    - Manage the organism lifecycle (start / run / stop)
    - Persist state across restarts
    """

    VERSION = "1.0.0"
    CYCLE_INTERVAL = 30  # seconds between main loop iterations

    def __init__(self):
        self.logger = logging.getLogger("MASTER_ORCHESTRATOR")
        self.running = False

        # Registered subsystems
        self.subsystems: dict[str, Subsystem] = {
            "HyperAI_Phoenix": Subsystem("HyperAI_Phoenix", "hyperai_phoenix"),
            "AXCONTROL": Subsystem("AXCONTROL", "axcontrol"),
            "Factory": Subsystem("Factory", "factory"),
            "AutonomousOperator": Subsystem("AutonomousOperator", "autonomous_operator"),
        }

        # Component engines
        self.healer = SelfHealingEngine(self)
        self.intelligence = IntelligenceHub()
        self.monitoring = MonitoringHub()

        # Communication bus (simple in-process event queue)
        self._event_queue: asyncio.Queue = asyncio.Queue()

        # Load previous state if available
        self._load_state()

    # ------------------------------------------------------------------
    # State persistence
    # ------------------------------------------------------------------

    def _load_state(self) -> None:
        if STATE_FILE.exists():
            try:
                data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
                for name, info in data.get("subsystems", {}).items():
                    if name in self.subsystems:
                        sub = self.subsystems[name]
                        sub.restart_count = info.get("restart_count", 0)
                self.logger.info("📂 State restored from %s", STATE_FILE)
            except Exception as exc:
                self.logger.warning("Could not load state: %s", exc)

    def _save_state(self) -> None:
        data = {
            "version": self.VERSION,
            "saved_at": datetime.now(timezone.utc).isoformat(),
            "subsystems": {n: s.to_dict() for n, s in self.subsystems.items()},
        }
        try:
            STATE_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
        except OSError as exc:
            self.logger.warning("Could not save state: %s", exc)

    # ------------------------------------------------------------------
    # Inter-subsystem communication bus
    # ------------------------------------------------------------------

    async def publish(self, event_type: str, payload: dict) -> None:
        await self._event_queue.put({"type": event_type, "payload": payload, "ts": time.time()})

    async def _drain_events(self) -> None:
        while not self._event_queue.empty():
            event = await self._event_queue.get()
            self.logger.debug("📨 Event: %s → %s", event["type"], event["payload"])

    # ------------------------------------------------------------------
    # Health-check probes
    # ------------------------------------------------------------------

    def _probe_subsystem(self, sub: Subsystem) -> bool:
        """
        Perform a lightweight health probe for a subsystem.
        In production this would call HTTP health endpoints or
        check process status; here we inspect the module path.
        """
        if sub.module_path:
            path = BASE_DIR / sub.module_path
            if path.exists():
                sub.record_heartbeat()
                return True
        # Subsystem directory/module not found
        sub.record_error("module path not found")
        return False

    async def _health_check_cycle(self) -> dict:
        results = {}
        for name, sub in self.subsystems.items():
            ok = self._probe_subsystem(sub)
            results[name] = ok
        return results

    # ------------------------------------------------------------------
    # Main lifecycle
    # ------------------------------------------------------------------

    async def start(self) -> None:
        self.logger.info("🧬 AUTONOMOUS ORGANISM v%s STARTING", self.VERSION)
        self.running = True

        # Announce startup to all subsystems
        await self.publish("ORGANISM_START", {"version": self.VERSION})

        # Register OS signals for graceful shutdown
        loop = asyncio.get_event_loop()
        for sig in (signal.SIGTERM, signal.SIGINT):
            try:
                loop.add_signal_handler(sig, self._request_shutdown)
            except (NotImplementedError, RuntimeError):
                # Windows / restricted environments
                pass

        await self._run_loop()

    def _request_shutdown(self) -> None:
        self.logger.info("🛑 Shutdown signal received.")
        self.running = False

    async def _run_loop(self) -> None:
        cycle = 0
        try:
            while self.running:
                cycle += 1
                self.logger.info("🔄 Organism cycle #%d", cycle)

                # 1. Health checks
                health = await self._health_check_cycle()

                # 2. Monitoring snapshot
                snapshot = self.monitoring.capture(self.subsystems)
                self.monitoring.write_dashboard(DATA_DIR / "dashboard.json")

                # 3. Feed intelligence
                self.intelligence.ingest_metrics(snapshot)
                if cycle % 5 == 0:
                    insights = self.intelligence.run_learning_cycle()
                    self.logger.info("🧠 Intelligence insights: %s", insights)
                    await self.publish("INTELLIGENCE_INSIGHTS", insights)

                # 4. Self-healing
                healing_results = await self.healer.run_healing_cycle()
                if healing_results:
                    self.logger.info("🔧 Healing results: %s", healing_results)
                    await self.publish("HEALING_COMPLETED", healing_results)

                # 5. Drain event bus
                await self._drain_events()

                # 6. Persist state
                self._save_state()

                self.logger.info(
                    "📊 Overall status: %s | Health: %s",
                    snapshot.get("overall_status"),
                    health,
                )

                await asyncio.sleep(self.CYCLE_INTERVAL)

        except asyncio.CancelledError:
            pass
        finally:
            self.logger.info("🏁 Organism shutting down. Saving state...")
            self._save_state()

    # ------------------------------------------------------------------
    # Public API for external callers / tests
    # ------------------------------------------------------------------

    def get_status(self) -> dict:
        return self.monitoring.latest_report()

    def register_subsystem(self, name: str, module_path: str | None = None) -> Subsystem:
        sub = Subsystem(name, module_path)
        self.subsystems[name] = sub
        return sub


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

async def _main() -> None:
    orchestrator = MasterOrchestrator()
    await orchestrator.start()


if __name__ == "__main__":
    asyncio.run(_main())
