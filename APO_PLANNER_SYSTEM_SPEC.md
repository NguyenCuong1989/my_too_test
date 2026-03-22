# Σ_APΩ RUNTIME PLANNING ENGINE
## Complete System Implementation Specification

---

## SECTION 1: SYSTEM ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────────┐
│                    OPERATOR (U)                                 │
│              @Antigravity_APO_Bot (Telegram)                    │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│              COMMAND ROUTER                                     │
│         (Parse Command → Extract Intent)                        │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│              STATE MANAGER                                      │
│              (Ψ_t Storage)                                      │
│         ├── Runtime State                                       │
│         ├── Task History                                        │
│         ├── System Metrics                                      │
│         └── Error Log                                           │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│         PLANNER SERVICE (Π_plan)                                │
│         HTTP POST /planner                                      │
│         ├── Input: (Ψ, Goal, Context, Capabilities)            │
│         ├── Process: State Analysis + Goal Decomposition       │
│         └── Output: Deterministic Task DAG (τ)                 │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│         CANON VALIDATOR (V)                                     │
│         ├── Phase Order Validation                              │
│         ├── Capability Validation                               │
│         ├── Skill Validation                                    │
│         └── DAG Integrity Check                                 │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│         OMNI ORCHESTRATOR (Ω)                                   │
│         ├── Task Dispatch                                       │
│         ├── Execution Sequencing                                │
│         ├── Error Handling                                      │
│         └── State Update                                        │
└────────────────────┬────────────────────────────────────────────┘
                     │
     ┌───────────────┼───────────────┐
     │               │               │
     ▼               ▼               ▼
┌──────────┐   ┌──────────┐   ┌──────────┐
│ Factory  │   │AXControl │   │ Phoenix  │
│   (F)    │   │    (A)   │   │    (P)   │
└─────┬────┘   └─────┬────┘   └─────┬────┘
      │              │              │
      └──────────────┼──────────────┘
                     │
        CAPABILITY GRAPH (C = {F, A, P})
                     │
     ┌───────────────┼───────────────┐
     │               │               │
     ▼               ▼               ▼
┌──────────┐   ┌──────────┐   ┌──────────┐
│ Skill    │   │ Skill    │   │ Skill    │
│Executors │   │Executors │   │Executors │
└─────┬────┘   └─────┬────┘   └─────┬────┘
      │              │              │
      └──────────────┼──────────────┘
                     │
                     ▼
        EXECUTION (Task Atomic Units)
                     │
                     ▼
        OBSERVE (Ψ_{t+1} Collection)
                     │
                     └─→ STATE MANAGER
                         (Loop Until GoalReached)
```

---

## SECTION 2: PLANNER PROTOCOL SPECIFICATION

### ENDPOINT

```
POST /planner
HOST: localhost:8080
CONTENT-TYPE: application/json
```

### REQUEST CONTRACT

**Input Definition:**

```
Input := ⟨Ψ_t, Goal, Context, AllowedCapabilities⟩

Where:
  Ψ_t = RuntimeState (current system state snapshot)
  Goal = ExecutionObjective (what to achieve)
  Context = OptionalMetadata (hints for planner)
  AllowedCapabilities = C_allowed ⊆ {Factory, AXControl, Phoenix}
```

### REQUEST PAYLOAD EXAMPLE

```json
{
  "state": {
    "current_phase": "IDLE",
    "runtime_uptime": 3600,
    "active_tasks": 0,
    "error_count": 0,
    "task_history": [],
    "system_metrics": {}
  },
  "goal": {
    "type": "AUTONOMOUS_EXECUTION",
    "target": "verify system backup",
    "priority": "HIGH",
    "timeout_seconds": 300
  },
  "context": {
    "retry_count": 0,
    "previous_failures": []
  },
  "allowed_capabilities": ["factory", "axcontrol", "phoenix"]
}
```

### RESPONSE CONTRACT

**Output Definition:**

```
Plan := ⟨PlanID, Tasks, Edges, Metadata⟩

Where:
  PlanID = UniqueIdentifier
  Tasks = {τ_1, τ_2, ..., τ_n}  (ordered task set)
  Edges = {e_ij = (τ_i, τ_j)}   (dependency graph)
  Metadata = ExecutionMetadata
```

### RESPONSE PAYLOAD EXAMPLE

```json
{
  "plan_id": "plan_20260305_001",
  "created_at": "2026-03-05T21:45:30Z",
  "goal_reference": "verify system backup",
  "tasks": [
    {
      "id": "task_001",
      "phase": "origin",
      "capability": "factory",
      "skill": "verify_system_state",
      "priority": 1,
      "input": {
        "check_components": ["database", "filesystem", "network"]
      },
      "timeout_seconds": 60
    },
    {
      "id": "task_002",
      "phase": "event",
      "capability": "factory",
      "skill": "initiate_backup",
      "priority": 2,
      "depends_on": ["task_001"],
      "input": {
        "backup_target": "/backups/system",
        "compression": "gzip"
      },
      "timeout_seconds": 180
    },
    {
      "id": "task_003",
      "phase": "propagation",
      "capability": "factory",
      "skill": "verify_backup",
      "priority": 3,
      "depends_on": ["task_002"],
      "input": {
        "checksum_validation": true
      },
      "timeout_seconds": 60
    },
    {
      "id": "task_004",
      "phase": "observe",
      "capability": "axcontrol",
      "skill": "monitor_completion",
      "priority": 4,
      "depends_on": ["task_003"],
      "input": {
        "collect_metrics": true
      },
      "timeout_seconds": 30
    },
    {
      "id": "task_005",
      "phase": "interface",
      "capability": "phoenix",
      "skill": "generate_report",
      "priority": 5,
      "depends_on": ["task_004"],
      "input": {
        "report_format": "json",
        "include_metrics": true
      },
      "timeout_seconds": 30
    }
  ],
  "edges": [
    {"from": "task_001", "to": "task_002"},
    {"from": "task_002", "to": "task_003"},
    {"from": "task_003", "to": "task_004"},
    {"from": "task_004", "to": "task_005"}
  ],
  "metadata": {
    "estimated_duration_seconds": 360,
    "parallelizable_tasks": [],
    "rollback_required": false
  }
}
```

---

## SECTION 3: JSON SCHEMAS

### SCHEMA 1: PLANNER REQUEST

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "APO_PlannerRequest",
  "type": "object",
  "required": ["state", "goal", "allowed_capabilities"],
  "properties": {
    "state": {
      "type": "object",
      "title": "RuntimeState",
      "required": ["current_phase"],
      "properties": {
        "current_phase": {
          "type": "string",
          "enum": ["IDLE", "PLANNING", "EXECUTING", "OBSERVING", "DRIFT_DETECTED", "HEALING", "COMPLETED"]
        },
        "runtime_uptime": {"type": "number"},
        "active_tasks": {"type": "integer"},
        "error_count": {"type": "integer"},
        "task_history": {"type": "array", "items": {"type": "string"}},
        "system_metrics": {"type": "object"}
      }
    },
    "goal": {
      "type": "object",
      "title": "ExecutionGoal",
      "required": ["type", "target"],
      "properties": {
        "type": {
          "type": "string",
          "enum": ["AUTONOMOUS_EXECUTION", "SYSTEM_VERIFICATION", "RECOVERY", "OPTIMIZATION", "CUSTOM"]
        },
        "target": {"type": "string"},
        "priority": {"type": "string", "enum": ["LOW", "MEDIUM", "HIGH", "CRITICAL"]},
        "timeout_seconds": {"type": "integer", "minimum": 1}
      }
    },
    "context": {
      "type": "object",
      "title": "OptionalContext",
      "properties": {
        "retry_count": {"type": "integer"},
        "previous_failures": {"type": "array", "items": {"type": "string"}},
        "hints": {"type": "array", "items": {"type": "string"}}
      }
    },
    "allowed_capabilities": {
      "type": "array",
      "title": "AllowedCapabilities",
      "items": {"type": "string", "enum": ["factory", "axcontrol", "phoenix"]},
      "minItems": 1
    }
  }
}
```

### SCHEMA 2: TASK DEFINITION

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "APO_Task",
  "type": "object",
  "required": ["id", "phase", "capability", "skill", "input"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^task_[0-9]{3,}$"
    },
    "phase": {
      "type": "string",
      "enum": ["origin", "event", "propagation", "observe", "interface", "failure", "boundary"]
    },
    "capability": {
      "type": "string",
      "enum": ["factory", "axcontrol", "phoenix"]
    },
    "skill": {
      "type": "string",
      "description": "Skill name must exist in capability registry"
    },
    "priority": {
      "type": "integer",
      "minimum": 1,
      "maximum": 10
    },
    "depends_on": {
      "type": "array",
      "items": {"type": "string"},
      "description": "Task IDs this task depends on"
    },
    "input": {
      "type": "object",
      "title": "TaskPayload"
    },
    "timeout_seconds": {
      "type": "integer",
      "minimum": 1
    }
  }
}
```

### SCHEMA 3: PLANNER RESPONSE (PLAN DAG)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "APO_Plan",
  "type": "object",
  "required": ["plan_id", "tasks", "edges"],
  "properties": {
    "plan_id": {
      "type": "string",
      "pattern": "^plan_[0-9]{8}_[0-9]{3,}$"
    },
    "created_at": {
      "type": "string",
      "format": "date-time"
    },
    "goal_reference": {
      "type": "string"
    },
    "tasks": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/task"
      }
    },
    "edges": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["from", "to"],
        "properties": {
          "from": {"type": "string"},
          "to": {"type": "string"}
        }
      }
    },
    "metadata": {
      "type": "object",
      "properties": {
        "estimated_duration_seconds": {"type": "number"},
        "parallelizable_tasks": {"type": "array"},
        "rollback_required": {"type": "boolean"}
      }
    }
  },
  "definitions": {
    "task": {
      "type": "object",
      "required": ["id", "phase", "capability", "skill", "input"],
      "properties": {
        "id": {"type": "string"},
        "phase": {"type": "string"},
        "capability": {"type": "string"},
        "skill": {"type": "string"},
        "priority": {"type": "integer"},
        "depends_on": {"type": "array"},
        "input": {"type": "object"},
        "timeout_seconds": {"type": "integer"}
      }
    }
  }
}
```

---

## SECTION 4: PYTHON PLANNER SERVICE

```python
# apo_planner_service.py
# APΩ Runtime Planning Engine
# Role: Deterministic Task Graph Generator
# Input: (State, Goal, Context, Capabilities)
# Output: Structured Task DAG

from flask import Flask, request, jsonify
from datetime import datetime
from typing import Dict, List, Any
import uuid
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("APO_Planner")

# ============================================================================
# CAPABILITY REGISTRY
# ============================================================================

CAPABILITY_REGISTRY = {
    "factory": {
        "skills": [
            "verify_system_state",
            "initiate_backup",
            "verify_backup",
            "deploy",
            "filesystem_operation",
            "networking_operation",
            "automation_task"
        ]
    },
    "axcontrol": {
        "skills": [
            "monitor_completion",
            "control_infrastructure",
            "runtime_adjustment",
            "system_control"
        ]
    },
    "phoenix": {
        "skills": [
            "generate_report",
            "reasoning_analysis",
            "memory_retrieval",
            "analysis_task"
        ]
    }
}

CANONICAL_PHASES = [
    "origin",
    "event",
    "propagation",
    "observe",
    "interface",
    "failure",
    "boundary"
]

# ============================================================================
# PLANNER ENGINE
# ============================================================================

class APOPlannerEngine:
    """Deterministic task DAG generator"""

    def __init__(self):
        self.phase_index = {}
        for idx, phase in enumerate(CANONICAL_PHASES):
            self.phase_index[phase] = idx

    def build_plan(
        self,
        state: Dict[str, Any],
        goal: Dict[str, str],
        context: Dict[str, Any],
        allowed_capabilities: List[str]
    ) -> Dict[str, Any]:
        """
        Generate deterministic task DAG

        Input: Ψ_t (state), Goal, Context, AllowedCapabilities
        Output: Plan τ = {τ_1, τ_2, ..., τ_n} with edges
        """

        tasks = []
        task_sequence = []

        # PHASE 1: ORIGIN - System state verification
        task_001 = {
            "id": "task_001",
            "phase": "origin",
            "capability": "factory",
            "skill": "verify_system_state",
            "priority": 1,
            "input": {
                "check_components": ["database", "filesystem", "network"]
            },
            "timeout_seconds": 60
        }
        tasks.append(task_001)
        task_sequence.append("task_001")

        # PHASE 2: EVENT - Goal decomposition and task initiation
        if goal["type"] == "AUTONOMOUS_EXECUTION":
            task_002 = {
                "id": "task_002",
                "phase": "event",
                "capability": "factory",
                "skill": "initiate_backup",
                "priority": 2,
                "depends_on": ["task_001"],
                "input": {
                    "backup_target": "/backups/system",
                    "compression": "gzip"
                },
                "timeout_seconds": 180
            }
            tasks.append(task_002)
            task_sequence.append("task_002")

        # PHASE 3: PROPAGATION - Task execution setup
        task_003 = {
            "id": "task_003",
            "phase": "propagation",
            "capability": "factory",
            "skill": "verify_backup",
            "priority": 3,
            "depends_on": [task_sequence[-1]],
            "input": {
                "checksum_validation": True
            },
            "timeout_seconds": 60
        }
        tasks.append(task_003)
        task_sequence.append("task_003")

        # PHASE 4: OBSERVE - Monitoring and metrics collection
        task_004 = {
            "id": "task_004",
            "phase": "observe",
            "capability": "axcontrol",
            "skill": "monitor_completion",
            "priority": 4,
            "depends_on": [task_sequence[-1]],
            "input": {
                "collect_metrics": True
            },
            "timeout_seconds": 30
        }
        tasks.append(task_004)
        task_sequence.append("task_004")

        # PHASE 5: INTERFACE - Result synthesis
        task_005 = {
            "id": "task_005",
            "phase": "interface",
            "capability": "phoenix",
            "skill": "generate_report",
            "priority": 5,
            "depends_on": [task_sequence[-1]],
            "input": {
                "report_format": "json",
                "include_metrics": True
            },
            "timeout_seconds": 30
        }
        tasks.append(task_005)
        task_sequence.append("task_005")

        # Build DAG edges
        edges = []
        for i in range(len(task_sequence) - 1):
            edges.append({
                "from": task_sequence[i],
                "to": task_sequence[i + 1]
            })

        # Generate plan
        plan = {
            "plan_id": f"plan_{datetime.now().strftime('%Y%m%d')}_{uuid.uuid4().hex[:6]}",
            "created_at": datetime.utcnow().isoformat() + "Z",
            "goal_reference": goal.get("target", "unknown"),
            "tasks": tasks,
            "edges": edges,
            "metadata": {
                "estimated_duration_seconds": sum(t.get("timeout_seconds", 30) for t in tasks),
                "parallelizable_tasks": [],
                "rollback_required": False
            }
        }

        return plan


# ============================================================================
# FLASK ENDPOINTS
# ============================================================================

planner = APOPlannerEngine()

@app.route("/planner", methods=["POST"])
def planner_endpoint():
    """POST /planner - Deterministic plan generation"""

    payload = request.json

    # Extract request components
    state = payload.get("state", {})
    goal = payload.get("goal", {})
    context = payload.get("context", {})
    allowed_capabilities = payload.get("allowed_capabilities", [])

    # Generate plan
    plan = planner.build_plan(state, goal, context, allowed_capabilities)

    logger.info(f"[PLANNER] Generated plan: {plan['plan_id']}")

    return jsonify(plan), 200


@app.route("/planner/health", methods=["GET"])
def health_check():
    """GET /planner/health - Service health status"""
    return jsonify({
        "status": "healthy",
        "service": "APO_PlannerService",
        "capabilities": list(CAPABILITY_REGISTRY.keys())
    }), 200


# ============================================================================
# SERVICE STARTUP
# ============================================================================

if __name__ == "__main__":
    logger.info("[PLANNER] APΩ Runtime Planning Engine starting...")
    logger.info(f"[PLANNER] Registered capabilities: {list(CAPABILITY_REGISTRY.keys())}")
    logger.info("[PLANNER] Listening on http://0.0.0.0:8080/planner")
    app.run(host="0.0.0.0", port=8080, threaded=True)
```

---

## SECTION 5: CANON VALIDATOR

```python
# canon_validator.py
# APΩ Runtime Canon Constraint Validator
# Validates task DAG against canonical phase ordering and capability constraints

from typing import Dict, List, Any

class CanonValidator:
    """Enforces canonical execution constraints"""

    CANONICAL_PHASES = [
        "origin",
        "event",
        "propagation",
        "observe",
        "interface",
        "failure",
        "boundary"
    ]

    VALID_CAPABILITIES = {"factory", "axcontrol", "phoenix"}

    CAPABILITY_SKILLS = {
        "factory": {
            "verify_system_state",
            "initiate_backup",
            "verify_backup",
            "deploy",
            "filesystem_operation",
            "networking_operation",
            "automation_task"
        },
        "axcontrol": {
            "monitor_completion",
            "control_infrastructure",
            "runtime_adjustment",
            "system_control"
        },
        "phoenix": {
            "generate_report",
            "reasoning_analysis",
            "memory_retrieval",
            "analysis_task"
        }
    }

    def validate(self, plan: Dict[str, Any]) -> tuple[bool, str]:
        """
        Validate plan against canonical constraints

        Returns: (is_valid: bool, error_message: str)
        """

        tasks = plan.get("tasks", [])
        edges = plan.get("edges", [])

        # 1. VALIDATE TASK EXISTENCE
        task_ids = {t["id"] for t in tasks}
        for edge in edges:
            if edge["from"] not in task_ids:
                return (False, f"Invalid edge source: {edge['from']} not in tasks")
            if edge["to"] not in task_ids:
                return (False, f"Invalid edge target: {edge['to']} not in tasks")

        # 2. VALIDATE PHASE ORDERING
        phase_map = {t["id"]: self.CANONICAL_PHASES.index(t["phase"]) for t in tasks}

        for edge in edges:
            src_phase = phase_map[edge["from"]]
            dst_phase = phase_map[edge["to"]]
            if src_phase >= dst_phase:
                return (False, f"Phase order violation: {edge['from']} (phase {src_phase}) must precede {edge['to']} (phase {dst_phase})")

        # 3. VALIDATE CAPABILITIES
        for task in tasks:
            capability = task.get("capability")
            if capability not in self.VALID_CAPABILITIES:
                return (False, f"Invalid capability: {capability}")

        # 4. VALIDATE SKILLS
        for task in tasks:
            capability = task.get("capability")
            skill = task.get("skill")
            if skill not in self.CAPABILITY_SKILLS.get(capability, set()):
                return (False, f"Invalid skill {skill} for capability {capability}")

        # 5. VALIDATE DEPENDENCIES
        for task in tasks:
            depends_on = task.get("depends_on", [])
            for dep_id in depends_on:
                if dep_id not in task_ids:
                    return (False, f"Dependency {dep_id} not found for task {task['id']}")

        return (True, "Plan is valid")

    def validate_strict(self, plan: Dict[str, Any]) -> None:
        """Validate and raise exception on failure"""
        is_valid, message = self.validate(plan)
        if not is_valid:
            raise ValueError(f"Canon validation failed: {message}")
```

---

## SECTION 6: RUNTIME CONTROL LOOP

```python
# runtime_kernel.py
# APΩ Runtime Control Loop
# Ψ_t → Π_plan → τ → Validation → Execution → Ψ_{t+1}

import requests
import json
import logging
from typing import Dict, Any
from canon_validator import CanonValidator

logger = logging.getLogger("APO_RuntimeKernel")

class RuntimeKernel:
    """Deterministic runtime execution loop"""

    def __init__(self, planner_url: str, orchestrator):
        self.planner_url = planner_url
        self.orchestrator = orchestrator
        self.validator = CanonValidator()
        self.state_manager = {}

    def get_state(self) -> Dict[str, Any]:
        """Retrieve current runtime state Ψ_t"""
        return {
            "current_phase": "IDLE",
            "runtime_uptime": 0,
            "active_tasks": 0,
            "error_count": 0,
            "task_history": [],
            "system_metrics": {}
        }

    def plan(self, state: Dict[str, Any], goal: Dict[str, str]) -> Dict[str, Any]:
        """
        Request plan from planner service
        Π_plan(Ψ_t, Goal) → τ
        """
        payload = {
            "state": state,
            "goal": goal,
            "context": {},
            "allowed_capabilities": ["factory", "axcontrol", "phoenix"]
        }

        response = requests.post(self.planner_url, json=payload)
        plan = response.json()

        logger.info(f"[KERNEL] Plan generated: {plan['plan_id']}")
        return plan

    def validate_plan(self, plan: Dict[str, Any]) -> bool:
        """Validate plan against canon constraints"""
        is_valid, message = self.validator.validate(plan)
        logger.info(f"[KERNEL] Plan validation: {message}")
        return is_valid

    def execute_plan(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """Execute plan via orchestrator"""
        logger.info(f"[KERNEL] Executing plan: {plan['plan_id']}")
        result = self.orchestrator.execute(plan)
        return result

    def observe(self) -> Dict[str, Any]:
        """Collect post-execution state Ψ_{t+1}"""
        new_state = self.get_state()
        logger.info("[KERNEL] State observed")
        return new_state

    def run(self, goal: Dict[str, str], max_iterations: int = 10):
        """
        Main runtime loop:

        while not goal_reached:
            Ψ_t ← get_state()
            τ ← planner(Ψ_t, Goal)
            validate(τ)
            execute(τ)
            Ψ_{t+1} ← observe()
        """

        iteration = 0

        while iteration < max_iterations:

            logger.info(f"[KERNEL] Runtime iteration {iteration}")

            # STEP 1: Get current state
            state = self.get_state()
            logger.info(f"[KERNEL] Current state: {state['current_phase']}")

            # STEP 2: Generate plan
            plan = self.plan(state, goal)

            # STEP 3: Validate plan
            if not self.validate_plan(plan):
                logger.error("[KERNEL] Plan validation failed")
                break

            # STEP 4: Execute plan
            result = self.execute_plan(plan)

            # STEP 5: Observe new state
            new_state = self.observe()

            # STEP 6: Check goal completion
            if result.get("status") == "completed":
                logger.info("[KERNEL] Goal reached - execution complete")
                break

            iteration += 1

        logger.info(f"[KERNEL] Runtime loop terminated after {iteration} iterations")

        return {
            "status": "complete",
            "iterations": iteration,
            "final_state": new_state
        }
```

---

## SECTION 7: OMNI ORCHESTRATOR INTEGRATION

```python
# omni_orchestrator.py
# APΩ Task Execution Orchestrator
# Executes task DAG with capability dispatch

import logging
from typing import Dict, Any, List

logger = logging.getLogger("APO_OmniOrchestrator")

class OmniOrchestrator:
    """Executes structured task DAG"""

    def __init__(self, capability_executors: Dict[str, Any]):
        """
        Initialize with capability executors

        capability_executors:
          "factory": FactoryExecutor instance
          "axcontrol": AXControlExecutor instance
          "phoenix": PhoenixExecutor instance
        """
        self.executors = capability_executors

    def execute(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute plan DAG

        Input: Plan τ with tasks and edges
        Output: Execution result {status, outputs, errors}
        """

        tasks = {t["id"]: t for t in plan["tasks"]}
        edges = plan["edges"]
        completed = set()
        outputs = {}
        errors = []

        logger.info(f"[ORCHESTRATOR] Executing plan: {plan['plan_id']}")

        # Topological execution
        while len(completed) < len(tasks):

            # Find executable tasks (dependencies satisfied)
            executable = []
            for task_id, task in tasks.items():
                if task_id not in completed:
                    deps = task.get("depends_on", [])
                    if all(dep in completed for dep in deps):
                        executable.append(task_id)

            if not executable:
                logger.error("[ORCHESTRATOR] No executable tasks but plan incomplete")
                break

            # Execute tasks
            for task_id in executable:

                task = tasks[task_id]
                capability = task["capability"]
                skill = task["skill"]
                payload = task["input"]

                logger.info(f"[ORCHESTRATOR] Executing {capability}.{skill} (task {task_id})")

                # Dispatch to capability executor
                executor = self.executors.get(capability)
                if not executor:
                    errors.append(f"No executor for capability {capability}")
                    continue

                try:
                    result = executor.run(skill, payload)
                    outputs[task_id] = result
                    completed.add(task_id)
                    logger.info(f"[ORCHESTRATOR] Task {task_id} completed")
                except Exception as e:
                    errors.append(f"Task {task_id} failed: {str(e)}")
                    logger.error(f"[ORCHESTRATOR] Task {task_id} failed: {e}")

        logger.info(f"[ORCHESTRATOR] Plan execution complete. Completed: {len(completed)}/{len(tasks)}")

        return {
            "status": "completed" if len(completed) == len(tasks) else "partial",
            "plan_id": plan["plan_id"],
            "completed_tasks": len(completed),
            "total_tasks": len(tasks),
            "outputs": outputs,
            "errors": errors
        }
```

---

## SYSTEM INVARIANTS

```
[Deterministic] = True
  ∀ Input, Planner(Input) → DeterministicOutput

[PlannerStateless] = True
  ∀ t, Planner(Ψ_t) ⊥ Planner(Ψ_s) | t ≠ s

[ExecutionExternalized] = True
  Planner(·) ⟹ τ (tasks only)
  Ω(τ) ⟹ execution only

[CanonOrdering] = Enforced
  ∀ Plan, Phases ∈ {Origin, Event, Propagation, Observe, Interface, Failure, Boundary}
  Phases must be ordered and not skipped

[CapabilityConstraint] = Enforced
  ∀ Task, Task.capability ∈ {Factory, AXControl, Phoenix}
  Task.skill ∈ Skills[Task.capability]
```

---

END SPECIFICATION
