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
"""
Passive observation logger (read-only, no emit).

- Logs input events (key/mouse metadata) and periodic AX snapshots to NDJSON.
- Classifies human activity H0/H1/H2 by event density (rolling 5s window).
- No network, no emit, no content capture (no key strings, no clipboard data).

Requirements: macOS, Accessibility + Input Monitoring permissions.
"""

import argparse
import json
import sys
import time
from collections import deque
from pathlib import Path

from adapters.macos_ax import observer
from core.The.state_projector import map_state_to_hexagram

try:
    from Quartz import CGEventTapCreate, CGEventTapEnable
    from Quartz import CFRunLoopAddSource, CFRunLoopGetCurrent, CFRunLoopSourceInvalidate, CFRunLoopRunInMode
    from Quartz import CFMachPortCreateRunLoopSource, kCFRunLoopCommonModes, kCFRunLoopDefaultMode, kCGHIDEventTap, kCGHeadInsertEventTap
    from Quartz import kCGEventMaskForAllEvents, kCGEventKeyDown, kCGEventLeftMouseDown, kCGEventRightMouseDown
    from Quartz import kCGEventOtherMouseDown, CGEventGetIntegerValueField, kCGMouseEventButtonNumber, kCGEventSourceUnixProcessID
except Exception:
    print("This observer requires macOS Quartz (pyobjc).", file=sys.stderr)
    sys.exit(1)


def now():
    return time.time()


def classify_human_state(events_window, horizon=5.0):
    """Deterministic classifier based on event count in horizon seconds."""
    cutoff = now() - horizon
    while events_window and events_window[0] < cutoff:
        events_window.popleft()
    n = len(events_window)
    if n == 0:
        return "H0"
    if n < 8:
        return "H1"
    return "H2"


def write_record(fh, obj):
    fh.write(json.dumps(obj, ensure_ascii=False) + "\n")
    fh.flush()


def run(interval: float, duration: float, output: Path):
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as fh:
        events_window = deque()
        human_state = "H0"

        def tap_callback(proxy, etype, event, refcon):
            ts = now()
            sub = None
            if etype == kCGEventKeyDown:
                sub = "key"
                keycode = CGEventGetIntegerValueField(event, 9)  # kCGKeyboardEventKeycode
                pid = CGEventGetIntegerValueField(event, kCGEventSourceUnixProcessID)
                rec = {"ts": ts, "type": "input", "sub": sub, "keycode": int(keycode), "pid": int(pid)}
                write_record(fh, rec)
            elif etype in (kCGEventLeftMouseDown, kCGEventRightMouseDown, kCGEventOtherMouseDown):
                sub = "mouse"
                btn = CGEventGetIntegerValueField(event, kCGMouseEventButtonNumber)
                pid = CGEventGetIntegerValueField(event, kCGEventSourceUnixProcessID)
                rec = {"ts": ts, "type": "input", "sub": sub, "button": int(btn), "pid": int(pid)}
                write_record(fh, rec)
            if sub:
                events_window.append(ts)
            return event

        # Install event tap (passive)
        tap = CGEventTapCreate(
            kCGHIDEventTap,
            kCGHeadInsertEventTap,
            0,
            kCGEventMaskForAllEvents,
            tap_callback,
            None,
        )
        if not tap:
            print("Failed to create event tap (check permissions).", file=sys.stderr)
            sys.exit(1)
        run_loop_source = CFMachPortCreateRunLoopSource(None, tap, 0)
        CFRunLoopAddSource(CFRunLoopGetCurrent(), run_loop_source, kCFRunLoopCommonModes)
        CGEventTapEnable(tap, True)

        start = now()
        next_poll = start
        try:
            while True:
                now_ts = now()
                if duration > 0 and now_ts - start >= duration:
                    break
                if now_ts >= next_poll:
                    snap = observer.observe()
                    if snap:
                        hex_bits = map_state_to_hexagram(snap)
                        rec = {
                            "ts": now_ts,
                            "type": "ax",
                            "app": getattr(snap, "app", None),
                            "role": getattr(snap, "role", None),
                            "label": getattr(snap, "label", None),
                            "hex": hex_bits,
                        }
                        write_record(fh, rec)
                    state = classify_human_state(events_window)
                    if state != human_state:
                        human_state = state
                        write_record(fh, {"ts": now_ts, "type": "human_state", "state": human_state})
                    next_poll = now_ts + interval
                # Pump run loop to deliver tap events
                CFRunLoopRunInMode(kCFRunLoopDefaultMode, 0.01, False)
        finally:
            CFRunLoopSourceInvalidate(run_loop_source)
            # no explicit close for tap; exiting process releases


def main():
    ap = argparse.ArgumentParser(description="AXCONTROL passive observation logger (no emit).")
    ap.add_argument("--interval", type=float, default=0.5, help="Snapshot interval seconds (default 0.5)")
    ap.add_argument("--duration", type=float, default=300, help="Total duration seconds (0 = infinite)")
    ap.add_argument("--output", type=Path, default=Path("logs/observe.ndjson"), help="Output NDJSON file")
    args = ap.parse_args()
    run(args.interval, args.duration, args.output)


if __name__ == "__main__":
    main()
