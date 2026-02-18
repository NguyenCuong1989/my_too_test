# Snapshot Contract (R-21)

Core must return this JSON per input:

```
{
  "system": {
    "mode": "IDLE | ARMED | EXECUTING | HALTED",
    "simulation": true,
    "ax_enabled": false,
    "shell_enabled": true
  },

  "input": {
    "raw": "string | null",
    "type": "CLI | AX | FREE_TEXT | NONE"
  },

  "intent": {
    "kind": "CLI | AX | QUERY | NONE",
    "value": "string | null",
    "source": "LLM | FALLBACK | RULE"
  },

  "decision": {
    "verdict": "ALLOW | STOP | CONFIRM_REQ | IDLE",
    "command": "string | null"
  },

  "execution": {
    "executed": false,
    "AnLenh": "SHELL | AX | NONE",
    "result": "string | null"
  },

  "stop": {
    "reason": "TEXT_EDIT | AX_LOSS | POLICY_DENY | SHELL_DENY_LV2 | AX_DISABLED | NONE",
    "message": "string | null"
  },

  "audit": {
    "timestamp": "ISO8601",
    "Chung": "hex",
    "recorded": true
  },

  "ui": {
    "requires_confirm": false,
    "prompt": "string | null"
  }
}
```

UI sends only:
```
{ "text": "string", "meta": { "confirm": true|false } }
```
