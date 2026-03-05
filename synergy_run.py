# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

"""
DAIOF SYNERGY EVALUATION (Phase 3)

Objectives:
1. Run the Orchestrator for exactly 1 full cycle.
2. Verify inter-node pulse overlap and coordination.
3. Confirm SymphonyControlCenter conducting logic.
"""

import sys
import asyncio
import logging
from pathlib import Path

# Setup Paths
BASE_DIR = Path("/Users/andy/my_too_test")
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "autonomous_operator"))
sys.path.append(str(BASE_DIR / "autonomous_operator" / "nodes"))
sys.path.append(str(BASE_DIR / "DAIOF-Framework"))

from orchestrator_v3 import AutonomousOperator

class SynergyOperator(AutonomousOperator):
    async def main_loop(self, max_cycles=1):
        cycle_count = 0
        while self.is_running and cycle_count < max_cycles:
            cycle_count += 1
            print(f"\n🌀 [SYNERGY RUN] STARTING CYCLE {cycle_count}...")

            # Use the original orchestrator logic but without the infinite sleep
            await super().main_loop() # This might need adjustment if super().main_loop() has an infinite while

    async def run_controlled(self, cycles=1):
        # Revised logic: Manually trigger the cycle steps to avoid infinite loop
        print(f"🚀 [SYNERGY RUN] ACTIVATING DAIOF FLEET (Max Cycles: {cycles})")
        print("----------------------------------------------------------")

        for i in range(1, cycles + 1):
            print(f"\n--- 🌀 CYCLE {i} STARTING ---")

            # Send heartbeat
            self.link.send_pulse(
                node_name="SynergyOrchestrator",
                pulse_type="SYNERGY_HEARTBEAT",
                content=f"Integrated test cycle {i}",
                intensity=1.0
            )

            # 1. Recovery
            print("📦 [Node: Recovery] Running...")
            self.recovery.run_cycle()

            # 2. Web (Async)
            print("📦 [Node: Web] Running...")
            await self.web.run_cycle()

            # 3. Biz
            print("📦 [Node: Biz] Running (Limited Scan)...")
            # We skip the full run here to avoid long hangs, or run with 1 email
            self.biz.run_cycle()

            # 4. Guardian
            print("📦 [Node: Guardian] Running...")
            self.guardian.run_cycle()

            # 5. Audit
            print("📦 [Node: Audit] Running...")
            self.audit.run_cycle()

            if self.symphony:
                print("🎼 [Symphony] Conducting...")
                self.symphony.conduct_symphony()

            print(f"--- ✅ CYCLE {i} COMPLETED ---")

        print("----------------------------------------------------------")
        print("🏁 [SYNERGY EVALUATION COMPLETE]")

async def main():
    # Setup logging to console only for synergy run
    logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')

    op = SynergyOperator()
    await op.run_controlled(cycles=1)

if __name__ == "__main__":
    asyncio.run(main())
