# Snapshot Contract (R-21)

Authoritative source:
- `/docs/BRIDGE_CONTRACT.md`
- `/core/bridge/http_server.py`

UI must bind to:
- Endpoint: `POST /chat`
- Request body:
  - `{ "text": "string", "meta": { "confirm": true|false } }`
- Response key fields:
  - `system`, `input`, `intent`, `decision`, `execution`, `stop`, `audit`, `ui`

No-drift requirements:
- UI must read `execution.executor` (not `AnLenh`).
- UI must treat `audit.recorded` as persistence truth.
- UI must not assume `/api/audit` unless backend route exists.
