"""
Health Indicator

Provides a simple API to compute and expose composite health
indicators for the organism and its subsystems.
"""

from __future__ import annotations

import time
from enum import Enum
from typing import Callable


class HealthLevel(str, Enum):
    GREEN = "green"   # Fully healthy
    YELLOW = "yellow" # Degraded but operational
    RED = "red"       # Critical / failed


class HealthIndicator:
    """
    Aggregates component health checks into a single composite score.

    Parameters
    ----------
    name:
        Human-readable name of this indicator.
    checks:
        Mapping of check name → callable returning (bool, str).
        The bool signals pass/fail; the str is an optional detail message.
    """

    def __init__(
        self,
        name: str,
        checks: dict[str, Callable[[], tuple[bool, str]]] | None = None,
    ) -> None:
        self.name = name
        self._checks: dict[str, Callable[[], tuple[bool, str]]] = checks or {}
        self._history: list[dict] = []

    def add_check(self, name: str, fn: Callable[[], tuple[bool, str]]) -> None:
        self._checks[name] = fn

    def run(self) -> dict:
        results: dict[str, dict] = {}
        passed = 0
        for check_name, fn in self._checks.items():
            try:
                ok, detail = fn()
            except Exception as exc:
                ok, detail = False, str(exc)
            results[check_name] = {"ok": ok, "detail": detail}
            if ok:
                passed += 1

        total = len(self._checks)
        ratio = passed / total if total > 0 else 1.0
        level = (
            HealthLevel.GREEN
            if ratio == 1.0
            else HealthLevel.YELLOW
            if ratio >= 0.5
            else HealthLevel.RED
        )

        report = {
            "indicator": self.name,
            "level": level.value,
            "passed": passed,
            "total": total,
            "ratio": round(ratio, 3),
            "checks": results,
            "ts": time.time(),
        }
        self._history.append(report)
        if len(self._history) > 100:
            self._history = self._history[-50:]
        return report

    def latest(self) -> dict | None:
        return self._history[-1] if self._history else None

    def trend(self, window: int = 10) -> str:
        """Return 'improving', 'stable', or 'degrading' based on recent history."""
        recent = [h["ratio"] for h in self._history[-window:]]
        if len(recent) < 2:
            return "stable"
        delta = recent[-1] - recent[0]
        if delta > 0.05:
            return "improving"
        if delta < -0.05:
            return "degrading"
        return "stable"
