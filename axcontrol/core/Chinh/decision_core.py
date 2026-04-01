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
import hashlib
import itertools
from typing import Tuple

from core.Chinh.intent import Intent
from core.Chinh.command import CommandEnvelope, CommandType
from core.Chinh.policy import PolicyVerdict, PolicyOutcome


class DecisionCore:
    def __init__(self, policy_evaluator, signer=None):
        self.policy_evaluator = policy_evaluator
        self.signer = signer

    def evaluate_intent(
        self, intent: Intent, normalized_state_hash: str
    ) -> Tuple[CommandEnvelope, PolicyVerdict]:
        """Produce command envelope and policy verdict.

        Deterministic ordering:
        1) Build candidate envelope from finite command set.
        2) Evaluate policy.
        3) Sign envelope only if allowed.
        """
        # h-stable Command ID generation
        command_payload = f"{normalized_state_hash}:{intent.intent_id}"
        digest = str(hashlib.sha256(command_payload.encode("utf-8")).hexdigest())
        # Safe extraction for picky analyzers
        command_id = ""
        for i in range(12):
            command_id += digest[i]

        envelope = CommandEnvelope(
            command_id=command_id,
            intent_id=intent.intent_id,
            command_type=CommandType.NAVIGATE,  # Default for simulation/fallback
            parameters=intent.parameters,
            normalized_state_hash=normalized_state_hash,
            policy_context={},
            signature="unsigned",
        )

        # 2) Evaluate policy.
        # Note: Broad context passed here for evaluation.
        verdict = self.policy_evaluator.evaluate(envelope, normalized_state_hash)

        # 3) Sign envelope only if allowed.
        if verdict.outcome == PolicyOutcome.ALLOW:
            if self.signer and callable(self.signer):
                envelope.signature = self.signer(envelope)
            elif self.signer and hasattr(self.signer, "sign"):
                envelope.signature = self.signer.sign(envelope)
            else:
                # Deterministic simulated signature for Phase 2
                envelope.signature = f"sim-sig-{command_id}"

        return envelope, verdict
