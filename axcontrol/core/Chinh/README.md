# core/decision

Data models and authority logic that translate normalized state and intent into signed, policy-checked command envelopes. Execution is never triggered here; only deterministic decision-making.

Components:
- `intent.py`: intent schema (human or LLM provenance).
- `command.py`: signed, device-bound command envelopes (finite set).
- `policy.py`: policy verdict structures.
- `decision_core.py`: single authority to build + validate envelopes (exec elsewhere).
- `llm_strategy.py`: local-only LLM intent suggestion with 200ms timeout and deterministic fallback.
