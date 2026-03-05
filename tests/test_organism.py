"""
Tests for the Autonomous Organism System core components.

Covers:
- main_organism.MasterOrchestrator
- self_healing.FailureDetector / RecoveryManager / StateStore
- monitoring.MetricsCollector / HealthIndicator / Dashboard
"""

import asyncio
import json
import tempfile
import unittest
from pathlib import Path


# ---------------------------------------------------------------------------
# self_healing tests
# ---------------------------------------------------------------------------

class TestFailureDetector(unittest.TestCase):
    def _make_detector(self):
        from self_healing.detector import FailureDetector
        return FailureDetector(failure_threshold=3)

    def test_healthy_signals_not_flagged(self):
        det = self._make_detector()
        for _ in range(5):
            det.record("svc_a", True)
        self.assertEqual(det.detect_failures(), [])

    def test_consecutive_failures_flagged(self):
        det = self._make_detector()
        for _ in range(3):
            det.record("svc_a", False)
        self.assertIn("svc_a", det.detect_failures())

    def test_below_threshold_not_flagged(self):
        det = self._make_detector()
        det.record("svc_a", True)
        det.record("svc_a", False)
        det.record("svc_a", False)
        self.assertEqual(det.detect_failures(), [])

    def test_health_score_all_healthy(self):
        det = self._make_detector()
        for _ in range(5):
            det.record("svc_b", True)
        self.assertEqual(det.health_score("svc_b"), 1.0)

    def test_health_score_all_failed(self):
        det = self._make_detector()
        for _ in range(5):
            det.record("svc_b", False)
        self.assertEqual(det.health_score("svc_b"), 0.0)

    def test_on_failure_callback(self):
        called = []
        from self_healing.detector import FailureDetector
        det = FailureDetector(failure_threshold=2, on_failure=lambda n, r: called.append(n))
        for _ in range(2):
            det.record("svc_c", False)
        det.detect_failures()
        self.assertIn("svc_c", called)

    def test_heartbeat_timeout(self):
        import time
        from self_healing.detector import FailureDetector
        det = FailureDetector(failure_threshold=3, heartbeat_timeout=0.01)
        det.record("svc_d", True)
        time.sleep(0.05)
        failures = det.detect_failures()
        self.assertIn("svc_d", failures)


class TestRecoveryManager(unittest.TestCase):
    def _make_manager(self):
        from self_healing.recovery import RecoveryManager
        return RecoveryManager(max_attempts=3, base_delay=0.0)

    def test_default_strategy_succeeds(self):
        mgr = self._make_manager()
        result = asyncio.run(mgr.attempt_recovery("svc_a"))
        self.assertTrue(result)

    def test_custom_strategy_used(self):
        mgr = self._make_manager()
        called = []

        async def my_strategy(name):
            called.append(name)
            return True

        mgr.register_strategy("svc_b", my_strategy)
        asyncio.run(mgr.attempt_recovery("svc_b"))
        self.assertIn("svc_b", called)

    def test_max_attempts_escalates(self):
        escalated = []
        from self_healing.recovery import RecoveryManager
        mgr = RecoveryManager(
            max_attempts=2,
            base_delay=0.0,
            escalation_hook=lambda n: escalated.append(n),
        )

        async def failing(_):
            return False

        mgr.register_strategy("svc_c", failing)
        asyncio.run(mgr.attempt_recovery("svc_c"))
        asyncio.run(mgr.attempt_recovery("svc_c"))
        result = asyncio.run(mgr.attempt_recovery("svc_c"))  # exceeds max
        self.assertFalse(result)
        self.assertIn("svc_c", escalated)

    def test_heal_all(self):
        mgr = self._make_manager()
        results = asyncio.run(mgr.heal_all(["svc_a", "svc_b"]))
        self.assertTrue(results["svc_a"])
        self.assertTrue(results["svc_b"])

    def test_recovery_summary(self):
        mgr = self._make_manager()
        asyncio.run(mgr.attempt_recovery("svc_a"))
        summary = mgr.recovery_summary()
        self.assertIn("total_attempts", summary)


class TestStateStore(unittest.TestCase):
    def _make_store(self):
        from self_healing.state_store import StateStore
        tmp = tempfile.mkdtemp()
        return StateStore(Path(tmp) / "state.json")

    def test_set_and_get(self):
        store = self._make_store()
        store.set("key1", "value1")
        self.assertEqual(store.get("key1"), "value1")

    def test_default_on_missing(self):
        store = self._make_store()
        self.assertIsNone(store.get("nonexistent"))
        self.assertEqual(store.get("nonexistent", "default"), "default")

    def test_delete(self):
        store = self._make_store()
        store.set("key2", 42)
        store.delete("key2")
        self.assertIsNone(store.get("key2"))

    def test_persistence(self):
        from self_healing.state_store import StateStore
        tmp = tempfile.mkdtemp()
        path = Path(tmp) / "state.json"
        store1 = StateStore(path)
        store1.set("persistent_key", "hello")
        store2 = StateStore(path)
        self.assertEqual(store2.get("persistent_key"), "hello")

    def test_snapshot_and_restore(self):
        store = self._make_store()
        store.snapshot_subsystem("svc_a", {"status": "healthy"})
        snap = store.restore_snapshot("svc_a")
        self.assertIsNotNone(snap)
        self.assertEqual(snap["status"], "healthy")

    def test_record_and_query_events(self):
        store = self._make_store()
        store.record_event("HEALED", {"subsystem": "svc_a"})
        store.record_event("FAILED", {"subsystem": "svc_b"})
        events = store.query_events("HEALED")
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]["subsystem"], "svc_a")


# ---------------------------------------------------------------------------
# monitoring tests
# ---------------------------------------------------------------------------

class TestMetricsCollector(unittest.TestCase):
    def _make_collector(self):
        from monitoring.metrics import MetricsCollector
        return MetricsCollector()

    def test_gauge_record_and_stats(self):
        c = self._make_collector()
        g = c.gauge("cpu")
        g.record(10.0)
        g.record(20.0)
        stats = g.stats()
        self.assertEqual(stats["count"], 2)
        self.assertEqual(stats["latest"], 20.0)
        self.assertAlmostEqual(stats["mean"], 15.0)

    def test_counter_increment(self):
        c = self._make_collector()
        ctr = c.counter("cycles")
        ctr.increment()
        ctr.increment(3)
        self.assertEqual(ctr.value, 4)

    def test_snapshot_keys(self):
        c = self._make_collector()
        c.gauge("health").record(0.9)
        c.counter("actions").increment()
        snap = c.snapshot()
        self.assertIn("gauges", snap)
        self.assertIn("counters", snap)

    def test_record_cycle(self):
        c = self._make_collector()
        c.record_cycle(1, 3, 4, healing_triggered=True)
        snap = c.snapshot()
        self.assertEqual(snap["counters"]["total_cycles"], 1)
        self.assertEqual(snap["counters"]["healing_actions"], 1)


class TestHealthIndicator(unittest.TestCase):
    def _make_indicator(self):
        from monitoring.health import HealthIndicator
        return HealthIndicator("test")

    def test_all_passing(self):
        ind = self._make_indicator()
        ind.add_check("always_ok", lambda: (True, "ok"))
        report = ind.run()
        self.assertEqual(report["level"], "green")
        self.assertEqual(report["passed"], 1)

    def test_all_failing(self):
        ind = self._make_indicator()
        ind.add_check("always_fail", lambda: (False, "err"))
        report = ind.run()
        self.assertEqual(report["level"], "red")
        self.assertEqual(report["passed"], 0)

    def test_mixed_checks_yellow(self):
        ind = self._make_indicator()
        ind.add_check("ok1", lambda: (True, "ok"))
        ind.add_check("fail1", lambda: (False, "err"))
        report = ind.run()
        self.assertEqual(report["level"], "yellow")

    def test_latest(self):
        ind = self._make_indicator()
        ind.add_check("c", lambda: (True, ""))
        ind.run()
        self.assertIsNotNone(ind.latest())

    def test_trend_stable(self):
        ind = self._make_indicator()
        ind.add_check("c", lambda: (True, ""))
        for _ in range(5):
            ind.run()
        self.assertEqual(ind.trend(), "stable")


class TestDashboard(unittest.TestCase):
    def test_render_writes_file(self):
        from monitoring.dashboard import Dashboard
        with tempfile.TemporaryDirectory() as tmp:
            db = Dashboard(tmp)
            snap = db.render(
                subsystems={"svc_a": {"status": "healthy"}},
                metrics_snapshot={"gauges": {}, "counters": {}},
            )
            self.assertIn("generated_at", snap)
            path = Path(tmp) / "dashboard.json"
            self.assertTrue(path.exists())
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertIn("subsystems", data)

    def test_evolution_log(self):
        from monitoring.dashboard import Dashboard
        with tempfile.TemporaryDirectory() as tmp:
            db = Dashboard(tmp)
            db.record_evolution_snapshot(1, {"health_ratio": 0.9})
            evo = json.loads((Path(tmp) / "evolution_log.json").read_text(encoding="utf-8"))
            self.assertEqual(len(evo), 1)
            self.assertEqual(evo[0]["cycle"], 1)


# ---------------------------------------------------------------------------
# main_organism tests
# ---------------------------------------------------------------------------

class TestMasterOrchestrator(unittest.TestCase):
    def _make_orchestrator(self):
        import os
        import tempfile
        from main_organism import MasterOrchestrator
        # Point state file to a temp dir so tests don't pollute data/
        tmp = tempfile.mkdtemp()
        import main_organism
        main_organism.STATE_FILE = Path(tmp) / "state.json"
        main_organism.DATA_DIR = Path(tmp)
        main_organism.LOG_DIR = Path(tmp)
        return MasterOrchestrator()

    def test_instantiation(self):
        orch = self._make_orchestrator()
        self.assertIsNotNone(orch)
        self.assertIn("AXCONTROL", orch.subsystems)

    def test_register_subsystem(self):
        orch = self._make_orchestrator()
        sub = orch.register_subsystem("NewSvc")
        self.assertIn("NewSvc", orch.subsystems)

    def test_get_status_empty(self):
        orch = self._make_orchestrator()
        status = orch.get_status()
        self.assertIsInstance(status, dict)

    def test_health_check_cycle(self):
        orch = self._make_orchestrator()
        results = asyncio.run(orch._health_check_cycle())
        self.assertIsInstance(results, dict)

    def test_save_and_load_state(self):
        import tempfile
        tmp = tempfile.mkdtemp()
        from main_organism import MasterOrchestrator
        import main_organism
        main_organism.STATE_FILE = Path(tmp) / "state.json"
        main_organism.DATA_DIR = Path(tmp)
        main_organism.LOG_DIR = Path(tmp)

        orch = MasterOrchestrator()
        orch.subsystems["AXCONTROL"].restart_count = 7
        orch._save_state()

        orch2 = MasterOrchestrator()
        self.assertEqual(orch2.subsystems["AXCONTROL"].restart_count, 7)

    def test_publish_event(self):
        orch = self._make_orchestrator()
        asyncio.run(orch.publish("TEST_EVENT", {"msg": "hello"}))
        self.assertFalse(orch._event_queue.empty())

    def test_short_run(self):
        """Organism starts, completes one cycle, and stops cleanly."""
        import tempfile
        tmp = tempfile.mkdtemp()
        from main_organism import MasterOrchestrator
        import main_organism
        main_organism.STATE_FILE = Path(tmp) / "state.json"
        main_organism.DATA_DIR = Path(tmp)
        main_organism.LOG_DIR = Path(tmp)
        main_organism.MasterOrchestrator.CYCLE_INTERVAL = 0  # instant

        orch = MasterOrchestrator()

        async def _run():
            orch.running = True
            # Run exactly one iteration of the internal loop body
            await orch._health_check_cycle()
            snapshot = orch.monitoring.capture(orch.subsystems)
            orch.monitoring.write_dashboard(Path(tmp) / "dashboard.json")
            orch.intelligence.ingest_metrics(snapshot)
            await orch.healer.run_healing_cycle()
            orch._save_state()

        asyncio.run(_run())
        self.assertTrue((Path(tmp) / "state.json").exists())


if __name__ == "__main__":
    unittest.main()
