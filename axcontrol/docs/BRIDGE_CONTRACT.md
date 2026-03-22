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
# Bridge Contract (Authoritative)

Endpoint:
- `POST /chat`

Request:
```json
{
  "text": "string",
  "meta": { "confirm": true }
}
```

Response required fields:
```json
{
  "system": {
    "mode": "IDLE | EXECUTING | HALTED",
    "simulation": true,
    "ax_enabled": false,
    "shell_enabled": true
  },
  "input": {
    "raw": "string | null",
    "type": "CLI | AX | FREE_TEXT | NONE"
  },
  "intent": {
    "kind": "CLI | AX | QUERY | FREE_TEXT_ACTION | NONE",
    "value": "string | null",
    "source": "RULE | human | NONE"
  },
  "decision": {
    "verdict": "ALLOW | STOP | CONFIRM_REQ | IDLE",
    "command": "string | null"
  },
  "execution": {
    "executed": false,
    "executor": "SHELL | AX | NONE",
    "result": "string | null"
  },
  "stop": {
    "reason": "NONE | lexicon_violation | audit_write_failed | ...",
    "message": "string | null"
  },
  "audit": {
    "timestamp": "ISO8601",
    "Chung": "sha256 hex",
    "recorded": true,
    "error": "string (optional)"
  },
  "ui": {
    "requires_confirm": false,
    "prompt": "string | null",
    "suggestions": ["string"]
  }
}
```

No-drift rules:
- Contract source-of-truth is this file + `/core/bridge/http_server.py`.
- UI A and UI B must not assume additional fields.
- `audit.recorded=true` only when append to sink succeeds.
