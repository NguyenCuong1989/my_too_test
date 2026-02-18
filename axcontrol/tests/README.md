# Tests Overview

- `real_device/`: R-17 safety validations on live macOS apps (System Settings, Notes) with TAB-first navigation and strict STOP semantics.
- `replay/`: Deterministic replay tests consuming audit logs; no live UI access; LLM never re-invoked during replay.
