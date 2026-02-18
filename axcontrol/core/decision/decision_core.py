"""Decision Core — single authority.

Translates intent + state into signed command envelopes, applying policy checks in deterministic order.
Execution is performed elsewhere; this module never emits UI actions.
"""
from typing import Tuple

from .intent import Intent
from .command import CommandEnvelope
from .policy import PolicyVerdict, PolicyOutcome


class DecisionCore:
    def __init__(self, policy_evaluator, signer):
        self.policy_evaluator = policy_evaluator
        self.signer = signer

    def evaluate_intent(self, intent: Intent, normalized_state_hash: str) -> Tuple[CommandEnvelope, PolicyVerdict]:
        """Produce command envelope and policy verdict.

        Deterministic ordering:
        1) Build candidate envelope from finite command set.
        2) Evaluate policy.
        3) Sign envelope only if allowed.
        """
        raise NotImplementedError("Phase 1 stub: decision logic to be implemented in Phase 2")
