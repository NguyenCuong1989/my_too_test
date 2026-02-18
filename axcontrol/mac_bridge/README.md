# macOS Control Bridge Notes (R-17)

## Accessibility & Permissions
- Open `x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility` and tick Terminal, Python, and AXControl.app (after packaging).
- Enable Input Monitoring for Terminal/Python when emitting keystrokes (TAB-only in safe mode).
- Vision remains OFF by default.

## AX Observer (real)
- Implement `adapters/macos_ax/observer.py` using `NSWorkspace` for frontmost app and `AXUIElementCopyAttributeValue` wrappers.
- Return stable tuples: app, role, label, bbox. Handle `AX_LOST` gracefully (no crashes, STOP when None).
- Poll with 0.2s sleep; log snapshots; STOP on AX loss or app switch.
- CLI smoke: `python3 examples/run_finder.py` should log AX in real time without crashing when switching/minimizing apps.

## TAB-only Input Emit
- Grant Accessibility + Input Monitoring to emitter process.
- `input/keyboard.py`: `KEY_TAB = 0x30`; `emit_tab()` emits keydown+keyup with 10ms gap; rate limited (min 200ms between tabs).
- Control loop: STOP on AX loss or app change; TAB-only, no Enter/click.

## Safari AX Context (bounded)
- `adapters/macos_ax/safari.py` should derive zones: ADDRESS_BAR, WEB_CONTENT, TOOLBAR_BUTTON.
- Observer sets `ctx["app"]="Safari"` and attaches zone.
- Policy: ADDRESS_BAR/WEB_CONTENT → actions blocked; TOOLBAR_BUTTON → allow TAB only.
- Demo: `python3 examples/run_safari.py` with Safari open; TAB should move toolbar/tabs, never enter web content/address bar.

## Safety Invariants
- No dynamic code injection; bounded AX/CGEvent usage only.
- Kill-switch local-only; human override always wins.
