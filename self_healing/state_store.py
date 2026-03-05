"""
State Store

Provides persistent state management for the self-healing framework,
enabling state restoration after failures or restarts.
"""

from __future__ import annotations

import json
import logging
import time
from pathlib import Path
from typing import Any


logger = logging.getLogger(__name__)


class StateStore:
    """
    JSON-backed key-value store for organism state.

    Thread-safety note: this implementation is designed for single-
    process use within an asyncio event loop.  For multi-process
    deployments, replace the backend with a proper database.
    """

    def __init__(self, path: Path | str = "data/organism_state.json") -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._data: dict[str, Any] = {}
        self._load()

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def _load(self) -> None:
        if self.path.exists():
            try:
                self._data = json.loads(self.path.read_text(encoding="utf-8"))
                logger.debug("State loaded from %s (%d keys)", self.path, len(self._data))
            except (json.JSONDecodeError, OSError) as exc:
                logger.warning("Could not load state from %s: %s", self.path, exc)
                self._data = {}

    def save(self) -> None:
        """Persist current in-memory state to disk."""
        try:
            self.path.write_text(
                json.dumps(self._data, indent=2, default=str),
                encoding="utf-8",
            )
        except OSError as exc:
            logger.error("Could not save state: %s", exc)

    # ------------------------------------------------------------------
    # CRUD
    # ------------------------------------------------------------------

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    def set(self, key: str, value: Any, *, auto_save: bool = True) -> None:
        self._data[key] = value
        if auto_save:
            self.save()

    def delete(self, key: str, *, auto_save: bool = True) -> None:
        self._data.pop(key, None)
        if auto_save:
            self.save()

    def all_keys(self) -> list[str]:
        return list(self._data.keys())

    # ------------------------------------------------------------------
    # Subsystem snapshots
    # ------------------------------------------------------------------

    def snapshot_subsystem(self, name: str, data: dict) -> None:
        """Persist a point-in-time snapshot of a subsystem's state."""
        snapshots = self._data.setdefault("snapshots", {})
        snapshots.setdefault(name, []).append({"ts": time.time(), **data})
        # Rolling window
        if len(snapshots[name]) > 50:
            snapshots[name] = snapshots[name][-25:]
        self.save()

    def latest_snapshot(self, name: str) -> dict | None:
        snapshots = self._data.get("snapshots", {}).get(name, [])
        return snapshots[-1] if snapshots else None

    def restore_snapshot(self, name: str) -> dict | None:
        """
        Return the latest snapshot for *name* to allow callers to
        restore a subsystem to a known-good configuration.
        """
        snapshot = self.latest_snapshot(name)
        if snapshot:
            logger.info("📋 Restoring snapshot for %s from ts=%s", name, snapshot.get("ts"))
        return snapshot

    # ------------------------------------------------------------------
    # Evolution / knowledge base
    # ------------------------------------------------------------------

    def record_event(self, event_type: str, payload: dict) -> None:
        """Append an event to the persistent knowledge base."""
        events = self._data.setdefault("events", [])
        events.append({"type": event_type, "ts": time.time(), **payload})
        if len(events) > 1000:
            self._data["events"] = events[-500:]
        self.save()

    def query_events(self, event_type: str | None = None, limit: int = 20) -> list[dict]:
        events = self._data.get("events", [])
        if event_type:
            events = [e for e in events if e.get("type") == event_type]
        return events[-limit:]
