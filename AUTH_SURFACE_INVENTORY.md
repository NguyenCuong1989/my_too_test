# AUTH SURFACE INVENTORY

Status: Draft
Snapshot date: 2026-03-22
Scope: `/Users/andy` local authority and session surfaces
Method: D&R Protocol, local-source-first, fail-close

## 1. Canon

Authority is assigned to durable control surfaces, not to transient browser sessions.

Canonical rule:

```text
authority_surface != session_surface
browser_profile != authority
ephemeral_context != canon
```

## 2. Surface Taxonomy

### 2.1 Authority Surfaces

- `gh`
- `.codex`
- `.gemini`
- `.openclaw`
- `.hyperai`

### 2.2 Session Surfaces

- Chrome profiles
- browser automation profiles
- Playwright contexts

### 2.3 Registry Surfaces

- repo runtime canon and registries
- capability maps
- planner/orchestrator policy files

## 3. Inventory

| Surface | Canonical role | Local evidence | Scope | Risk profile | Required rule |
|---|---|---|---|---|---|
| `gh` | GitHub control surface for repos, issues, PRs, and workflow routing | Live auth was previously verified in local audit | External authority | High impact if mixed with browser session state | One identity, one auth lane, no shadow login in browser profile |
| `.codex` | Codex runtime authority surface | `auth.json`, `config.toml`, `state_5.sqlite`, `history.jsonl`, `session_index.jsonl`, `archived_sessions/`, `shell_snapshots/` | Agent runtime and workspace memory | Medium to high, because it can carry live tokens and execution state | Keep Codex auth isolated from browser automation state |
| `.gemini` | Gemini CLI and Antigravity authority surface | `google_accounts.json`, `oauth_creds.json`, `projects.json`, `trustedFolders.json`, `antigravity/mcp_config.json`, `antigravity-browser-profile/`, `history/` | Google/Gemini/MCP routing and browser-backed sessions | High, because OAuth, MCP, and browser state are co-located | Separate projects, OAuth, and browser profile ownership |
| `.openclaw` | OpenClaw control surface | `identity/device-auth.json`, `openclaw.json`, `workspace/AGENTS.md`, `workspace/IDENTITY.md`, `workspace/BOOTSTRAP.md`, `gateway` auth/mode config | Device identity and workspace control | High, because device identity and gateway settings define authority | One device identity per trusted operator lane |
| `.hyperai` | HyperAI system authority surface | `config/persistence_status.json`, `services/`, `logs/`, `processes.json`, startup and recovery scripts | System orchestration and persistence | Medium to high, because process control and persistence are coupled | Keep process control separate from browser session state |
| Chrome `Default` | Human browsing session surface | `Library/Application Support/Google/Chrome/Default` | Browser session | Medium | Do not use as shared automation identity |
| Chrome `Profile 1` | Secondary browser session surface | `Library/Application Support/Google/Chrome/Profile 1` | Browser session | Medium | Assign a single purpose and never cross-use with authority surfaces |
| `.gemini/antigravity-browser-profile` | Dedicated Gemini/Antigravity browser session | `.gemini/antigravity-browser-profile/` | Browser session | High if shared | Keep isolated from human Chrome profiles |
| Playwright contexts | Ephemeral automation session surface | Runtime-created, not stored as a stable authority directory | Temporary browser automation | High if reused across tasks | Always treat as disposable and task-local |
| Repo canon files | Runtime registry and policy surfaces | `runtime_authority_map.yaml`, `omni_registry.json`, `GEMINI.md`, `DOCKER_RUNTIME_AUTHORITY_CANON.md`, `APO_PLANNER_SYSTEM_SPEC.md` | Policy and execution registry | Medium | Canon files define behavior, not credentials |

## 4. Observed State Snapshot

- `.gemini/projects.json` contains `11` project entries.
- `.gemini/antigravity/mcp_config.json` contains `19` MCP servers.
- Chrome has `2` top-level profiles visible: `Default` and `Profile 1`.
- `.gemini` contains both `antigravity-browser-profile` and `history`, which confirms browser session and activity logs are colocated with authority state.
- `.codex` contains both runtime state and auth artifacts, so it must be treated as a privileged authority surface rather than a generic cache.

## 5. Ownership Model

Each authority surface must have exactly one owning lane.

```text
one surface -> one owner -> one token store -> one profile boundary -> one audit trail
```

Required assignments:

- `gh` owns GitHub control-plane actions only.
- `.codex` owns Codex runtime and agent execution state only.
- `.gemini` owns Gemini CLI, MCP routing, and Antigravity browser sessions only.
- `.openclaw` owns OpenClaw gateway/device identity only.
- `.hyperai` owns HyperAI process and persistence control only.

## 6. Exclusion Rules

- Browser profiles are not authority sources.
- Playwright contexts are not durable identities.
- A session that can log in is not automatically the canonical owner.
- A token that works in one surface must not be copied into another surface unless the receiving surface is the declared owner.

## 7. Immediate Risks

1. Token scattering across `.codex`, `.gemini`, `.openclaw`, and browser-backed profiles.
2. Multiple browser automation processes coexisting without a declared owner.
3. Authority confusion between canonical auth surfaces and shell/session surfaces.
4. Silent drift between registry state and active browser profile state.

## 8. Required Outputs for Downstream Use

This inventory is only valid if downstream systems preserve:

1. Surface-level ownership tags.
2. Explicit session boundary per browser profile.
3. Separate storage for auth material and execution material.
4. Fail-close behavior when ownership is ambiguous.

## 9. Canonical Summary

```text
gh, .codex, .gemini, .openclaw, and .hyperai are authority surfaces.
Chrome, browser profiles, and Playwright contexts are session surfaces.
Authority must not be inferred from session presence.
```
