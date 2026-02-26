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
"""
The main control loop (Van) for the axcontrol system.
"""

import time
from typing import Optional

from adapters.macos_ax import observer
from core.Chinh.decision_core import DecisionCore
from core.Chinh.intent import Intent, IntentSource
from core.Chinh.llm_strategy import suggest_intent
from core.Chinh.policy import PolicyOutcome
from core.Luat.evaluator import PolicyEvaluator
from core.The.normalize import normalize_ui_state
from core.The.ctrl_state import CtrlState, SessionStatus
from core.Menh.rate_limit import RateLimiter
from core.Menh.stop_reasons import StopReason
from core.Menh.Diet import KillSwitch
from core.canon.existence_state import ExistenceState
from core.canon.existence_state_map import EXISTENCE_STATE_MAP
from core.The.state_projector import map_state_to_hexagram
from core.Chung.logger import AuditLogger
from core.Chung.log_schema import AuditRecord
from core.Menh.Chung import compute_Chung
from core.Van.AnLenh import Executor
from core.Van.watchdog import Watchdog
from core.observability import trace
from input.keyboard import emit_tab
from apps import finder, safari, system_settings, notes


class _InMemorySink:
    def __init__(self):
        self.records = []

    def append(self, record):
        self.records.append(record)


class ControlLoop:
    def __init__(self):
        self.rate_limiter = RateLimiter(min_interval_ms=200)
        # Initialize with standard rules
        self.policy_evaluator = PolicyEvaluator(
            rules={
                "allowed_apps": {
                    "Finder",
                    "Safari",
                    "System Settings",
                    "Notes",
                    "Terminal",
                },
                "allowed_actions": {"TAB"},
            }
        )
        self.decision_core = DecisionCore(policy_evaluator=self.policy_evaluator)
        self.logger = AuditLogger(sink=_InMemorySink())
        self.ctrl_state = CtrlState(status=SessionStatus.ARMED)
        self.locked_state_hash = None
        self.prev_Chung = None  # Chain seed

        # R-03: Atomic Execution Layer
        self.kill_switch = KillSwitch()
        self.watchdog = Watchdog(max_duration_ms=5000, max_events=100)
        self.executor = Executor(
            ax_bridge=None,
            event_emitter=None,
            watchdog=self.watchdog,
            kill_switch=self.kill_switch,
        )

    def _select_app_policy(self, app: str):
        if app == "Finder":
            return finder.allow_action
        if app == "Safari":
            return safari.allow_action
        if app == "System Settings":
            return system_settings.allow_action
        if app == "Notes":
            return notes.allow_action
        return lambda role, action, label=None: (True, None)

    def _intent_from_llm(self, snap_app: str, snap_role: str):
        ctx = {"app": snap_app, "role": snap_role}
        intent = suggest_intent(ctx)
        if intent:
            trace.emit(
                self.logger.sink,
                trace.LLM_INTENT,
                {"intent": intent.intent_id, "ctx": ctx},
            )
        return intent

    def _log_step(
        self,
        snap,
        intent,
        envelope,
        verdict,
        stop_reason,
        state_hash,
        hex_bits,
        effect=None,
        step_index=0,
        override_flag=False,
        kill_switch_active=False,
        evidence_level=2,
    ):
        current_Chung = compute_Chung(
            state_hash,
            intent.intent_id,
            envelope.command_id,
            effect or verdict.outcome.value,
            prev_Chung=self.prev_Chung,
        )
        record = AuditRecord(
            timestamp=time.time(),
            state_before={"app": snap.app, "role": snap.role},
            intent={"intent_id": intent.intent_id},
            command={"command_id": envelope.command_id},
            policy_decision={"verdict": verdict.outcome.value},
            state_after={},
            Chung=current_Chung,
            step_index=step_index,
            chained_hash=self.prev_Chung,
            stop_reason=stop_reason,
            hex_bits=hex_bits,
            override_flag=override_flag,
            kill_switch_active=kill_switch_active,
            evidence_level=evidence_level,
        )
        self.logger.log(record)
        self.prev_Chung = current_Chung  # Chain it

    def _settle(self, timeout_ms: int = 1000, stable_req: int = 3) -> Optional[str]:
        """Wait until UIState.hash is stable. Returns None if AX_LOST during entire window."""
        last_hash = None
        stable_count = 0
        start_ts = time.time()
        was_ever_observed = False

        while (time.time() - start_ts) * 1000 < timeout_ms:
            raw = observer.observe()
            if not raw:
                time.sleep(0.05)
                continue

            was_ever_observed = True
            curr_hash = normalize_ui_state(raw).hash

            if curr_hash == last_hash:
                stable_count += 1
            else:
                stable_count = 0

            if stable_count >= stable_req:
                return curr_hash

            last_hash = curr_hash
            time.sleep(0.05)

        if not was_ever_observed:
            return None # AX_LOST signal
        return "unstable"

    def run_once(self) -> Optional[StopReason]:
        # 1. Settle & Observation (R-03 Formalization)
        state_hash = self._settle()
        if state_hash is None:
            return StopReason.AX_LOST
        if state_hash == "unstable":
            return StopReason.TIMING_VIOLATION

        raw_snap = observer.observe()
        if raw_snap is None:
            # Race condition: lost right after settle
            return StopReason.AX_LOST

        # 2. Normalization (Determinism Anchor)
        ui_state = normalize_ui_state(raw_snap)
        # Ensure we use the hash we settled on
        state_hash = ui_state.hash

        # h-Causality check
        if self.locked_state_hash is not None and state_hash != self.locked_state_hash:
            return StopReason.CAUSALITY_VIOLATION

        # 3. Existence Verification
        hex_bits = map_state_to_hexagram(raw_snap)
        existence = EXISTENCE_STATE_MAP.get(hex_bits, ExistenceState.DIET)
        if existence in {ExistenceState.TU, ExistenceState.DIET}:
            return StopReason.ONTOLOGICAL_VIOLATION

        # 4. Intent & Decision
        intent = self._intent_from_llm(raw_snap.app, raw_snap.role) or Intent(
            intent_id="fallback-tab",
            goal="safe_tab_navigation",
            parameters={"action": "TAB"},
            source=IntentSource.HUMAN,
        )

        # Authority Delegation (Decision Core)
        envelope, verdict = self.decision_core.evaluate_intent(intent, state_hash)

        # 5. App-specific secondary check
        app_policy = self._select_app_policy(raw_snap.app)
        allowed, stop_reason = app_policy(raw_snap.role, "TAB", raw_snap.label)

        if not allowed or verdict.outcome == PolicyOutcome.DENY:
            final_stop = (
                StopReason(stop_reason) if stop_reason else StopReason.POLICY_DENIAL
            )
            self._log_step(
                raw_snap, intent, envelope, verdict, final_stop.value, state_hash, hex_bits
            )
            return final_stop

        # 6. Safety Guards (Rate limiting)
        if not self.rate_limiter.allow():
            return StopReason.TIMING_VIOLATION

        # 7. Execution (Atomic Loop)
        self.locked_state_hash = state_hash  # Lock state before commit

        result = self.executor.execute(envelope, ui_state, self.ctrl_state)

        # 8. Post-Check & Logging Atomic Effects
        if result["status"] == "stopped":
            is_kill = (result["reason"] == StopReason.KILL_SWITCH)
            self._log_step(
                raw_snap,
                intent,
                envelope,
                verdict,
                result["reason"].value if hasattr(result["reason"], "value") else result["reason"],
                state_hash,
                hex_bits,
                step_index=result["step_index"],
                override_flag=is_kill,
                kill_switch_active=is_kill,
                evidence_level=1 if is_kill else 2,
            )
            return result["reason"]

        for i, effect in enumerate(result.get("effects", [])):
            # If effect is a UI emission, it's Level 1 Sovereignty evidence
            is_ui = effect.get("type", "").startswith("AX_") or effect.get("type", "").startswith("KEY_")
            self._log_step(
                raw_snap,
                intent,
                envelope,
                verdict,
                None,
                state_hash,
                hex_bits,
                effect=effect,
                step_index=i,
                evidence_level=1 if is_ui else 2,
            )

        # Final Drift Check
        snap_after = observer.observe()
        if snap_after:
            ui_after = normalize_ui_state(snap_after)
            if ui_after.hash != state_hash:
                return StopReason.STATE_DRIFT_MID_STEP

        return None
