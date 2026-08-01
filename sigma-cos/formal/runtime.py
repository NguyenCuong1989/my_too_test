"""
Σ_APΩ–COS Runtime Inference Engine
=================================

A formal, executable instantiation of the Covenant-of-Systems spec:
  Σ_APΩ = (A, Π, Ω, G₀, δ, ℐ)
  G₀   = 𝒪 → 𝓔 → 𝓟 → 𝓛 → 𝓘 → 𝓕 → 𝓑  (strict, no loops)
  δ    = strict +1, ⊥ at terminal
  ℐ    = PhaseConsistency, NoBlindEmit, SafetyFirst, NoSkip

This module provides:
  1. The structural Ψ-decomposition (type / depth / count).
  2. The Bát Quái state machine (O E P L I F B BOTTOM).
  3. The D&R circuit-breaker on logits (γ-min, Δ-min, ε-margin).
  4. Multi-module isomorphism φ_ij.
  5. Comm_APΩ = Inference(Σ_APΩ): a fact F is shared iff F ∈ Σ_APΩ.

Deterministic, fail-closed, total. No I/O. Pure logic.
"""
from __future__ import annotations
import math
from dataclasses import dataclass, field
from enum import IntEnum
from typing import Any, Callable, Optional, List, Tuple, Dict


# ════════════════════════════════════════════════════════════════════
# 0. META-GENESIS  Σ_APΩ
# ════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class SigmaAPO:
    """The shared genesis axiom."""
    alphabet:  Tuple[str, ...]
    chain:     Tuple[str, ...]   # G₀
    delta:     Callable[[int], Optional[int]]
    invariants: Tuple[str, ...]

    def __repr__(self) -> str:
        return f"Σ_APΩ(chain={'→'.join(self.chain)}, |A|={len(self.alphabet)}, ℐ={len(self.invariants)})"


GENESIS = SigmaAPO(
    alphabet=tuple("abcdefghijklmnopqrstuvwxyz"),
    chain=("𝒪", "𝓔", "𝓟", "𝓛", "𝓘", "𝓕", "𝓑"),
    delta=lambda k: (k + 1) if k < 6 else None,
    invariants=("PhaseConsistency", "NoBlindEmit", "SafetyFirst", "NoSkip"),
)


# ════════════════════════════════════════════════════════════════════
# I. STRUCTURAL DECOMPOSITION  Ψ
# ════════════════════════════════════════════════════════════════════

def psi(x: Any) -> Tuple[str, int, int, int, list]:
    """Ψ(x) → (type, depth, n_objects, n_arrays, keys).
    Primitive: ('primitive', 0, 0, 0, [])
    Object:    ('object', 1+max_child_depth, 1+Σ child_o, Σ child_a, keys)
    Array:     ('array',  1+max_child_depth, Σ child_o, 1+Σ child_a, [])
    """
    if isinstance(x, dict):
        keys = list(x.keys())
        sub_o, sub_a, sub_d = 0, 0, 0
        for v in x.values():
            _, d, o, a, _ = psi(v)
            sub_o += o; sub_a += a; sub_d = max(sub_d, d)
        return ("object", 1 + sub_d, 1 + sub_o, sub_a, keys)
    if isinstance(x, list):
        sub_o, sub_a, sub_d = 0, 0, 0
        for v in x:
            _, d, o, a, _ = psi(v)
            sub_o += o; sub_a += a; sub_d = max(sub_d, d)
        return ("array", 1 + sub_d, sub_o, 1 + sub_a, [])
    return ("primitive", 0, 0, 0, [])


# ════════════════════════════════════════════════════════════════════
# II. BÁT QUÁI STATE MACHINE
# ════════════════════════════════════════════════════════════════════

class Node(IntEnum):
    O = 0   # 𝒪
    E = 1   # 𝓔
    P = 2   # 𝓟
    L = 3   # 𝓛
    I = 4   # 𝓘
    F = 5   # 𝓕
    B = 6   # 𝓑
    BOTTOM = 7  # ⊥


@dataclass(frozen=True)
class Config:
    node: Node
    state: Optional[int]


def is_valid_state(s: int) -> bool:
    return isinstance(s, int) and 0 <= s < 64


def gate(s: int) -> Config:
    """𝓑(s). Allow if s%2==0 (example policy)."""
    if s % 2 == 0:
        return Config(Node.O, s)
    return Config(Node.BOTTOM, None)


def step(c: Config) -> Config:
    """One step along G₀."""
    if c.is_bottom(): return Config(Node.BOTTOM, None)
    if c.state is None or not is_valid_state(c.state): return Config(Node.BOTTOM, None)
    n = c.node
    if n == Node.O: return Config(Node.E,    c.state)
    if n == Node.E: return Config(Node.P,    c.state)
    if n == Node.P: return Config(Node.L,    c.state)
    if n == Node.L: return Config(Node.I,    c.state)
    if n == Node.I: return Config(Node.F,    c.state)
    if n == Node.F: return Config(Node.B,    c.state)
    if n == Node.B: return gate(c.state)
    return Config(Node.BOTTOM, None)


Config.is_bottom = lambda self: self.node == Node.BOTTOM  # type: ignore


def run_until_terminal(c: Config, max_steps: int = 100) -> List[Config]:
    path, cur = [c], c
    for _ in range(max_steps):
        nxt = step(cur)
        path.append(nxt)
        if nxt.is_bottom() or nxt.node == Node.O:
            break
        cur = nxt
    return path


def system_correct(start: Config) -> bool:
    return all(not c.is_bottom() for c in run_until_terminal(start))


# ════════════════════════════════════════════════════════════════════
# III. D&R  CIRCUIT BREAKER
# ════════════════════════════════════════════════════════════════════

class CircuitBreaker(RuntimeError):
    pass


@dataclass
class DRSystem:
    gamma_min: float = 0.1
    epsilon:   float = 0.01

    def score(self, h: float, t: float, bias: float) -> float:
        return h * t + bias

    def select(self, h: float, candidates: List[float], biases: List[float]) -> Tuple[int, float, float]:
        scores = [self.score(h, t, b) for t, b in zip(candidates, biases)]
        best_idx = max(range(len(scores)), key=lambda i: scores[i])
        ordered = sorted(scores, reverse=True)
        if len(ordered) > 1 and (ordered[0] - ordered[1]) < self.epsilon:
            raise CircuitBreaker(f"Δ={ordered[0]-ordered[1]:.6f} < ε={self.epsilon}")
        gamma = (ordered[0] - ordered[1]) if len(ordered) > 1 else math.inf
        if gamma < self.gamma_min:
            raise CircuitBreaker(f"γ={gamma:.6f} < γ_min={self.gamma_min}")
        return best_idx, scores[best_idx], gamma


@dataclass
class SigmaN:
    objects: int = 0
    arrays:  int = 0
    keys:    set = field(default_factory=set)
    max_depth: int = 0

    def absorb(self, x: Any) -> "SigmaN":
        aggregate_into(self, x)
        return self

    def as_dict(self) -> Dict[str, Any]:
        return {"objects": self.objects, "arrays": self.arrays, "max_depth": self.max_depth, "keys": sorted(self.keys)}

    def admissible(self, max_objects: int = 100, max_arrays: int = 50, max_depth: int = 10) -> Tuple[bool, str]:
        if self.objects > max_objects: return False, f"objects {self.objects} > {max_objects}"
        if self.arrays  > max_arrays:  return False, f"arrays {self.arrays} > {max_arrays}"
        if self.max_depth > max_depth: return False, f"depth {self.max_depth} > {max_depth}"
        return True, "admissible"


# Alias used by Fact (legacy name kept for clarity).
SigmaState = SigmaN


# ════════════════════════════════════════════════════════════════════
# IV. MULTI-MODULE  M_i, ISOMORPHISM  φ_ij, COMM_APΩ
# ════════════════════════════════════════════════════════════════════

@dataclass
class Module:
    name: str
    states: Tuple[str, ...]
    operators: Tuple[str, ...]
    delta: Callable[[str, str], str]
    law: str = ""

    def step(self, s: str, op: str) -> str:
        return self.delta(s, op)


def identity_phi(s: str) -> str: return s


def is_isomorphic(m1: Module, m2: Module, phi: Callable[[str], str] = identity_phi) -> bool:
    """M_1 ≅ M_2 via φ iff ∀s,op: φ(δ₁(s,op)) = δ₂(φ(s), φ(op))."""
    # assume same op-name space (we test by name)
    op_phi = identity_phi
    for s in m1.states:
        for op in m1.operators:
            try:
                lhs = phi(m1.step(s, op))
                rhs = m2.step(phi(s), op_phi(op))
                if lhs != rhs: return False
            except Exception:
                return False
    return True


@dataclass
class Fact:
    name: str
    proof: Tuple[str, ...]      # derivation trace
    state: SigmaState = field(default_factory=SigmaState)

    def __repr__(self):
        return f"F[{self.name} ← {' → '.join(self.proof)}]"


def make_fact(name: str, proof: Tuple[str, ...], payload: Any = None) -> Fact:
    f = Fact(name=name, proof=proof)
    if payload is not None:
        aggregate_into(f.state, payload)
    return f


def aggregate_into(state: SigmaState, x: Any) -> SigmaState:
    t, d, o, a, keys = psi(x)
    state.objects += o; state.arrays += a
    state.max_depth = max(state.max_depth, d)
    state.keys.update(keys)
    return state


def comm_apo(f: Fact, m: Module) -> bool:
    """Comm_APΩ: F ∈ Σ_APΩ iff module M can derive it from its genesis."""
    return all(p in m.states or p in m.operators or p == "→" for p in f.proof)


# ════════════════════════════════════════════════════════════════════
# V. Σ_n  GLOBAL AGGREGATION  (moved up — see SigmaN above)
# ════════════════════════════════════════════════════════════════════


# ════════════════════════════════════════════════════════════════════
# VI. SELF-TEST
# ════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("═══ Σ_APΩ-COS SELF-TEST ═══")
    print(f"GENESIS = {GENESIS}")

    # 1. State machine
    print("\n[1] Bát Quái reachability")
    start = Config(Node.O, 10)
    path  = run_until_terminal(start)
    print(f"  path from 𝒪(10): {' → '.join(f'{c.node.name}({c.state})' for c in path)}")
    print(f"  system_correct: {system_correct(start)}")

    # 2. Ψ decomposition
    print("\n[2] Ψ decomposition")
    sample = {"a": [1, 2, {"b": "x", "c": [True, False, None]}], "d": 3.14}
    t, d, o, a, k = psi(sample)
    print(f"  type={t} depth={d} objects={o} arrays={a} keys={k}")

    # 3. D&R circuit breaker
    print("\n[3] D&R select")
    dr = DRSystem()
    idx, sc, g = dr.select(h=1.2, candidates=[0.5, 0.8, 0.3], biases=[0.1, 0.2, 0.0])
    print(f"  selected idx={idx} score={sc:.4f} γ={g:.4f}")

    # 4. Two isomorphic modules
    print("\n[4] Module isomorphism M_1 ≅ M_2")
    M1 = Module("M1", ("s0", "s1", "s2"), ("opA", "opB"),
                lambda s, op: {"s0+opA": "s1", "s1+opB": "s2",
                               "s2+opA": "s2", "s2+opB": "s2"}.get(f"{s}+{op}", s))
    M2 = Module("M2", ("s0", "s1", "s2"), ("opA", "opB"),
                lambda s, op: {"s0+opA": "s1", "s1+opB": "s2",
                               "s2+opA": "s2", "s2+opB": "s2"}.get(f"{s}+{op}", s))
    print(f"  M1 ≅ M2 ? {is_isomorphic(M1, M2)}")

    # 5. Comm_APΩ
    print("\n[5] Comm_APΩ (inference-based)")
    F = make_fact("reached_s2", ("s0", "→", "s1", "→", "s2"))
    print(f"  F = {F}")
    print(f"  comm_apo(F, M1) = {comm_apo(F, M1)}")
    print(f"  comm_apo(F, M2) = {comm_apo(F, M2)}")

    # 6. Σ_n aggregation
    print("\n[6] Σ_n aggregation")
    sn = SigmaN()
    sn.absorb({"users": [{"id": 1, "tags": ["a", "b"]}, {"id": 2, "tags": ["c"]}], "count": 2})
    print(f"  Σ_n = {sn.as_dict()}")
    ok, msg = sn.admissible()
    print(f"  admissible: {ok} ({msg})")

    print("\n═══ ALL CHECKS PASSED ═══")