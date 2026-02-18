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
            normalized_state_hash=f"{snap.app}:{snap.role}:{snap.label}",
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
            self._log_step(snap, intent, envelope, verdict, stop_reason or StopReason.POLICY_DENIAL.value)
            return StopReason(stop_reason) if stop_reason else StopReason.POLICY_DENIAL

        # Rate limit
        if not self.rate_limiter.allow():
            self._log_step(snap, intent, envelope, verdict, StopReason.TIMING_VIOLATION.value)
            return StopReason.TIMING_VIOLATION

        # Emit TAB
        emit_tab()
        trace.emit(self.logger.sink, trace.COMMAND_EXECUTED, {"command_id": envelope.command_id})

        self._log_step(snap, intent, envelope, verdict, None)
        return None

    def _log_step(self, snap, intent, envelope, verdict, stop_reason):
        effect = {"emitted": "TAB" if verdict.outcome == PolicyOutcome.ALLOW else "DENY"}
        record = AuditRecord(
            timestamp=time.time(),
            state_before={"app": snap.app, "role": snap.role, "label": snap.label},
            intent=intent.__dict__,
            command=envelope.__dict__,
            policy_decision=verdict.__dict__,
            state_after={"app": snap.app, "role": snap.role, "label": snap.label},
            Chung=compute_Chung(
                {"app": snap.app, "role": snap.role, "label": snap.label},
                intent.__dict__,
                envelope.__dict__,
                effect,
            ),
            stop_reason=stop_reason,
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
