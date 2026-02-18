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
"""Simple rate limiter for input emit (TAB-first safe mode)."""

import time
from typing import Optional


class RateLimiter:
    def __init__(self, min_interval_ms: int = 200):
        self.min_interval_ms = min_interval_ms
        self._last_ts_ms: Optional[float] = None

    def allow(self) -> bool:
        now = time.time() * 1000
        if self._last_ts_ms is None or (now - self._last_ts_ms) >= self.min_interval_ms:
            self._last_ts_ms = now
            return True
        return False
