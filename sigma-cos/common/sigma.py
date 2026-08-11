"""
Σ-aggregator. Counts objects/arrays/keys/depth in a JSON-like value.
Used to validate constraints and to compute Σ_n.
"""
from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class SigmaState:
    objects: int = 0
    arrays: int = 0
    keys: set = field(default_factory=set)
    max_depth: int = 0


def psi(x) -> tuple:
    """Ψ operator. Returns (type, depth, count_o, count_a, keys)."""
    if isinstance(x, dict):
        keys = list(x.keys())
        sub_o, sub_a, sub_d = 0, 0, 0
        for k, v in x.items():
            t, d, o, a, _ = psi(v)
            sub_o += o
            sub_a += a
            sub_d = max(sub_d, d)
        return ("object", 1 + sub_d, 1 + sub_o, sub_a, keys)
    if isinstance(x, list):
        sub_o, sub_a, sub_d = 0, 0, 0
        for v in x:
            t, d, o, a, _ = psi(v)
            sub_o += o
            sub_a += a
            sub_d = max(sub_d, d)
        return ("array", 1 + sub_d, sub_o, 1 + sub_a, [])
    return ("primitive", 0, 0, 0, [])


def aggregate(state: SigmaState, x) -> SigmaState:
    t, d, o, a, keys = psi(x)
    state.objects += o
    state.arrays += a
    state.max_depth = max(state.max_depth, d)
    state.keys.update(keys)
    return state


def validate(state: SigmaState, constraints: dict) -> tuple[bool, str]:
    mo = constraints.get("max_objects", 100)
    ma = constraints.get("max_arrays", 50)
    md = constraints.get("max_depth", 10)
    if state.objects > mo:
        return False, f"too many objects: {state.objects} > {mo}"
    if state.arrays > ma:
        return False, f"too many arrays: {state.arrays} > {ma}"
    if state.max_depth > md:
        return False, f"too deep: {state.max_depth} > {md}"
    return True, "ok"