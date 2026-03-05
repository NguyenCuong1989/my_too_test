import json

class StateManager:
    def __init__(self):
        self.state = {"status": "INIT"}
        self.finished = False
    def get_state(self):
        return self.state
    def observe(self):
        return {"status": "STABLE"}
    def update(self, new_state):
        self.state = new_state
    def goal_reached(self, goal):
        return self.finished

class RuntimeEngine:
    def __init__(self, planner, validator, orchestrator, state_manager):
        self.planner = planner
        self.validator = validator
        self.orchestrator = orchestrator
        self.state_manager = state_manager
    def run(self, goal):
        print(f"--- STARTING APΩ RUNTIME LOOP: {goal} ---")
        # For demo purposes, we run only one cycle
        state = self.state_manager.get_state()
        request = {
            "state": state,
            "goal": goal,
            "context": {},
            "allowed_capabilities": ["factory", "axcontrol", "phoenix"]
        }
        plan = self.planner.compute_plan(**request)
        print(f"[PLANNER] Plan generated: {json.dumps(plan)}")

        validated_plan = self.validator.validate(plan)
        print("[VALIDATOR] Plan validated.")

        self.orchestrator.execute(validated_plan)

        new_state = self.state_manager.observe()
        self.state_manager.update(new_state)
        self.state_manager.finished = True
        print("--- LOOP TERMINATED: GOAL ACHIEVED ---")

if __name__ == "__main__":
    from planner_v2 import PlannerEngine
    from validator_v2 import CanonValidator
    from orchestrator_v2 import OmniOrchestrator, CapabilityGraph

    engine = RuntimeEngine(
        planner=PlannerEngine(),
        validator=CanonValidator(),
        orchestrator=OmniOrchestrator(CapabilityGraph()),
        state_manager=StateManager()
    )
    engine.run("DEPLOY_CORE_V1")
