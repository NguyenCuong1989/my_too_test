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
