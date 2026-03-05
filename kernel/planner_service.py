import json
from typing import Dict, List, Any
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="APΩ Planner Service")

class Task(BaseModel):
    id: str
    capability: str
    skill: str
    input: Dict[str, Any]
    dependencies: List[str] = []
    phase: str

class PlannerRequest(BaseModel):
    state: Dict[str, Any]
    goal: str
    context: Dict[str, Any] = {}
    allowed_capabilities: List[str]

class PlannerResponse(BaseModel):
    tasks: List[Task]

def compute_plan(state: Dict, goal: str, capabilities: List[str]) -> List[Task]:
    if "factory" not in capabilities:
        raise ValueError("Factory capability required for baseline operations.")
    return [
        Task(
            id="t1",
            capability="phoenix",
            skill="analysis",
            input={"target": goal, "state_diff": state},
            dependencies=[],
            phase="Origin"
        ),
        Task(
            id="t2",
            capability="factory",
            skill="automation",
            input={"action": "execute_derived_logic"},
            dependencies=["t1"],
            phase="Event"
        )
    ]

@app.post("/planner", response_model=PlannerResponse)
async def create_plan(request: PlannerRequest):
    try:
        tasks = compute_plan(
            state=request.state,
            goal=request.goal,
            capabilities=request.allowed_capabilities
        )
        return PlannerResponse(tasks=tasks)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
