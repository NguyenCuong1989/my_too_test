import uuid
import time
from typing import Dict, List, Any
from pydantic import BaseModel

class Task(BaseModel):
    id: str
    phase: str
    capability: str
    skill: str
    input: Dict[str, Any]

class PlanEnvelope(BaseModel):
    plan_id: str
    created_at: int
    planner_version: str
    tasks: List[Task]
    edges: List[Dict[str, str]]

class PlannerPipeline:
    def __init__(self, engine_version="1.0.0"):
        self.version = engine_version

    def build_plan(self, state, goal, context, allowed_caps) -> PlanEnvelope:
        t1_id = str(uuid.uuid4())
        t2_id = str(uuid.uuid4())
        tasks = [
            Task(id=t1_id, phase="origin", capability="phoenix", skill="analysis", input={"dataset": state}),
            Task(id=t2_id, phase="event", capability="factory", skill="deploy", input={"target": "runtime", "artifact": goal})
        ]
        edges = [{"from": t1_id, "to": t2_id}]
        return PlanEnvelope(
            plan_id=str(uuid.uuid4()),
            created_at=int(time.time()),
            planner_version=self.version,
            tasks=tasks,
            edges=edges
        )
