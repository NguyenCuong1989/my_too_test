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
Trace utilities and event names.

All executions emit structured traces to feed audit log and status surfaces.
"""

LLM_DECISION = "LLM_DECISION"
LLM_INTENT = "LLM_INTENT"
COMMAND_EXECUTED = "COMMAND_EXECUTED"
STOP_TRIGGERED = "STOP_TRIGGERED"
REPLAY_EVENT = "REPLAY_EVENT"


def emit(trace_sink, event_type: str, payload: dict) -> None:
    """
    Minimal trace emitter; sink is responsible for persistence/ordering.
    """
    if trace_sink is None:
        return
    trace_sink.write({"type": event_type, "payload": payload})
