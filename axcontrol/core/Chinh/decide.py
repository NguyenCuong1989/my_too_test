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
"""Decision orchestration helper."""

from core.Chinh.decision_core import DecisionCore
from core.Luat.evaluator import PolicyEvaluator


def build_decider(policy_rules):
    evaluator = PolicyEvaluator(policy_rules)
    return DecisionCore(policy_evaluator=evaluator, signer=_noop_signer)


def _noop_signer(envelope):
    return envelope
