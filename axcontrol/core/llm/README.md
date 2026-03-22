# core/llm

LLM integration is optional, local-only, and sandboxed. The LLM may *propose* intents; it never emits executable actions and cannot bypass policy or STOP conditions.

## Guardrails
- 200ms hard timeout per call; subprocess-run with timeout.
- Clamp to intent schema; invalid output → fallback None.
- Deterministic fallback path; replay never re-invokes LLM.
- Logged as `LLM_DECISION` / `LLM_INTENT` with provenance=llm.
- Cannot override STOP; cannot emit events.

## Local setup (Ollama)
1. Install: `brew install ollama`
2. Verify: `ollama --version`
3. Pull model: `ollama pull llama3.1:8b` (or `3b`)
4. Smoke test: `ollama run llama3.1:8b \"Say OK\"`

## Usage
- Toggle via `LLM_MODE`.
- Build minimal context (app, role) → call strategy → intent suggestion or None.
- Downstream policy/decision flows remain deterministic; commands are only created after policy allow.
