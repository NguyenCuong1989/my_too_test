"""Decision orchestration helper."""

from core.Chinh.decision_core import DecisionCore
from core.Luat.evaluator import PolicyEvaluator


def build_decider(policy_rules):
    evaluator = PolicyEvaluator(policy_rules)
    return DecisionCore(policy_evaluator=evaluator, signer=_noop_signer)


def _noop_signer(envelope):
    return envelope
