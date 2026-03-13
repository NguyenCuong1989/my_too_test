# Σ_APΩ₂ CORE MODULE
# Authority: BỐ CƯỐNG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL - WATCHDOG

import logging

class GovernanceWatchdog:
    """
    🛡️ Governance Heartbeat (Watchdog)
    Constraint: if steps_since_Ω > k -> redirect to Ω
    Prevents: Runaway loops, deadlocks, and governance bypass.
    """
    def __init__(self, max_steps=5):
        self.logger = logging.getLogger("Ω_WATCHDOG")
        self.max_steps = max_steps
        self.steps_since_last_omega = 0

    def observe_step(self, step_type: str):
        """
        Observes a single transition step in the runtime.
        """
        if step_type == "OMEGA_GATE":
            self.steps_since_last_omega = 0
            self.logger.info("💓 HEARTBEAT: Governance sync verified.")
        else:
            self.steps_since_last_omega += 1

        if self.steps_since_last_omega >= self.max_steps:
            self.logger.critical("🚨 WATCHDOG_TRIP: Max steps exceeded. Forcing Return to Ω.")
            return "FORCE_OMEGA_RETURN"

        return "STABLE"

    def check_liveness(self, axes_status: dict):
        # Detects message queue deadlocks (Option B - Axis Isolation)
        for axis, status in axes_status.items():
            if status == "STALLED":
                self.logger.warning(f"⚠️ ISOLATION: Axis {axis} is stalled. Triggering fail-fast.")
                return f"ISOLATE_{axis}"
        return "LIVENESS_OK"
