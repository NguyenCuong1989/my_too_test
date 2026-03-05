"""
synergy.py — Synergy Evaluation (refactored from synergy_run.py)

Phase 3: runs the Orchestrator for a controlled number of cycles to verify
inter-node pulse overlap and SymphonyControlCenter coordination.
"""

import asyncio
import logging
from pathlib import Path

from src.config.settings import DAIOF_INSTALL_DIR

logger = logging.getLogger(__name__)


def _load_operator(base_dir: Path):
    """Dynamically import the AutonomousOperator from *base_dir*."""
    import sys

    sys.path.insert(0, str(base_dir))
    sys.path.insert(0, str(base_dir / "autonomous_operator"))
    sys.path.insert(0, str(base_dir / "autonomous_operator" / "nodes"))
    sys.path.insert(0, str(base_dir / "DAIOF-Framework"))

    from orchestrator_v3 import AutonomousOperator  # noqa: PLC0415

    return AutonomousOperator


class SynergyOperator:
    """Wraps an :class:`AutonomousOperator` to run a fixed number of cycles."""

    def __init__(self, operator):
        self._operator = operator

    async def run_controlled(self, cycles: int = 1) -> None:
        """Execute *cycles* orchestration cycles then stop.

        Args:
            cycles: Number of full cycles to execute (default 1).
        """
        op = self._operator
        print(f"[SYNERGY] Activating DAIOF fleet (max cycles: {cycles})")
        print("-" * 58)

        for i in range(1, cycles + 1):
            print(f"\n--- CYCLE {i} STARTING ---")

            op.link.send_pulse(
                node_name="SynergyOrchestrator",
                pulse_type="SYNERGY_HEARTBEAT",
                content=f"Integrated test cycle {i}",
                intensity=1.0,
            )

            print("[Node: Recovery] Running...")
            op.recovery.run_cycle()

            print("[Node: Web] Running...")
            await op.web.run_cycle()

            print("[Node: Biz] Running (limited scan)...")
            op.biz.run_cycle()

            print("[Node: Guardian] Running...")
            op.guardian.run_cycle()

            print("[Node: Audit] Running...")
            op.audit.run_cycle()

            if getattr(op, "symphony", None):
                print("[Symphony] Conducting...")
                op.symphony.conduct_symphony()

            print(f"--- CYCLE {i} COMPLETED ---")

        print("-" * 58)
        print("[SYNERGY EVALUATION COMPLETE]")


async def run_synergy(base_dir: Path | None = None, cycles: int = 1) -> None:
    """Entry point for a synergy evaluation run.

    Args:
        base_dir: Root directory of the DAIOF installation.
        cycles: Number of orchestration cycles to execute.
    """
    if base_dir is None:
        base_dir = DAIOF_INSTALL_DIR

    logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")

    AutonomousOperator = _load_operator(base_dir)
    operator = AutonomousOperator()
    synergy = SynergyOperator(operator)
    await synergy.run_controlled(cycles=cycles)
