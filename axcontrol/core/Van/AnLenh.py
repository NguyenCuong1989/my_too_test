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
"""Execution orchestration.

Receives validated, signed CommandEnvelope and performs bounded action via bridges/emitters.
"""

import time
from typing import Any, List, Optional, Dict

from core.Chinh.command import CommandEnvelope, CommandType, AtomicStepType, AtomicStep
from core.The.ui_state import UIState
from core.The.ctrl_state import CtrlState
from core.The.normalize import normalize_ui_state
from core.Menh.stop_reasons import StopReason
from core.tools import shell_cli
from adapters.macos_ax import observer


class Executor:
    def __init__(self, ax_bridge, event_emitter, watchdog, kill_switch=None):
        self.ax_bridge = ax_bridge
        self.event_emitter = event_emitter
        self.watchdog = watchdog
        self.kill_switch = kill_switch

    def _settle_by_convergence(self, timeout_ms: int = 1000, stable_req: int = 3) -> str:
        """Wait until UIState.hash is stable over N consecutive observations."""
        last_hash = None
        stable_count = 0
        start_ts = time.time()

        while (time.time() - start_ts) * 1000 < timeout_ms:
            raw = observer.observe()
            if not raw:
                continue
            curr_hash = normalize_ui_state(raw).hash

            if curr_hash == last_hash:
                stable_count += 1
            else:
                stable_count = 0

            if stable_count >= stable_req:
                return curr_hash

            last_hash = curr_hash
            time.sleep(0.05)  # 50ms polling

        return last_hash or "unstable"

    def execute(
        self, envelope: CommandEnvelope, ui_state: UIState, ctrl_state: CtrlState
    ) -> Any:
        """Execute command via atomic units with barriers."""
        start_ts = time.time()
        effects = []

        # Handle Legacy CLI for Phase 1 compatibility
        if envelope.command_type == CommandType.CLI:
            cmd = envelope.parameters.get("cmd", "")
            rc, out, err = shell_cli.run(cmd)
            return {"exit_code": rc, "stdout": out, "stderr": err}

        # New Atomic Execution Path
        for i, step in enumerate(envelope.atomic_steps):
            # 1. EXECUTION BARRIER
            kill_engaged = self.kill_switch.engaged if self.kill_switch else False
            stop_reason = self.watchdog.guard(start_ts, i, kill_engaged)
            if stop_reason:
                return {"status": "stopped", "reason": stop_reason, "step_index": i, "effects": effects}

            # 2. PRE-SETTLE (Stable Hand)
            self._settle_by_convergence()

            # 3. ATOMIC EMIT
            effect = self._emit_atomic(step)
            effects.append(effect)

            # 4. POST-SETTLE & LOG BINDING
            final_hash = self._settle_by_convergence()
            # In Phase 2, this hash will be used to chain the audit log

        return {"status": "success", "effects": effects}

    def _emit_atomic(self, step: AtomicStep) -> Dict[str, Any]:
        """Low-level OS emission."""
        # This will be wired to actual Quartz/AX calls in Phase 2
        # For now, it's a trace of intent
        return {
            "type": step.type.value,
            "target": step.target,
            "params": step.parameters,
            "ts": time.time()
        }
