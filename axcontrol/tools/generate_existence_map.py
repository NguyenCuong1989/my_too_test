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
from itertools import product
from pathlib import Path
from typing import Dict, Tuple
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from core.canon.existence_state import ExistenceState

Hexagram = Tuple[int, int, int, int, int, int]


def is_canonical(q: Hexagram) -> bool:
    return len(q) == 6 and all(bit in (0, 1) for bit in q)


def is_tu(q: Hexagram) -> bool:
    # ∀ i ∈ {2,3,4,5}, hᵢ = 0
    return all(q[i] == 0 for i in (1, 2, 3, 4))


def is_sinh(q: Hexagram) -> bool:
    # ∃ i ∈ {2,3,4,5}, hᵢ = 1 and Internal ≥ External
    if not any(q[i] == 1 for i in (1, 2, 3, 4)):
        return False
    internal = sum(q[i] for i in (0, 1, 2))
    external = sum(q[i] for i in (3, 4, 5))
    return internal >= external


def classify(q: Hexagram) -> ExistenceState:
    if not is_canonical(q):
        return ExistenceState.DIET
    if is_tu(q):
        return ExistenceState.TU
    if is_sinh(q):
        return ExistenceState.SINH
    return ExistenceState.TRI


def generate_map() -> Dict[str, ExistenceState]:
    mapping: Dict[str, ExistenceState] = {}
    for bits in product([0, 1], repeat=6):
        key = "".join(str(b) for b in bits)
        mapping[key] = classify(bits)
    assert len(mapping) == 64
    assert all(len(k) == 6 for k in mapping)
    return mapping


def main():
    mapping = generate_map()
    lines = [
        "# =============================================================================",
        "# PROJECT: CANON-TO-SYSTEM DETERMINISTIC PROJECTION",
        "# METHOD: D&R PROTOCOL (CLOSED)",
        "#",
        "# ORIGINATOR / CREATOR:",
        "#   alpha_prime_omega",
        "#",
        "# LEGAL ONTOLOGY:",
        "#   This source file is a deterministic projection of a closed Canon.",
        "#   Removal or alteration of this header voids legal and ontological validity.",
        "#",
        "# STATUS:",
        "#   GENERATED — NON-AUTONOMOUS — NON-OWNERLESS",
        "#",
        "# TRACEABILITY:",
        "#   Canon -> COG -> Projection(Π) -> Artifact",
        "#",
        "# =============================================================================",
        "\"\"\"Auto-generated existence state map (64 hexagrams). Do not edit by hand.\"\"\"",
        "from core.canon.existence_state import ExistenceState",
        "",
        "EXISTENCE_STATE_MAP = {",
    ]
    for key, state in sorted(mapping.items()):
        lines.append(f'    "{key}": ExistenceState.{state.name},')
    lines.append("}")
    lines.append("")
    lines.append("assert len(EXISTENCE_STATE_MAP) == 64")
    lines.append("assert all(len(k) == 6 for k in EXISTENCE_STATE_MAP)")

    target = Path(__file__).resolve().parents[1] / "core" / "canon" / "existence_state_map.py"
    target.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {target}")


if __name__ == "__main__":
    main()
