# AUTH SURFACE ROTATION AND ISOLATION PLAN

Status: Draft
Snapshot date: 2026-03-22
Scope: `/Users/andy` auth, browser, and agent surfaces
Objective: reduce token scattering, isolate session ownership, and normalize authority lanes
Method: fail-close control ladder

## 1. Goal

Establish one canonical owner per auth surface and one dedicated session boundary per browser lane.

Primary target:

```text
minimize shared auth state
minimize mixed browser ownership
minimize silent drift between registry and session
```

## 2. Control Ladder

### Phase 1 - Freeze

- Stop new ad hoc logins.
- Do not reuse any browser profile for a different authority surface.
- Do not rotate secrets while ownership is still ambiguous.

### Phase 2 - Tag

- Label each surface as `authority`, `session`, or `registry`.
- Mark the owning app, folder, and process for each surface.
- Identify any surface that currently has more than one active login path.

### Phase 3 - Split

- Give each authority surface a dedicated local store.
- Give each browser lane a dedicated profile directory.
- Keep human browsing separate from agent automation browsing.

### Phase 4 - Migrate

- Move sessions one surface at a time.
- Validate the new lane before decommissioning the old one.
- Never migrate two authority surfaces into the same browser profile.

### Phase 5 - Rotate

- Rotate only the surface that has changed owner, leaked, or drifted.
- Keep rotations scoped to the smallest viable boundary.
- Replace stale credentials after migration, not before.

### Phase 6 - Audit

- Re-run inventory.
- Confirm that the active profile matches the declared owner.
- Confirm that no authority surface is backed by a session surface that also serves another owner.

## 3. Isolation Matrix

| Surface | Isolation boundary | Rotation trigger | Storage rule | Recovery rule |
|---|---|---|---|---|
| `gh` | CLI auth lane only | account handoff, suspicious token use, repo ownership change | keep GitHub auth out of browser profile stores | re-authenticate in CLI and revoke stale grants |
| `.codex` | Codex runtime store only | workspace change, token exposure, agent reset | keep Codex auth and state together, but not in browser session data | rebind to current workspace root and invalidate stale sessions |
| `.gemini` | Gemini CLI + Antigravity lane only | project ownership change, browser profile compromise, MCP registry drift | keep OAuth and MCP state in surface-local storage only | reissue browser profile and revalidate MCP server registry |
| `.openclaw` | device identity and gateway lane only | device replacement, gateway mode change, identity mismatch | keep device auth separate from browser auth | regenerate device binding and re-approve gateway mode |
| `.hyperai` | process and persistence lane only | service restart with identity change, persistence corruption | keep system persistence out of browser profiles | restore from local backup or reinitialize process state |
| Chrome human profile | one human lane | profile contamination, shared login, unexpected extension state | never store automation identity here | create a clean profile and migrate only user-owned browsing |
| Chrome automation profile | one automation lane | task boundary change, profile leakage, mixed credentials | one purpose only, no human browsing | destroy and recreate if ownership becomes unclear |
| `.gemini/antigravity-browser-profile` | Gemini automation lane only | Gemini login drift, MCP auth drift, profile compromise | no shared use with Chrome Default or Profile 1 | re-create from clean baseline and relink to Gemini only |
| Playwright context | single task lane | task completion, failed state, context leak | never persist as durable authority | discard and create a fresh context per task |

## 4. Rotation Rules

### 4.1 What rotates

- Browser profile cookies and local storage.
- OAuth refresh tokens tied to a compromised or stale lane.
- Device identity bindings when a device is repurposed.
- MCP access grants when project ownership changes.

### 4.2 What does not rotate casually

- Canonical registry files.
- Stable workspace ownership records.
- Runtime policy documents.
- Historical audit logs unless retention policy requires pruning.

### 4.3 Rotation order

1. Create the new isolated lane.
2. Validate that the new lane can authenticate.
3. Confirm that the old lane is no longer needed.
4. Revoke or disable the old lane.
5. Re-run inventory and compare with the previous snapshot.

## 5. Browser Isolation Plan

Current browser evidence shows:

- `Chrome/Default`
- `Chrome/Profile 1`
- `.gemini/antigravity-browser-profile`

Required future state:

- `Chrome/Default` is reserved for human browsing only.
- `Chrome/Profile 1` is reserved for one non-human purpose only.
- `.gemini/antigravity-browser-profile` is reserved for Gemini/Antigravity only.
- Playwright uses ephemeral contexts only and never inherits a shared profile by default.

Operational constraints:

- No browser profile may represent multiple authority surfaces.
- No automation process may attach to a profile owned by a different lane.
- No profile may be used as a hidden fallback for another service after login failure.

## 6. Session Ownership Rules

```text
session_owner must be explicit
session_owner must be stable
session_owner must be single-valued
```

Required owner labels:

- `human`
- `codex`
- `gemini`
- `openclaw`
- `hyperai`
- `playwright-task`

Normalization rule:

```text
if owner is unknown
then deny reuse
```

## 7. Failure Modes

### 7.1 Token scattering

Symptoms:

- the same account appears in multiple tools without a declared owner
- auth files and browser profiles both carry overlapping access material

Response:

- freeze new logins
- isolate the most privileged lane first
- rebuild the lowest-trust lane second

### 7.2 Mixed browser ownership

Symptoms:

- one Chrome profile is used for both human browsing and automation
- one profile is attached to both Gemini and a separate operator session

Response:

- split the profile
- move the automation lane to a dedicated directory
- revoke stale cookies after migration

### 7.3 Registry drift

Symptoms:

- declared project or MCP ownership no longer matches the active session

Response:

- update the registry first
- rotate only the impacted auth lane
- keep the rest of the system stable

## 8. Implementation Sequence

1. Freeze current logins and sessions.
2. Create a canonical owner map for every auth surface.
3. Split browser profiles by owner.
4. Rebind `.gemini`, `.codex`, `.openclaw`, and `gh` to their declared lanes.
5. Re-run inventory and confirm no shared-session ambiguity remains.
6. Add periodic review for new tools and new browser profiles.

## 9. Operating Cadence

- Inventory review: weekly.
- Session drift review: on tool install or new browser profile creation.
- Credential rotation review: after compromise, ownership change, or lane migration.
- Registry review: after any change to planner, orchestrator, or MCP routing.

## 10. Success Criteria

The plan is complete when:

1. Every auth surface has exactly one declared owner.
2. Every browser profile has exactly one purpose.
3. No authority surface depends on a shared browser profile.
4. No session surface is treated as canonical authority.
5. Inventory and runtime state converge after re-scan.

## 11. Canonical Summary

```text
split by surface
own by lane
rotate by trigger
audit by snapshot
fail closed on ambiguity
```
