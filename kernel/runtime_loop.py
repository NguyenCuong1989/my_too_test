import time
import json
from typing import Dict, Any

class MockPlannerClient:
    def request_plan(self, state, goal, allowed_capabilities):
        return {
            "tasks": [
                {
                    "id": "t1",
                    "capability": "phoenix",
                    "skill": "analysis",
                    "input": {"target": goal},
                    "dependencies": [],
                    "phase": "Origin"
                },
                {
                    "id": "t2",
                    "capability": "factory",
                    "skill": "automation",
                    "input": {"action": "execute"},
                    "dependencies": ["t1"],
                    "phase": "Event"
                }
            ]
        }

class MockOrchestrator:
    def dispatch(self, plan):
        print(f"Executing plan: {json.dumps(plan)}")

def observe() -> Dict[str, Any]:
    return {"status": "OBSERVING", "metrics": {}}

def goal_reached(state: Dict, goal: str) -> bool:
    return state.get("status") == "SEALED"

def execute_loop(goal: str, planner_client, orchestrator):
    from canon_validator import CanonValidator
    state = observe()
    iteration = 0
    max_iterations = 2

    while not goal_reached(state, goal) and iteration < max_iterations:
        iteration += 1
        raw_plan = planner_client.request_plan(
            state=state,
            goal=goal,
            allowed_capabilities=["factory", "axcontrol", "phoenix"]
        )

        try:
            validated_plan = CanonValidator.validate(raw_plan)
            orchestrator.dispatch(validated_plan)
            state = {"status": "SEALED"}
        except ValueError as e:
            print(f"Plan Rejected: {e}")
            state = {"status": "INVALID", "error": str(e)}
            break

if __name__ == "__main__":
    execute_loop("Test APΩ Loop", MockPlannerClient(), MockOrchestrator())
