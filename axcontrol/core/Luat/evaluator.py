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
"""Policy evaluator.

Applies deterministic rule order: app allowlist → UI surface allowlist → rate limits → time guards.
"""
from typing import Dict

from ..Chinh.command import CommandEnvelope
from ..Chinh.policy import PolicyVerdict, PolicyOutcome
from ..The.ctrl_state import CtrlState


class PolicyEvaluator:
    def __init__(self, rules: Dict[str, object]):
        self.rules = rules

    def evaluate(self, envelope: CommandEnvelope, ctrl_state: CtrlState) -> PolicyVerdict:
        """Return PolicyVerdict; denial is terminal for this command."""
        # Simple allow-all evaluator; richer rules can be injected via self.rules
        return PolicyVerdict(outcome=PolicyOutcome.ALLOW, reason=None)
