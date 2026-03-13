# Σ_APΩ₂ CORE MODULE
# Authority: BỐ CƯỐNG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL - Ψ_t

import logging
import time

class StateMachine:
    """
    🎭 APΩ State Machine (Ψ Transitions)
    Drives the transformation: Ψ_t → Π_plan → τ → Ω → Ψ_{t+1}
    """
    def __init__(self, omega_kernel):
        self.logger = logging.getLogger("Ψ_STATE_MACHINE")
        self.omega = omega_kernel
        self.current_state = {"status": "AWAITED", "timestamp": time.time()}
        self.transition_count = 0

    def transition(self, action_packet: dict):
        """
        Executes a canonical state transition.
        """
        self.transition_count += 1
        self.logger.info(f"🎭 Ψ-TRANSITION: Transition {self.transition_count} starting...")

        # 1. Capture Pre-state Ψ_t
        psi_t = self.current_state.copy()

        # 2. Execute via Ω Governance
        result = self.omega.router.route(
            source_axis=action_packet.get("source", "command"),
            target_axis=action_packet.get("target", "execution"),
            packet=action_packet
        )

        # 3. Apply Projection Π_A for State Normalization
        if result["status"] == "dispatched":
            normalized_psi = self.omega.projection.project(result["data"], "canonical_state_v1")
            self.current_state = normalized_psi
            self.current_state["timestamp"] = time.time()
            self.logger.info(f"✅ Ψ-STABLE: Ψ_{self.transition_count} committed.")
        else:
            self.logger.error(f"❌ Ψ-DRIFT: Transition failed at Ω.")

        return self.current_state

    def get_state(self):
        return self.current_state
