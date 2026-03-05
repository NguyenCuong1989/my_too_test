"""
Recovery Manager

Executes auto-recovery procedures for failed subsystems.
Supports pluggable recovery strategies (restart, rollback, dependency
healing) with exponential back-off.
"""

from __future__ import annotations

import asyncio
import logging
import time
from typing import Callable, Awaitable


logger = logging.getLogger(__name__)

RecoveryFn = Callable[[str], Awaitable[bool]]


class RecoveryManager:
    """
    Manages recovery procedures for failing subsystems.

    Parameters
    ----------
    max_attempts:
        Maximum consecutive recovery attempts before giving up and
        escalating.
    base_delay:
        Base back-off delay in seconds (doubles each attempt).
    """

    def __init__(
        self,
        max_attempts: int = 5,
        base_delay: float = 2.0,
        escalation_hook: Callable[[str], None] | None = None,
    ) -> None:
        self.max_attempts = max_attempts
        self.base_delay = base_delay
        self.escalation_hook = escalation_hook

        self._attempt_counts: dict[str, int] = {}
        self._last_attempt: dict[str, float] = {}
        self._strategies: dict[str, RecoveryFn] = {}
        self._recovery_log: list[dict] = []

    # ------------------------------------------------------------------
    # Strategy registry
    # ------------------------------------------------------------------

    def register_strategy(self, subsystem: str, fn: RecoveryFn) -> None:
        """Register a custom async recovery function for a subsystem."""
        self._strategies[subsystem] = fn

    # ------------------------------------------------------------------
    # Recovery execution
    # ------------------------------------------------------------------

    async def attempt_recovery(self, subsystem: str) -> bool:
        """
        Try to recover *subsystem*.  Uses a registered strategy if
        available, otherwise falls back to a generic restart simulation.

        Returns True on success, False on failure.
        """
        attempts = self._attempt_counts.get(subsystem, 0)

        if attempts >= self.max_attempts:
            logger.error(
                "🆘 %s exceeded max recovery attempts (%d). Escalating.",
                subsystem,
                self.max_attempts,
            )
            if self.escalation_hook:
                self.escalation_hook(subsystem)
            return False

        # Exponential back-off
        if attempts > 0:
            delay = self.base_delay * (2 ** (attempts - 1))
            logger.info("⏳ Back-off %ss before retrying %s", delay, subsystem)
            await asyncio.sleep(delay)

        self._attempt_counts[subsystem] = attempts + 1
        self._last_attempt[subsystem] = time.time()

        strategy = self._strategies.get(subsystem, self._default_strategy)
        try:
            success = await strategy(subsystem)
        except Exception as exc:
            logger.error("Recovery strategy raised: %s", exc)
            success = False

        entry = {
            "subsystem": subsystem,
            "attempt": attempts + 1,
            "success": success,
            "ts": time.time(),
        }
        self._recovery_log.append(entry)
        if len(self._recovery_log) > 500:
            self._recovery_log = self._recovery_log[-250:]

        if success:
            logger.info("✅ Recovery succeeded for %s (attempt %d)", subsystem, attempts + 1)
            self._attempt_counts[subsystem] = 0  # reset counter on success
        else:
            logger.warning(
                "❌ Recovery attempt %d/%d failed for %s",
                attempts + 1,
                self.max_attempts,
                subsystem,
            )
        return success

    # ------------------------------------------------------------------
    # Default strategy
    # ------------------------------------------------------------------

    @staticmethod
    async def _default_strategy(subsystem: str) -> bool:
        """Generic restart simulation (override with real process control)."""
        logger.info("🔄 Default restart strategy for %s", subsystem)
        await asyncio.sleep(0.05)  # simulate restart time
        return True

    # ------------------------------------------------------------------
    # Batch recovery
    # ------------------------------------------------------------------

    async def heal_all(self, failing: list[str]) -> dict[str, bool]:
        """Attempt recovery for every subsystem in *failing*."""
        results: dict[str, bool] = {}
        tasks = {name: self.attempt_recovery(name) for name in failing}
        for name, coro in tasks.items():
            results[name] = await coro
        return results

    # ------------------------------------------------------------------
    # Dependency healing
    # ------------------------------------------------------------------

    async def heal_dependencies(
        self, subsystem: str, deps: list[str]
    ) -> dict[str, bool]:
        """
        Heal dependencies first, then the subsystem itself.
        Useful when a component fails due to a broken upstream.
        """
        results: dict[str, bool] = {}
        for dep in deps:
            results[dep] = await self.attempt_recovery(dep)
        results[subsystem] = await self.attempt_recovery(subsystem)
        return results

    # ------------------------------------------------------------------
    # Reporting
    # ------------------------------------------------------------------

    def recovery_summary(self) -> dict:
        return {
            "total_attempts": sum(self._attempt_counts.values()),
            "log_entries": len(self._recovery_log),
            "last_entries": self._recovery_log[-5:],
        }
