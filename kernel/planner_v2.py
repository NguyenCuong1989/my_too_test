from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI()

class PlannerRequest(BaseModel):
    state: Dict[str, Any]
    goal: str
    context: Dict[str, Any]
    allowed_capabilities: List[str]

class Task(BaseModel):
    capability: str
    skill: str
    input: Dict[str, Any]

class PlannerResponse(BaseModel):
    tasks: List[Task]

class PlannerEngine:
    def compute_plan(self, state, goal, context, allowed_capabilities):
        tasks = []
        if "factory" in allowed_capabilities:
            tasks.append({
                "capability": "factory",
                "skill": "deploy",
                "input": {
                    "goal": goal
                }
            })
        return {"tasks": tasks}

planner = PlannerEngine()

@app.post("/planner", response_model=PlannerResponse)
def planner_endpoint(request: PlannerRequest):
    plan = planner.compute_plan(
        request.state,
        request.goal,
        request.context,
        request.allowed_capabilities
    )
    return plan
