import time


class RuntimeKernel:

    def __init__(self, planner, validator, orchestrator, state_manager):

        self.planner = planner
        self.validator = validator
        self.orchestrator = orchestrator
        self.state_manager = state_manager


    def run(self, goal, allowed_capabilities=None):

        if allowed_capabilities is None:
            allowed_capabilities = ["factory", "axcontrol", "phoenix"]

        while True:

            # Ψ_t
            state = self.state_manager.get_state()

            # Π_plan
            plan = self.planner.build_plan(
                state,
                goal,
                {},
                allowed_capabilities
            )

            # V (Canon Verification)
            self.validator.validate(plan)

            # Ω (Omni Orchestrator)
            self.orchestrator.execute(plan)

            # Ω_obs
            new_state = self.state_manager.observe()

            if new_state.get("goal_achieved"):
                print(f"Goal {goal} achieved successfully.")
                break

            time.sleep(1) # Safety delay
