"""
Failure Detector

Monitors subsystem health signals and raises alerts when
anomalies or degraded states are detected.
"""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from typing import Callable


logger = logging.getLogger(__name__)


@dataclass
class HealthSignal:
    subsystem: str
    healthy: bool
    timestamp: float = field(default_factory=time.time)
    detail: str = ""


class FailureDetector:
    """
    Collects health signals and decides whether a subsystem
    requires intervention.

    Parameters
    ----------
    failure_threshold:
        Number of consecutive unhealthy signals before a subsystem
        is declared failed.
    heartbeat_timeout:
        Seconds since last heartbeat after which a subsystem is
        considered timed-out.
    """

    def __init__(
        self,
        failure_threshold: int = 3,
        heartbeat_timeout: float = 120.0,
        on_failure: Callable[[str, str], None] | None = None,
    ) -> None:
        self.failure_threshold = failure_threshold
        self.heartbeat_timeout = heartbeat_timeout
        self.on_failure = on_failure

        self._signals: dict[str, list[HealthSignal]] = {}
        self._last_seen: dict[str, float] = {}

    # ------------------------------------------------------------------
    # Signal ingestion
    # ------------------------------------------------------------------

    def record(self, subsystem: str, healthy: bool, detail: str = "") -> None:
        """Record one health reading for a subsystem."""
        sig = HealthSignal(subsystem=subsystem, healthy=healthy, detail=detail)
        self._signals.setdefault(subsystem, []).append(sig)
        if healthy:
            self._last_seen[subsystem] = time.time()
        # Rolling window – keep last 20 signals per subsystem
        if len(self._signals[subsystem]) > 20:
            self._signals[subsystem] = self._signals[subsystem][-20:]

    # ------------------------------------------------------------------
    # Analysis
    # ------------------------------------------------------------------

    def consecutive_failures(self, subsystem: str) -> int:
        """Return the number of trailing consecutive unhealthy signals."""
        signals = self._signals.get(subsystem, [])
        count = 0
        for sig in reversed(signals):
            if not sig.healthy:
                count += 1
            else:
                break
        return count

    def is_timed_out(self, subsystem: str) -> bool:
        last = self._last_seen.get(subsystem)
        if last is None:
            return False
        return (time.time() - last) > self.heartbeat_timeout

    def detect_failures(self) -> list[str]:
        """
        Analyse all tracked subsystems and return the names of those
        that require healing.  Fires ``on_failure`` callback for each.
        """
        failing = []
        for name in list(self._signals):
            reason = None
            if self.consecutive_failures(name) >= self.failure_threshold:
                reason = f"{self.failure_threshold} consecutive failures"
            elif self.is_timed_out(name):
                reason = "heartbeat timeout"

            if reason:
                failing.append(name)
                logger.warning("⚠️  Failure detected – %s: %s", name, reason)
                if self.on_failure:
                    self.on_failure(name, reason)
        return failing

    # ------------------------------------------------------------------
    # Anomaly helpers
    # ------------------------------------------------------------------

    def health_score(self, subsystem: str) -> float:
        """Return a 0.0–1.0 health score based on recent signals."""
        signals = self._signals.get(subsystem, [])
        if not signals:
            return 1.0
        window = signals[-10:]
        return sum(1 for s in window if s.healthy) / len(window)
