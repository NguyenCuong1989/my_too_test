"""macOS Accessibility bridge (bounded).

Provides minimal AX operations required by finite command set. No dynamic AX traversal beyond allowlist.
"""
from typing import Any


class BoundedAXBridge:
    def perform(self, command: Any) -> Any:
        """Execute a bounded AX action.

        Must honor allowlists and sandbox constraints; no privilege escalation.
        """
        raise NotImplementedError("Phase 1 stub: AX bridge to be implemented in Phase 2")
