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
"""Append-only audit logger."""

from typing import Iterable

from .log_schema import AuditRecord


class AuditLogger:
    def __init__(self, sink):
        self.sink = sink  # sink must provide append(record)

    def append(self, record: AuditRecord) -> None:
        """Append record; sink is responsible for immutability and hash chaining."""
        if not self.sink:
            return
        self.sink.append(record)

    def stream(self) -> Iterable[AuditRecord]:
        """Return iterable over records in time order."""
        if not self.sink:
            return []
        return getattr(self.sink, "records", [])
