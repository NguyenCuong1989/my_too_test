"""TAB-only emitter (safe mode)."""

import sys
import time

try:
    import Quartz
except Exception:  # pragma: no cover - non-macOS
    Quartz = None

KEY_TAB_CODE = 0x30


def emit_tab() -> None:
    if sys.platform != "darwin" or Quartz is None:
        print("[emit_tab] (simulated) sent TAB")
        return
    try:
        down = Quartz.CGEventCreateKeyboardEvent(None, KEY_TAB_CODE, True)
        up = Quartz.CGEventCreateKeyboardEvent(None, KEY_TAB_CODE, False)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, down)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, up)
        time.sleep(0.01)
    except Exception as exc:  # safety fallback
        print(f"[emit_tab] CGEvent failed: {exc}")
