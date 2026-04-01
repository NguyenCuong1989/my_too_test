# =============================================================================
# PROJECT: CANON-TO-SYSTEM DETERMINISTIC PROJECTION
# METHOD: D&R PROTOCOL (CLOSED)
#
# ORIGINATOR / CREATOR:
#   alpha_prime_omega
#
# LEGAL ONTOLOGY:
#   This source file is a deterministic projection of a closed Canon.
#   Removal or alteration of this header voids legal and ontological validity.
#
# STATUS:
#   GENERATED — NON-AUTONOMOUS — NON-OWNERLESS
#
# TRACEABILITY:
#   Canon -> COG -> Projection(Π) -> Artifact
#
# =============================================================================
"""Runtime watchdog.

Enforces timeouts, rate limits, and STOP conditions during execution.
"""

import time
from typing import Optional

from core.Menh.stop_reasons import StopReason


class Watchdog:
    def __init__(self, max_duration_ms: int = 5000, max_events: int = 100):
        self.max_duration_ms = max_duration_ms
        self.max_events = max_events

    def guard(
        self, start_ts: float, event_count: int, kill_switch_engaged: bool = False
    ) -> Optional[StopReason]:
        """Return stop reason if limits exceeded or human override triggered."""
        if kill_switch_engaged:
            return StopReason.KILL_SWITCH

        elapsed_ms = (time.time() - start_ts) * 1000
        if elapsed_ms > self.max_duration_ms:
            return StopReason.TIMING_VIOLATION

        if event_count > self.max_events:
            return StopReason.CAUSALITY_VIOLATION  # Excessive events implies loop or malfunction

        return None
