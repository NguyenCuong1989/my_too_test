"""Runtime watchdog.

Enforces timeouts, rate limits, and STOP conditions during execution.
"""
from typing import Optional


class Watchdog:
    def __init__(self, max_duration_ms: int, max_events: int):
        self.max_duration_ms = max_duration_ms
        self.max_events = max_events

    def guard(self, start_ts: float, event_count: int) -> Optional[str]:
        """Return stop reason if limits exceeded, else None."""
        raise NotImplementedError("Phase 1 stub: watchdog checks to be implemented in Phase 2")
