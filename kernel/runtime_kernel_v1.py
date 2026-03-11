class RuntimeKernel:

    def __init__(self, planner, validator, orchestrator, state_manager):
        """
        APΩ Runtime Control Loop
        Ψ_t → Π_plan → τ → Ω → Ψ_{t+1}
        """
        self.planner = planner
        self.validator = validator
        self.orchestrator = orchestrator
        self.state_manager = state_manager

    def run(self, goal: str):
        """
        Executes the deterministic control loop until the goal is reached.
        """
        print(f"Kernel: Starting Control Loop for goal: {goal}")
        
        while True:
            # 1. Observe State (Ψ_t)
            state = self.state_manager.observe()
            print(f"Kernel: Current State: {state}")

            # 2. Planning (Π_plan)
            # Standardized call signature
            plan = self.planner.build_plan(
                state=state,
                goal=goal,
                context={},
                allowed_capabilities=["factory", "axcontrol", "phoenix"]
            )

            # 3. Validation (V)
            # Enforces Canon
            self.validator.validate(plan)

            # 4. Orchestration (Ω)
            # Executes Task Graph (τ)
            self.orchestrator.execute(plan)

            # 5. Convergence Check (Ψ_{t+1})
            new_state = self.state_manager.observe()
            
            # Simple simulation: if goal is a capability that was just executed, we consider it reached
            # In real production, this would be a more complex goal check
            if new_state.get("goal_reached") or self._simulate_goal_check(plan, goal):
                print("Kernel: Goal convergence detected. Shutting down loop.")
                break

    def _simulate_goal_check(self, plan, goal):
        # Mock logic for simulation
        last_task = plan["tasks"][-1]
        if goal.lower() in last_task["capability"].lower() or goal.lower() in last_task["skill"].lower():
            return True
        return False
