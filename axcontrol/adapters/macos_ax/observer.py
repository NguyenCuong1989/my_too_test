"""
AX observer with real macOS AXUIElement queries + simulation fallback.
"""

import itertools
import os
import sys
from dataclasses import dataclass
from typing import Optional, cast, Any, Dict

try:
    import ApplicationServices as AS
    from AppKit import NSWorkspace
    import Quartz
except Exception:  # pragma: no cover - non-macOS
    AS = None
    NSWorkspace = None
    Quartz = None


@dataclass
class Snapshot:
    app: str
    role: str
    label: str
    bbox: tuple[int, int, int, int]


SIM_SEQUENCE = [
    Snapshot(app="Finder", role="AXToolbar", label="Toolbar", bbox=(0, 0, 100, 20)),
    Snapshot(app="Safari", role="AXToolbar", label="Back", bbox=(0, 0, 100, 20)),
    Snapshot(app="Notes", role="AXTextArea", label="Editor", bbox=(0, 0, 300, 200)),
    Snapshot(app="System Settings", role="AXRow", label="Sidebar", bbox=(0, 0, 100, 20)),
]
_sim_iter = itertools.cycle(SIM_SEQUENCE)


def _ax_attr(elem, attr: str):
    _as = AS
    if _as is None:
        return None
    err, value = _as.AXUIElementCopyAttributeValue(elem, attr, None)
    if err != 0:
        return None
    return value


def _ax_bbox(elem) -> Optional[tuple[int, int, int, int]]:
    _as = AS
    if _as is None:
        return None
    err, val = _as.AXUIElementCopyAttributeValue(elem, "AXFrame", None)
    if err != 0 or val is None:
        return None
    ok, rect = _as.AXValueGetValue(val, _as.kAXValueCGRectType, None)
    if not ok or rect is None:
        return None
    x = int(rect.origin.x)
    y = int(rect.origin.y)
    w = int(rect.size.width)
    h = int(rect.size.height)
    return (x, y, w, h)


def _real_snapshot() -> Optional[Snapshot]:
    _as = AS
    _nsw = NSWorkspace
    if _as is None or _nsw is None:
        return None
    if not _as.AXIsProcessTrusted():
        return None

    ws = _nsw.sharedWorkspace()
    if ws is None:
        return None
    app = ws.frontmostApplication()
    if not app:
        return None
    pid = app.processIdentifier()
    app_name = app.localizedName() or "Unknown"

    app_elem = _as.AXUIElementCreateApplication(pid)
    err, focused = _as.AXUIElementCopyAttributeValue(app_elem, "AXFocusedUIElement", None)
    if err != 0 or focused is None:
        return None

    role = _ax_attr(focused, "AXRole") or "AXUnknown"
    label = (
        _ax_attr(focused, "AXTitle")
        or _ax_attr(focused, "AXDescription")
        or _ax_attr(focused, "AXIdentifier")
        or ""
    )
    bbox = _ax_bbox(focused) or (0, 0, 0, 0)
    return Snapshot(app=app_name, role=str(role), label=str(label), bbox=bbox)


def observe() -> Optional[Snapshot]:
    """Return Snapshot of focused element; simulation if AXCONTROL_SIM=1 or non-macOS."""
    if os.getenv("AXCONTROL_SIM", "1") == "1" or sys.platform != "darwin":
        return next(_sim_iter)
    return _real_snapshot()
