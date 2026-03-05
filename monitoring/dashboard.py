"""
Dashboard

Generates real-time status reports and persists them as JSON files
for consumption by external monitoring tools or CI workflows.
"""

from __future__ import annotations

import json
import time
from datetime import datetime, timezone
from pathlib import Path


class Dashboard:
    """
    Assembles organism metrics, health indicators, and subsystem
    state into a unified dashboard snapshot.

    Parameters
    ----------
    output_dir:
        Directory where dashboard snapshots are written.
    """

    def __init__(self, output_dir: str | Path = "data") -> None:
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # Rendering
    # ------------------------------------------------------------------

    def render(
        self,
        subsystems: dict,
        metrics_snapshot: dict,
        health_report: dict | None = None,
        extra: dict | None = None,
    ) -> dict:
        """
        Compose a complete dashboard snapshot from all data sources.

        Returns the assembled dict (and also writes it to disk).
        """
        snapshot = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "epoch": time.time(),
            "subsystems": subsystems,
            "metrics": metrics_snapshot,
        }
        if health_report:
            snapshot["health"] = health_report
        if extra:
            snapshot.update(extra)

        self._write(snapshot, "dashboard.json")
        return snapshot

    def _write(self, data: dict, filename: str) -> None:
        path = self.output_dir / filename
        try:
            path.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
        except OSError:
            pass  # non-fatal – dashboard write should never crash the organism

    # ------------------------------------------------------------------
    # Evolution tracking
    # ------------------------------------------------------------------

    def record_evolution_snapshot(self, cycle: int, insights: dict) -> None:
        """Append an evolution record to the evolution log."""
        record = {
            "cycle": cycle,
            "ts": datetime.now(timezone.utc).isoformat(),
            **insights,
        }
        evolution_log = self.output_dir / "evolution_log.json"
        history: list = []
        if evolution_log.exists():
            try:
                history = json.loads(evolution_log.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                history = []
        history.append(record)
        if len(history) > 500:
            history = history[-250:]
        try:
            evolution_log.write_text(
                json.dumps(history, indent=2, default=str), encoding="utf-8"
            )
        except OSError:
            pass

    # ------------------------------------------------------------------
    # Performance report
    # ------------------------------------------------------------------

    def performance_report(self, metrics_snapshot: dict) -> dict:
        """Generate a human-readable performance summary."""
        gauges = metrics_snapshot.get("gauges", {})
        counters = metrics_snapshot.get("counters", {})
        health_ratio_stats = gauges.get("health_ratio", {})

        return {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "health_ratio": health_ratio_stats.get("latest"),
            "mean_health_ratio": health_ratio_stats.get("mean"),
            "total_cycles": counters.get("total_cycles", 0),
            "healing_actions": counters.get("healing_actions", 0),
        }
