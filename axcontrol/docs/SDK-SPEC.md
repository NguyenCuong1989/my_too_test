# SDK Specification (Status: COMPLETE)

## Purpose
Provide client libraries (Python, TypeScript) to submit intents/commands, poll status, and fetch logs from the control plane without direct UI execution.

## Principles
- Intent-only submission; SDK cannot emit UI actions.
- Commands must be signed, device-bound, and validated by Decision Core.
- Network calls are untrusted channels; integrity/authorization enforced on device.

## Surfaces
- Submit intent → returns signed command envelope or policy denial reason.
- Query execution status, STOP reasons, and audit log segments (read-only).
- Control commands (start, pause, resume, stop, kill) scoped to mobile/CLI authority.

## Non-Goals
- No heuristic automation helpers.
- No raw AX/CGEvent exposure.

## Deliverables
- Python SDK (local + remote control-plane client)
- TypeScript SDK (web/mobile control-plane client)
- Shared protocol definitions (see `sdk/protocol.md`)
