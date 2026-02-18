# Threat Model — STRIDE (Status: COMPLETE)

## Assets
- Decision Core authority
- Signed command envelopes
- Audit log + determinism hashes
- macOS accessibility bridge
- Mobile control plane channels

## Threats (per STRIDE)
- **Spoofing:** UI spoofing, command forgery → mitigated by signed, device-bound envelopes and UI surface allowlist.
- **Tampering:** Replay tampering, log modification → append-only log with hash chaining; local storage integrity checks.
- **Repudiation:** Action denial → full audit trail with state_before/after and policy verdicts.
- **Information Disclosure:** Vision output leaks → vision bounded; no raw pixel export; mobile plane read-only for status/logs.
- **Denial of Service:** Event flooding, timing violations → rate limits, watchdog, explicit STOP reasons.
- **Elevation of Privilege:** Permission escalation → bounded AX/CGEvent usage, no runtime privilege escalation, policy gate mandatory.

## Assumptions
- Human user and macOS core are trusted.
- Target apps, LLM, and network are untrusted.
- Mobile app is semi-trusted (UI-only).

## Residual Risks
- Vision hallucination (non-authoritative mitigates impact)
- Prompt injection against LLM intent proposals (policy + human approval required)

## Controls Mapping
- Policy Model: static + context-aware constraints
- Safety: kill-switch, watchdog, determinism hash validation
- Replay Rules: environment match required; read-only unless armed
