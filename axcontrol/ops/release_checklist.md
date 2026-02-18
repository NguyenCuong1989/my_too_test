# Release Checklist (R-17)

## I. Package as .app (local, sandboxed)
- Ensure core loop entrypoint `run_ax.py` imports `core.loop.control_loop.run`.
- Create bundle structure:
  - `app/AXControl.app/Contents/MacOS/AXControl` (executable wrapper, chmod +x)
  - `app/AXControl.app/Contents/Resources/`
  - `app/AXControl.app/Contents/Info.plist` with:
    - `CFBundleName=AXControl`
    - `CFBundleIdentifier=local.ax.control`
    - `CFBundleVersion=1.0`
    - `CFBundleExecutable=AXControl`
    - `LSUIElement=true` (no Dock icon)
- Open `app/AXControl.app` once to trigger prompts; tick AXControl in Accessibility (and Input Monitoring if needed).
- Features: local-only, bounded AX/input emit, kill-switch present, no cloud, no auto-start.

## J. Sign & Notarize (Developer ID)
- Prereqs: `xcode-select --install`, `xcrun --version`, `security find-identity -p codesigning`.
- Record Developer ID Application identity.
- Codesign: `codesign --force --deep --options runtime --sign "Developer ID Application: NAME (TEAMID)" app/AXControl.app`
- Verify: `codesign --verify --deep --strict app/AXControl.app`
- Zip: `ditto -c -k --keepParent app/AXControl.app AXControl.zip`
- Notarize: `xcrun notarytool submit AXControl.zip --apple-id "you@appleid.com" --team-id "TEAMID" --password "APP_SPECIFIC_PASSWORD" --wait`
- Expect status: Accepted; then `xcrun stapler staple app/AXControl.app`
- Gatekeeper check: `spctl -a -vv app/AXControl.app` → accepted, source=Notarized Developer ID.
- Post-step: re-tick Accessibility/Input Monitoring if prompted; double-click run without security warnings.
