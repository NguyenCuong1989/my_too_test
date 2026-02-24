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

from typing import Dict, Any
from ..Chinh.command import CommandEnvelope
from ..Chinh.policy import PolicyVerdict, PolicyOutcome


class PolicyEvaluator:
    def __init__(self, rules: Dict[str, Any]):
        self.rules = rules

    def evaluate(self, envelope: CommandEnvelope, context: Any) -> PolicyVerdict:
        """Return PolicyVerdict; denial is terminal for this command.

        Deterministic rule cascading:
        1) App Whitelist
        2) Action Whitelist
        3) (Future) Time Guards & Rate Limits
        """
        # Context might be raw string hash or CtrlState
        # For simulation, we rely on parameters in the envelope
        action = envelope.parameters.get("action")

        # 1. App Whitelist check (using normalized state context)
        # Normalized state hash format: "App:Role:Label"
        if isinstance(context, str) and ":" in context:
            app_name = context.split(":")[0]
            allowed_apps = self.rules.get("allowed_apps")
            if allowed_apps and app_name not in allowed_apps:
                return PolicyVerdict(
                    outcome=PolicyOutcome.DENY, reason=f"app_forbidden:{app_name}"
                )

        # 2. Action Whitelist (Simulation Safety)
        allowed_actions = self.rules.get("allowed_actions", {"TAB"})
        if action not in allowed_actions:
            return PolicyVerdict(
                outcome=PolicyOutcome.DENY, reason=f"action_forbidden:{action}"
            )

        return PolicyVerdict(outcome=PolicyOutcome.ALLOW, reason=None)
