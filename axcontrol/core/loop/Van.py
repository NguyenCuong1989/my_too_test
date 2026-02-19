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
Control loop (safe, deterministic, simulated).

Runs observe -> decide -> emit -> verify with TAB-only actions in simulation mode.
Real macOS integrations can replace observer/emitter while keeping interfaces.
"""

import time
from typing import Optional

from adapters.macos_ax import observer
from core.Chinh.command import CommandEnvelope, CommandType
from core.Chinh.intent import Intent, IntentSource
from core.Chinh.llm_strategy import suggest_intent
from core.Chinh.policy import PolicyVerdict, PolicyOutcome
from core.Luat.evaluator import PolicyEvaluator
from core.Menh.rate_limit import RateLimiter
from core.Menh.stop_reasons import StopReason
from core.Menh.Chung import compute_Chung
from core.canon.existence_state import ExistenceState
from core.canon.existence_state_map import EXISTENCE_STATE_MAP
from core.The.state_projector import map_state_to_hexagram
from core.Chung.log_schema import AuditRecord
from core.Chung.logger import AuditLogger
from core.observability import trace
from input.keyboard import emit_tab
from apps import finder, safari, system_settings, notes


class ControlLoop:
    def __init__(self):
        self.rate_limiter = RateLimiter(min_interval_ms=200)
        self.policy = PolicyEvaluator(rules={})
        self.logger = AuditLogger(sink=_InMemorySink())
        self.locked_state_proof = None

    def _select_app_policy(self, app: str):
        if app == "Finder":
            return finder.allow_action
        if app == "Safari":
            return safari.allow_action
        if app == "System Settings":
            return system_settings.allow_action
        if app == "Notes":
            return notes.allow_action
        return lambda role, action, label=None: True  # safe fallback: allow TAB-only checked later

    def _intent_from_llm(self, snap_app: str, snap_role: str):
        ctx = {"app": snap_app, "role": snap_role}
        intent = suggest_intent(ctx)
        if intent:
            trace.emit(self.logger.sink, trace.LLM_INTENT, {"intent": intent.intent_id, "ctx": ctx})
        return intent

    def run_once(self) -> Optional[StopReason]:
        snap = observer.observe()
        if snap is None:
            return StopReason.AX_LOST

        state_proof = f"{snap.app}:{snap.role}:{snap.label}"

        # Freeze Point #1: lexicon + state proof lock
        if self.locked_state_proof is not None and state_proof != self.locked_state_proof:
            return StopReason.CAUSALITY_VIOLATION

        # Existence filter (R-32): map to hexagram and classify
        hex_bits = map_state_to_hexagram(snap)
        existence = EXISTENCE_STATE_MAP.get(hex_bits, ExistenceState.DIET)
        if existence in {ExistenceState.TU, ExistenceState.DIET}:
            return StopReason.ONTOLOGICAL_VIOLATION

        app_policy = self._select_app_policy(snap.app)

        # Build intent (LLM optional, fallback deterministic)
        intent = self._intent_from_llm(snap.app, snap.role) or Intent(
            intent_id="fallback-tab",
            goal="safe_tab_navigation",
            parameters={"action": "TAB"},
            source=IntentSource.HUMAN,
        )

        # Build command envelope (TAB-only)
        envelope = CommandEnvelope(
            command_id=str(time.time()),
            intent_id=intent.intent_id,
            command_type=CommandType.NAVIGATE,
            parameters={"action": "TAB"},
            normalized_state_hash=state_proof,
            policy_context={},
            signature="simulated",
        )

        # Policy evaluation via app policy
        if snap.app == "Notes":
            allowed, stop_reason = app_policy(snap.role, "TAB", snap.label)
        elif snap.app == "Safari":
            allowed = app_policy(snap.role, snap.label, "TAB")
            stop_reason = None
        else:
            allowed = app_policy(snap.role, "TAB", snap.label)
            stop_reason = None
        verdict = PolicyVerdict(PolicyOutcome.ALLOW if allowed else PolicyOutcome.DENY, reason=stop_reason)

        if verdict.outcome == PolicyOutcome.DENY:
            self._log_step(snap, intent, envelope, verdict, stop_reason or StopReason.POLICY_DENIAL.value, state_proof, hex_bits)
            return StopReason(stop_reason) if stop_reason else StopReason.POLICY_DENIAL

        # Rate limit
        if not self.rate_limiter.allow():
            self._log_step(snap, intent, envelope, verdict, StopReason.TIMING_VIOLATION.value, state_proof, hex_bits)
            return StopReason.TIMING_VIOLATION

        # Emit TAB
        # Freeze Point #2: lock state before emit
        self.locked_state_proof = state_proof

        emit_tab()
        trace.emit(self.logger.sink, trace.COMMAND_EXECUTED, {"command_id": envelope.command_id})

        # Mid-step drift check (post emit)
        snap_after = observer.observe()
        if snap_after is None:
            self._log_step(snap, intent, envelope, verdict, StopReason.AX_LOST.value, state_proof, hex_bits)
            return StopReason.AX_LOST
        after_proof = f"{snap_after.app}:{snap_after.role}:{snap_after.label}"
        if after_proof != state_proof:
            drift_hex = map_state_to_hexagram(snap_after)
            self._log_step(snap_after, intent, envelope, verdict, StopReason.STATE_DRIFT_MID_STEP.value, after_proof, drift_hex)
            return StopReason.STATE_DRIFT_MID_STEP

        self._log_step(snap_after, intent, envelope, verdict, None, state_proof, hex_bits)
        return None

    def _log_step(self, snap, intent, envelope, verdict, stop_reason, state_proof, hex_bits):
        effect = {"emitted": "TAB" if verdict.outcome == PolicyOutcome.ALLOW else "DENY"}
        record = AuditRecord(
            timestamp=time.time(),
            state_before={"app": snap.app, "role": snap.role, "label": snap.label},
            intent=intent.__dict__,
            command=envelope.__dict__,
            policy_decision=verdict.__dict__,
            state_after={"app": snap.app, "role": snap.role, "label": snap.label},
            Chung=compute_Chung(
                state_proof,
                intent.__dict__,
                envelope.__dict__,
                effect,
            ),
            stop_reason=stop_reason,
            hex_bits=hex_bits,
        )
        self.logger.append(record)


class _InMemorySink:
    def __init__(self):
        self.records = []

    def append(self, record):
        self.records.append(record)

    def write(self, trace_event):
        self.records.append({"trace": trace_event})


def run(iterations: int = 5):
    loop = ControlLoop()
    for _ in range(iterations):
        stop = loop.run_once()
        if stop in {StopReason.POLICY_DENIAL, StopReason.TEXT_EDIT_BLOCKED, StopReason.AX_LOST, StopReason.APP_SWITCH}:
            print(f"[STOP] {stop}")
            break
    return loop.logger.sink.records
