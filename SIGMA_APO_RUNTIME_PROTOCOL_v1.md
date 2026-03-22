# APΩ Runtime Protocol Specification (APΩ-PLANNER-001)

## SECTION 1 — APΩ Runtime System Architecture

```
Ψ_t  (System State)
│
▼
┌───────────────────────────────┐
│ Telegram Interface            │
└───────────────┬───────────────┘
│
▼
┌───────────────────────────────┐
│ Command Router                │
│ Routes external commands      │
└───────────────┬───────────────┘
│
▼
┌───────────────────────────────┐
│ State Manager                 │
│ Maintains canonical Ψ state   │
└───────────────┬───────────────┘
│
▼
┌───────────────────────────────┐
│ Planner Service (Π_plan)      │
│ LLM Policy Engine             │
│ Stateless planning endpoint   │
└───────────────┬───────────────┘
│
▼
┌───────────────────────────────┐
│ Canon Validator (V)           │
│ Enforces capability + phase   │
└───────────────┬───────────────┘
│
▼
┌───────────────────────────────┐
│ Omni Orchestrator (Ω)         │
│ Executes validated DAG tasks  │
└───────────────┬───────────────┘
│
┌───────┼────────┐
▼       ▼        ▼
Factory(F) AXControl(A) Phoenix(P)
│       │        │
└──── Skill Executors ─────┘
│
▼
Ψ_{t+1}
```

### Runtime Equation

`Ψ_t → Π_plan → τ → Ω → Ψ_{t+1}`

---

## SECTION 2 — APΩ Planner Protocol Specification

### Protocol ID

`APΩ-PLANNER-001`

### Endpoint

`POST /planner`

### Planner Function

`Planner(Ψ, goal, context) → τ`

Where:

- `Ψ` = system state
- `goal` = runtime objective
- `τ` = DAG task graph

### Planner Responsibilities

1. analyze_state(Ψ)
2. compute_plan(goal)
3. emit_task_graph(τ)

### Planner Forbidden Actions

- execution
- shell commands
- state mutation
- system instruction emission

Execution belongs exclusively to the runtime executor: **Ω (Omni Orchestrator)**.

---

### Canonical Phase Model

- Origin
- Event
- Propagation
- Observe
- Interface
- Failure
- Boundary

**Ordering Constraint**: `phase(i) ≤ phase(j) if edge(i,j)`

---

## SECTION 3 — JSON Schemas

### Planner Request Schema

```json
{
  "$schema":"http://json-schema.org/draft-07/schema#",
  "type":"object",
  "required":[
    "state",
    "goal",
    "allowed_capabilities"
  ],
  "properties":{
    "state":{"type":"object"},
    "goal":{"type":"string"},
    "context":{"type":"object"},
    "allowed_capabilities":{
      "type":"array",
      "items":{
        "type":"string",
        "enum":["factory", "axcontrol", "phoenix"]
      }
    }
  }
}
```

### Planner Response Schema

```json
{
  "$schema":"http://json-schema.org/draft-07/schema#",
  "type":"object",
  "required":["tasks", "edges"],
  "properties":{
    "tasks":{
      "type":"array",
      "items":{
        "type":"object",
        "required":["id", "phase", "capability", "skill", "input"],
        "properties":{
          "id":{"type":"string"},
          "phase":{
            "type":"string",
            "enum":["origin", "event", "propagation", "observe", "interface", "failure", "boundary"]
          },
          "capability":{
            "type":"string",
            "enum":["factory", "axcontrol", "phoenix"]
          },
          "skill":{"type":"string"},
          "input":{"type":"object"}
        }
      }
    },
    "edges":{
      "type":"array",
      "items":{
        "type":"object",
        "required":["from", "to"],
        "properties":{
          "from":{"type":"string"},
          "to":{"type":"string"}
        }
      }
    }
  }
}
```

---

## SECTION 4 — Python Planner Service Implementation

(Implemented in `planner_service_v2.py`)

---

## SECTION 5 — Canon Validation Interface

### Capability Map

```python
VALID_CAPABILITIES = {
    "factory": ["deploy", "filesystem", "networking", "automation"],
    "axcontrol": ["control", "infrastructure", "runtime"],
    "phoenix": ["reasoning", "memory", "analysis"]
}
```

### Phase Order

`["origin", "event", "propagation", "observe", "interface", "failure", "boundary"]`

---

## SECTION 6 — Omni Orchestrator Integration

(Implemented in `kernel/omni_orchestrator_v1.py`)

---

## SECTION 7 — Capability Graph

(Configured in the Capability Registry)

---

## SECTION 8 — Runtime Control Loop

(Implemented in `kernel/runtime_kernel_v1.py`)

---

## SECTION 9 — Example Planning Cycle

(See `verify_planner_v2.py` for live demonstration)

---

## SECTION 10 — Integration Instructions

- **Deployment**: via `docker-compose`
- **Planner Role**: LLM as Policy Engine (`π(Ψ) → τ`)
- **Execution**: Restricted to `Ω (Omni Orchestrator)`

---

`APΩ Runtime = <State Manager> + <Planner Policy Engine> + <Canon Validator> + <Omni Orchestrator> + <Capability Graph> + <Skill Executors>`
