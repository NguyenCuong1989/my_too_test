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
"""Deterministic replay."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable, Optional

from .log_schema import AuditRecord
from core.Menh.Chung import compute_Chung


@dataclass
class ReplayResult:
    status: str
    stop_reason: Optional[str]
    verified_steps: int
    mismatch_at: Optional[int]
    evidence: dict


def replay(
    records: Iterable[AuditRecord],
    armed: bool = False,
    executor: Any = None,
    env_fingerprint: Optional[str] = None,
    verify_chain: bool = True,
) -> ReplayResult:
    """Replay actions from audit log.

    - Requires environment + determinism hash match
    - Read-only unless armed=True and human-approved
    - Must not escalate permissions during replay
    """
    verified_steps = 0
    previous_hash = None
    expected_env = env_fingerprint

    for idx, record in enumerate(records):
        if expected_env and record.timeline_id and record.timeline_id != expected_env:
            return ReplayResult(
                status="stopped",
                stop_reason="environment_mismatch",
                verified_steps=verified_steps,
                mismatch_at=idx,
                evidence={"record_timeline_id": record.timeline_id, "expected": expected_env},
            )

        expected_chung = compute_Chung(
            record.state_before,
            record.intent,
            record.command,
            record.policy_decision.get("verdict") if isinstance(record.policy_decision, dict) else record.policy_decision,
            prev_Chung=record.chained_hash,
        )
        if record.Chung != expected_chung:
            return ReplayResult(
                status="stopped",
                stop_reason="chung_mismatch",
                verified_steps=verified_steps,
                mismatch_at=idx,
                evidence={"expected": expected_chung, "actual": record.Chung},
            )

        if verify_chain:
            if record.hash_prev != previous_hash:
                return ReplayResult(
                    status="stopped",
                    stop_reason="hash_chain_break",
                    verified_steps=verified_steps,
                    mismatch_at=idx,
                    evidence={"expected_prev": previous_hash, "actual_prev": record.hash_prev},
                )
            previous_hash = record.hash_curr

        if armed and executor is not None:
            executor(record)

        verified_steps += 1

    return ReplayResult(
        status="verified",
        stop_reason=None,
        verified_steps=verified_steps,
        mismatch_at=None,
        evidence={"armed": armed, "verify_chain": verify_chain},
    )
