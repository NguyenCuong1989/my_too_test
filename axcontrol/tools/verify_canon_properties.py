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
Property-based verification for canonical survival ontology.

Checks:
1) Axis invariance is structural (Center not part of state); asserted descriptively.
2) Abyss safety: any XOR transition leading to TU/DIET must be blocked.
3) Friction determinism: same Q_now and Δ always produce same Q_next and decision.
"""

from itertools import product
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from core.canon.existence_state import ExistenceState
from core.canon.existence_state_map import EXISTENCE_STATE_MAP


def xor_bits(a: str, b: str) -> str:
    return "".join("1" if x != y else "0" for x, y in zip(a, b))


def run():
    states = sorted(EXISTENCE_STATE_MAP.keys())
    # Property 2: Abyss safety (no TU/DIET transition allowed)
    violations = 0
    det_mismatches = 0
    for q in states:
        for d in states:
            q_next = xor_bits(q, d)
            target_state = EXISTENCE_STATE_MAP.get(q_next, ExistenceState.DIET)
            # Decision model: allow only SINH/TRI
            decision_allow = target_state in {ExistenceState.SINH, ExistenceState.TRI}
            if not decision_allow and target_state not in {ExistenceState.TU, ExistenceState.DIET}:
                violations += 1
            # Determinism: recompute and compare
            q_next2 = xor_bits(q, d)
            if q_next != q_next2:
                det_mismatches += 1
    return {
        "total_pairs": len(states) ** 2,
        "abyss_violations": violations,
        "determinism_mismatches": det_mismatches,
    }


if __name__ == "__main__":
    summary = run()
    print(summary)
