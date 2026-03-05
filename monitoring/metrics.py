"""
Metrics Collector

Collects, aggregates and exports real-time performance metrics
for all organism subsystems.
"""

from __future__ import annotations

import time
from collections import deque
from dataclasses import dataclass, field
from statistics import mean, stdev


@dataclass
class Sample:
    value: float
    timestamp: float = field(default_factory=time.time)


class Gauge:
    """A rolling-window numeric metric."""

    def __init__(self, name: str, window: int = 60) -> None:
        self.name = name
        self._samples: deque[Sample] = deque(maxlen=window)

    def record(self, value: float) -> None:
        self._samples.append(Sample(value=value))

    @property
    def latest(self) -> float | None:
        return self._samples[-1].value if self._samples else None

    def stats(self) -> dict:
        if not self._samples:
            return {"count": 0}
        vals = [s.value for s in self._samples]
        result: dict = {"count": len(vals), "latest": vals[-1], "mean": round(mean(vals), 4)}
        if len(vals) >= 2:
            result["stdev"] = round(stdev(vals), 4)
        return result


class Counter:
    """A monotonically increasing counter."""

    def __init__(self, name: str) -> None:
        self.name = name
        self._value: int = 0

    def increment(self, by: int = 1) -> None:
        self._value += by

    @property
    def value(self) -> int:
        return self._value

    def to_dict(self) -> dict:
        return {"name": self.name, "value": self._value}


class MetricsCollector:
    """
    Central registry for organism metrics.

    Usage::

        collector = MetricsCollector()
        collector.gauge("cpu_pct").record(42.3)
        collector.counter("healing_actions").increment()
        print(collector.snapshot())
    """

    def __init__(self) -> None:
        self._gauges: dict[str, Gauge] = {}
        self._counters: dict[str, Counter] = {}

    # ------------------------------------------------------------------
    # Accessors
    # ------------------------------------------------------------------

    def gauge(self, name: str, window: int = 60) -> Gauge:
        if name not in self._gauges:
            self._gauges[name] = Gauge(name, window)
        return self._gauges[name]

    def counter(self, name: str) -> Counter:
        if name not in self._counters:
            self._counters[name] = Counter(name)
        return self._counters[name]

    # ------------------------------------------------------------------
    # Snapshot
    # ------------------------------------------------------------------

    def snapshot(self) -> dict:
        return {
            "ts": time.time(),
            "gauges": {n: g.stats() for n, g in self._gauges.items()},
            "counters": {n: c.value for n, c in self._counters.items()},
        }

    # ------------------------------------------------------------------
    # Convenience recorders
    # ------------------------------------------------------------------

    def record_cycle(
        self,
        cycle: int,
        healthy_count: int,
        total_count: int,
        healing_triggered: bool = False,
    ) -> None:
        self.gauge("health_ratio").record(healthy_count / max(total_count, 1))
        self.gauge("cycle_number").record(cycle)
        self.counter("total_cycles").increment()
        if healing_triggered:
            self.counter("healing_actions").increment()
