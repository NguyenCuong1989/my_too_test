# UX Mapping — Replit Export (Local-First Template)

Source: `external/replit_export/` (Replit export `ReplitExport-nguyencuong2509.tar.gz`).

Primary screen (`/`):
- Title: “Hello, World.” with badge “Local-First Template”.
- Status chips: “System Operational”, “Mobile-First Ready”, “Local Environment”.
- CTAs: `Get Started` (primary), `Documentation` (outline).
- Footer: “v1.0.0 • Mobile-First Tool-Orchestrated Build Method”.

Routes:
- `/` (home) via wouter `Route`.
- Fallback 404 page with heading “404 Page Not Found” and text “The requested resource is missing.”

UI Components (Radix + shadcn style):
- Buttons: primary + outline (expect role AXButton, labels above).
- Static text badges (role likely AXStaticText/AXText).
- Card containers with minimal interactive elements beyond buttons.

Policy/allowlist updates:
- Added to `core/policy/rules/ui_surface.yaml` with surfaces for CTA and status labels.
- No text inputs or destructive actions present; safe for TAB navigation.

Notes for AXCONTROL:
- Safe mode TAB-only is sufficient; Enter on primary/secondary buttons is acceptable if policy allows.
- LLM context keys: app name “Local-First Template”, route “/”, roles AXButton/AXStaticText.
- No additional AX affordances (checkbox, toggle) detected; vision fallback not required.
