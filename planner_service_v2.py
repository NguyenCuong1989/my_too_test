from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Optional
from kernel.adaptive_planner_v1 import AdaptivePlannerEngine
import uvicorn

# Mock persistence for the standalone service
class MockPersistence:
    pass

app = FastAPI(title="APΩ Planner Service", version="2.0.0")
planner_engine = AdaptivePlannerEngine(MockPersistence())

class PlannerRequest(BaseModel):
    state: Dict
    goal: str
    context: Dict = {}
    allowed_capabilities: List[str]

class Task(BaseModel):
    id: str
    phase: str
    capability: str
    skill: str
    input: Dict

class Edge(BaseModel):
    from_id: str
    to_id: str

class PlannerResponse(BaseModel):
    tasks: List[Task]
    edges: List[Edge]

@app.post("/planner", response_model=PlannerResponse)
async def planner_endpoint(req: PlannerRequest):
    """
    Standardized Planner Endpoint (APΩ-PLANNER-001)
    """
    print(f"Service: Received planning request for goal: {req.goal}")
    
    # Use the AdaptivePlannerEngine to build the plan
    plan = planner_engine.build_plan(
        state=req.state,
        goal=req.goal,
        context=req.context,
        allowed_capabilities=req.allowed_capabilities
    )
    
    # Convert kernel plan format to API response format if necessary
    # (The kernel now returns the standardized format)
    return plan

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
