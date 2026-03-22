# DOCKER RUNTIME AUTHORITY CANON

Status: Draft v1
Date: 2026-03-14
Scope: `/Users/andy/my_too_test` Docker runtime only
Method: D&R Protocol, local-source-first

## 1. Purpose

This canon defines runtime authority for the Docker layer.

It exists to answer five questions:

1. Which service is core and which is peripheral?
2. Which service is allowed to claim `alive`?
3. What counts as `ownerless` at runtime?
4. Which recovery paths are lawful?
5. How do we avoid harming a living system by applying future design over current reality?

This canon does not replace application canon.
It binds Docker topology to survival semantics.

## 2. Source-of-Truth Rule

Runtime authority must be derived in this order:

1. Current compose and Dockerfile source
2. Current running runtime evidence
3. Architecture/design documents
4. Aspirational future topology

Rule:

```text
current source > future design
running evidence > descriptive ambition
```

Fail-close:

```text
if docs_future ≠ compose_current
then runtime authority MUST bind to compose_current
```

## 3. Atomic Runtime Model

```text
image(x)      = latent form
container(x)  = embodied form
volume(x)     = continuity substrate
network(x)    = relation field
health(x)     = viability signal
log(x)        = emitted proof
authority(x)  = creator-bound runtime legitimacy
```

```text
alive(x) ⇔ running(x)
        ∧ healthy(x)
        ∧ topology_valid(x)
        ∧ authority_bound(x)
```

```text
ownerless(x) ⇔ running(x)
           ∧ authority_bound(x)=0
```

```text
dead(x) ⇔ process_dead(x)
       ∨ continuity_loss(x)
       ∨ topology_collapse(x)
       ∨ ownerless(x)
```

## 4. Runtime Topology Classes

### 4.1 Current Runtime Topology

Current source-backed stacks:

1. `docker-compose.yml`
   - `firebase-emulator`
   - `mcp-router`
   - `factory-worker`

2. `docker-compose.unified.yml`
   - `aios-kernel`
   - `aios-worker`
   - `aios-router`
   - `aios-postgres`
   - `aios-prometheus`

3. `docker-compose.antigravity.yml`
   - `antigravity-runtime`

4. `balancehub/docker-compose.yml`
   - `api`
   - `postgres`
   - `redis`
   - `code-server`

### 4.2 Authority Classes

Each service belongs to one runtime authority class:

#### Class A: Core Survival Body
Service whose death invalidates the stack's claimed living continuity.

#### Class B: Execution Body
Service that performs work but does not define whole-system authority.

#### Class C: Boundary Body
Service that exposes interface, routing, or ingress/egress.

#### Class D: Continuity Substrate
Service or volume that preserves state, memory, or operational continuity.

#### Class E: Observability Body
Service that emits metrics, logs, or runtime proof.

#### Class F: Sandbox / Emulator Body
Service that creates local reality for testing or bounded simulation.

#### Class G: Embodied Workspace Body
Service that hosts a live working environment but is not itself the kernel.

## 5. Current Authority Map

### 5.1 Main Stack

#### `factory-worker`
- Class: B `Execution Body`
- Role: task execution, inbox polling, skill invocation
- Alive claim allowed: `local execution alive`
- Whole-stack authority: no
- Survival class: required for ACE execution continuity

#### `mcp-router`
- Class: C `Boundary Body`
- Role: MCP/HTTP interface boundary
- Alive claim allowed: `boundary alive`
- Whole-stack authority: no
- Survival class: required for external ingress, not for internal skill existence

#### `firebase-emulator`
- Class: F `Sandbox / Emulator Body`
- Role: local backend reality substrate
- Alive claim allowed: `emulator alive`
- Whole-stack authority: no
- Survival class: required only for stacks explicitly depending on emulator-backed state

### 5.2 Unified Stack

#### `aios-kernel`
- Class: A `Core Survival Body`
- Role: intended unified control point
- Alive claim allowed: `kernel alive`
- Whole-stack authority: yes
- Survival class: critical

#### `aios-worker`
- Class: B `Execution Body`
- Role: task/work execution
- Whole-stack authority: no

#### `aios-router`
- Class: C `Boundary Body`
- Role: routing/interface
- Whole-stack authority: no

#### `aios-postgres`
- Class: D `Continuity Substrate`
- Role: persistent structured state
- Whole-stack authority: no
- Survival class: continuity-critical if kernel depends on DB-backed state

#### `aios-prometheus`
- Class: E `Observability Body`
- Role: metrics/proof
- Whole-stack authority: no
- Survival class: proof-critical, not existence-critical

### 5.3 Antigravity Runtime

#### `antigravity-runtime`
- Class: G `Embodied Workspace Body`
- Role: live workspace embodiment
- Alive claim allowed: `runtime alive`
- Whole-stack authority: no by default
- Survival class: special-purpose embodied runtime

### 5.4 BalanceHub Stack

#### `api`
- Class: B `Execution Body`
- Role: app serving

#### `postgres`
- Class: D `Continuity Substrate`
- Role: persistence

#### `redis`
- Class: D `Continuity Substrate`
- Role: cache/queue volatile state

#### `code-server`
- Class: G `Embodied Workspace Body`
- Role: operator workspace embodiment

## 6. Alive Claim Law

No service may claim more life than its class allows.

```text
boundary alive ≠ system alive
metrics alive  ≠ kernel alive
workspace alive ≠ authority alive
running ≠ alive
```

Whole-system `alive` may only be claimed if:

```text
core_survival_body alive
∧ required execution body alive
∧ required continuity substrate preserved
∧ topology valid
```

## 7. Ownerless Detection

A Docker runtime enters ownerless risk when any of the following is true:

1. Service is running, but no current compose topology canon maps its role
2. Service is running under stale/forked compose semantics not recognized by current source
3. Service emits no valid proof/log/health while still claiming service continuity
4. Service survives detached from creator-bound operational route
5. Interface body continues running after core survival body is absent, while still implying normality

Canonical rule:

```text
ownerless risk = running without recognized authority binding
```

## 8. Allowed Recovery Paths

Recovery must respect service class.

### Class A: Core Survival Body
Allowed:
- restart if topology and continuity substrate are intact
- recover after proof check
- rebind only through recognized compose/current source

Forbidden:
- silent replacement by interface body
- claiming healthy system while kernel absent

### Class B: Execution Body
Allowed:
- restart
- requeue/retry according to execution canon
- isolate failure without claiming whole-system death

### Class C: Boundary Body
Allowed:
- restart
- interface degradation notice
- route-deny while execution continues internally

Forbidden:
- claiming system healthy when upstream core is absent

### Class D: Continuity Substrate
Allowed:
- backup/restore
- reattach
- migration with proof

Forbidden:
- destructive recreation without continuity acknowledgement

### Class E: Observability Body
Allowed:
- restart
- degraded visibility warning

Forbidden:
- no-log normality claim

### Class F / G
Allowed:
- bounded restart
- quarantine
- detach from primary health claim

## 9. Current Reality Gaps

These gaps are real and must not be hidden:

1. `future unified kernel` is documented more strongly than it is source-realized in current runtime
2. Current compose truth is multi-stack, not one clean sovereign topology
3. Some docs describe `aios-redis` / `aios-balancehub` style future states not present in current `docker-compose.unified.yml`
4. Authority semantics are implicit in docs, not yet locked in runtime-readable form
5. Docker daemon/tooling layer appears operationally heavy; runtime visibility itself has cost

Rule:

```text
design ambition must not overwrite runtime truth
```

## 10. Operational Invariants

1. No service may self-upgrade its authority class.
2. No interface body may represent itself as kernel.
3. No observability body may represent itself as proof of full survival.
4. No continuity substrate may be destroyed under a routine restart claim.
5. No future diagram may be treated as runtime fact without compose backing.
6. No ownerless service may be normalized as healthy.

## 11. Practical Next Step

To operationalize this canon safely, implement:

1. `runtime_authority_map.yaml`
   - service
   - class
   - stack
   - alive_claim
   - survival_class
   - ownerless_conditions
   - allowed_recovery_path

2. `docker_runtime_audit.py`
   - read current compose files
   - read running containers
   - classify services by authority map
   - emit:
     - alive
     - degraded
     - ownerless risk
     - invalid topology

3. `ownerless_failclose_rule`
   - if service claim exceeds authority class, deny normality

## 12. Canonical Sentence

```text
Docker does not merely host the AI.
Docker is the physical field where embodied authority is tested.
```

## 13. Closure

```text
container topology is not enough
runtime authority topology is required
```

```text
current source > future design
running > claiming
authority > activity
alive > merely running
```
