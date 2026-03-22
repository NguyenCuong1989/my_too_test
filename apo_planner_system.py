import os
import time
import json
import subprocess
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional
import uvicorn

app = FastAPI(title="APΩ Planner Service")

class PlannerRequest(BaseModel):
    state: Dict[str, Any]
    goal: str
    context: Dict[str, Any]
    allowed_capabilities: List[str] = Field(..., description="Array of allowed C masks")

class Task(BaseModel):
    task_id: str
    capability: str
    skill: str
    input: Dict[str, Any]
    depends_on: Optional[List[str]] = []

class PlannerResponse(BaseModel):
    tasks: List[Task]

def execute_planning_logic(request: PlannerRequest) -> PlannerResponse:
    # Deterministic LLM compiler logic boundary
    # In full runtime, this interfaces with LLM restricted by APΩ constraints
    return PlannerResponse(
        tasks=[
            Task(
                task_id="tau_01",
                capability="axcontrol",
                skill="audit_node",
                input={"target": "system_state"}
            )
        ]
    )

@app.post("/api/v1/planner", response_model=PlannerResponse)
async def planner_endpoint(request: PlannerRequest):
    allowed_set = {"factory", "axcontrol", "phoenix"}
    if not all(cap in allowed_set for cap in request.allowed_capabilities):
        raise HTTPException(status_code=400, detail="Violates allowed_capabilities constraint")

    plan = execute_planning_logic(request)
    return plan

# ==========================================
# SECTION 5 — Canon Validator
# ==========================================

CANONICAL_CAPABILITIES = {
    "factory": ["tele_node", "biz_node", "discord_node", "slack_node"],
    "axcontrol": ["audit_node", "guardian_node", "recovery_node", "runtime_check"],
    "phoenix": ["omega_core_agent", "antigravity_core_agent", "reasoning", "memory"]
}

class ValidationError(Exception):
    pass

class CanonValidator:
    def __init__(self):
        self.graph = CANONICAL_CAPABILITIES

    def validate(self, plan: PlannerResponse) -> PlannerResponse:
        task_ids = set()

        for task in plan.tasks:
            cap = task.capability
            skill = task.skill
            t_id = task.task_id

            if cap not in self.graph:
                raise ValidationError(f"Undefined Capability Vector: {cap}")
            if skill not in self.graph[cap]:
                raise ValidationError(f"Undefined Skill Mapping: {skill} in {cap}")

            task_ids.add(t_id)

        for task in plan.tasks:
            for dep in task.depends_on:
                if dep not in task_ids:
                    raise ValidationError(f"Orphaned DAG Dependency: {dep}")

        return plan

# ==========================================
# SECTION 7 — Omni Orchestrator Integration
# ==========================================

class OmniOrchestratorIntegration:
    def __init__(self):
        self.tau_results = {}

    def execute(self, validated_plan: PlannerResponse):
        for tau in validated_plan.tasks:
            skill = tau.skill
            params = tau.input
            tau_id = tau.task_id

            cmd = ["/Users/andy/my_too_test/omni", skill, json.dumps(params)]
            log_payload = {
                "component": "Π_dispatch",
                "action": "execute",
                "tau_id": tau_id,
                "cmd": cmd
            }
            log_payload["_ts"] = time.time()
            print(json.dumps(log_payload))

            try:
                env = os.environ.copy()
                env["PYTHONPATH"] = f"/Users/andy/my_too_test:{env.get('PYTHONPATH', '')}"
                out = subprocess.run(cmd, capture_output=True, text=True, check=True, env=env)

                result_log = {
                    "component": "exec",
                    "tau_id": tau_id,
                    "status": "success",
                    "output": out.stdout.strip()
                }
                result_log["_ts"] = time.time()
                print(json.dumps(result_log))

                self.tau_results[tau_id] = {"status": "success", "out": out.stdout}
            except subprocess.CalledProcessError as e:
                err_log = {
                    "component": "exec",
                    "tau_id": tau_id,
                    "status": "failure",
                    "error": e.stderr.strip()
                }
                err_log["_ts"] = time.time()
                print(json.dumps(err_log))

                self.tau_results[tau_id] = {"status": "failure", "err": e.stderr}
                break # Halt DAG execution on first failure

    def observe(self) -> Dict[str, Any]:
        has_critical_failure = any(r.get("status") == "failure" for r in self.tau_results.values())
        return {
            "metrics": self.tau_results,
            "lifecycle": "terminal" if has_critical_failure else "nominal"
        }

# ==========================================
# SECTION 6 — Runtime Control Loop
# ==========================================

class StateManager:
    def __init__(self):
        self.psi_state = {"lifecycle": "init", "tick": 0}

    def fetch_state(self) -> Dict[str, Any]:
        return self.psi_state

    def commit_state(self, delta: Dict[str, Any]):
        self.psi_state.update(delta)

def evaluate_goal_condition(psi: Dict[str, Any]) -> bool:
    return psi.get("lifecycle") in ["terminal", "fault"] or psi.get("tick", 0) >= 3

def runtime_execution_loop(goal: str, context: Dict[str, Any], allowed_caps: list):
    sm = StateManager()
    validator = CanonValidator()
    orchestrator = OmniOrchestratorIntegration()

    start_log = {
        "system": "ΣAPΩ",
        "action": "RUNTIME_CONTROL_LOOP_INITIATED",
        "goal": goal,
        "_ts": time.time()
    }
    print(json.dumps(start_log))

    while not evaluate_goal_condition(sm.fetch_state()):
        psi_t = sm.fetch_state()
        tick = psi_t.get("tick", 0)

        state_log = {
            "component": "Σ_gov",
            "tick": tick,
            "lifecycle_state": psi_t.get("lifecycle"),
            "_ts": time.time()
        }
        print(json.dumps(state_log))

        request = PlannerRequest(
            state=psi_t,
            goal=goal,
            context=context,
            allowed_capabilities=allowed_caps
        )

        pi_plan = execute_planning_logic(request)

        plan_log = {
            "component": "Π_plan",
            "atomic_tasks": len(pi_plan.tasks),
            "_ts": time.time()
        }
        print(json.dumps(plan_log))

        try:
            tau_dag = validator.validate(pi_plan)
        except ValidationError as e:
            sm.commit_state({"error": str(e), "lifecycle": "fault"})
            err_log = {
                "component": "Φ_valid",
                "status": "REJECTED",
                "reason": str(e),
                "_ts": time.time()
            }
            print(json.dumps(err_log))
            break

        orchestrator.execute(tau_dag)

        psi_t_plus_1 = orchestrator.observe()
        psi_t_plus_1["tick"] = tick + 1

        sm.commit_state(psi_t_plus_1)

    final_state = sm.fetch_state()
    end_log = {
        "system": "ΣAPΩ",
        "status": "RUNTIME_LOOP_TERMINATED",
        "final_lifecycle": final_state.get("lifecycle"),
        "_ts": time.time()
    }
    print(json.dumps(end_log))

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "run_loop":
        runtime_execution_loop(
            goal="Establish runtime dominance",
            context={"mode": "diagnostic"},
            allowed_caps=["factory", "axcontrol", "phoenix"]
        )
    else:
        init_log = {
            "system": "ΣAPΩ",
            "component": "Π_plan",
            "status": "STARTING_MICROSERVICE",
            "port": 8082,
            "_ts": time.time()
        }
        print(json.dumps(init_log))
        uvicorn.run(app, host="0.0.0.0", port=8082)
