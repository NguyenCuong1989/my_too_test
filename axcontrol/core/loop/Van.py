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
from core.canon.existence_state import ExistenceState
from core.canon.existence_state_map import EXISTENCE_STATE_MAP
from core.The.state_projector import map_state_to_hexagram
from core.Chung.logger import AuditLogger
from core.Chung.log_schema import AuditRecord
from core.Menh.Chung import compute_Chung
from core.observability import trace
from input.keyboard import emit_tab
from apps import finder, safari, system_settings, notes


class _InMemorySink:
    def __init__(self):
        self.records = []

    def write(self, record):
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
        self, snap, intent, envelope, verdict, stop_reason, state_hash, hex_bits
    ):
        record = AuditRecord(
            Chung=compute_Chung(state_hash, envelope.command_id),
            timestamp=time.time(),
            app=snap.app,
            role=snap.role,
            hexagram=hex_bits,
            intent_id=intent.intent_id,
            command_id=envelope.command_id,
            verdict=verdict.outcome.value,
            stop_reason=stop_reason,
        )
        self.logger.log(record)

    def run_once(self) -> Optional[StopReason]:
        # 1. Observation
        raw_snap = observer.observe()
        if raw_snap is None:
            return StopReason.AX_LOST

        # 2. Normalization (Determinism Anchor)
        ui_state = normalize_ui_state(raw_snap)
        state_hash = ui_state.hash

        # h-Causality check
        if self.locked_state_hash is not None and state_hash != self.locked_state_hash:
            return StopReason.CAUSALITY_VIOLATION

        # 3. Existence Verification (R-32)
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

        # 5. App-specific secondary check (Unified Interface)
        app_policy = self._select_app_policy(raw_snap.app)
        allowed, stop_reason = app_policy(raw_snap.role, "TAB", raw_snap.label)

        if not allowed or verdict.outcome == PolicyOutcome.DENY:
            final_stop = (
                StopReason(stop_reason) if stop_reason else StopReason.POLICY_DENIAL
            )
            self._log_step(
                raw_snap,
                intent,
                envelope,
                verdict,
                final_stop.value,
                state_hash,
                hex_bits,
            )
            return final_stop

        # 6. Safety Guards (Rate limiting)
        if not self.rate_limiter.allow():
            return StopReason.TIMING_VIOLATION

        # 7. Execution (Emit)
        self.locked_state_hash = state_hash  # Lock state before commit
        emit_tab()

        # 8. Post-Check (Drift detection)
        snap_after = observer.observe()
        if snap_after:
            ui_after = normalize_ui_state(snap_after)
            if ui_after.hash != state_hash:
                # Drift detected
                self._log_step(
                    snap_after,
                    intent,
                    envelope,
                    verdict,
                    StopReason.STATE_DRIFT_MID_STEP.value,
                    state_hash,
                    hex_bits,
                )
                return StopReason.STATE_DRIFT_MID_STEP

        self._log_step(raw_snap, intent, envelope, verdict, None, state_hash, hex_bits)
        return None
