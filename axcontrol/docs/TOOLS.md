# Tools Integration (CLI & Chat Box)

## Shell CLI (bounded)
- Module: `core/tools/shell_cli.py`
- Allowed commands: `pwd`, `ls (-l/-a)`, `cat`, `head -n`, `tail -n`.
- Denies pipes, redirects, subshells, or non-allowlisted flags.
- Returns exit_code/stdout/stderr; caller must log via audit logger.
- Policy: treat as read-only diagnostics; no mutation allowed.

## Chat Box → Intent
- Module: `core/tools/chat_box.py`
- Accepts recent chat messages (max 8) and calls `llm_strategy` (defaults to local `qwen3:8b`) for intent suggestion.
- Deterministic fallback intent (`chat-fallback`) if LLM unavailable or times out.
- Provenance marked (llm or human) for audit; replay never re-calls LLM.
- CLI runner: `core/loop/chat_cli.py` provides `/cli <cmd>` and `/ax` steps plus free-text intents (logged only).

## Usage Notes
- CommandType `CLI` added for shell tool envelopes; ensure policy gate before execution.
- Keep allowlist append-only; no destructive commands; rate-limit at caller if needed.
