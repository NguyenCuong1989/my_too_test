"""Deterministic replay."""
from typing import Iterable, Any

from .log_schema import AuditRecord


def replay(records: Iterable[AuditRecord], armed: bool = False) -> Any:
    """Replay actions from audit log.

    - Requires environment + determinism hash match
    - Read-only unless armed=True and human-approved
    - Must not escalate permissions during replay
    """
    raise NotImplementedError("Phase 1 stub: replay logic to be implemented in Phase 2")
