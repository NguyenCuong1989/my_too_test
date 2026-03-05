import json
import time
from runtime_v5 import DeterministicRuntime
from persistence_v7 import PersistenceLayer, CheckpointManager
from logic_v5 import ExecutionContext
from adaptive_planner_v1 import AdaptivePlannerEngine

class PersistentRuntime(DeterministicRuntime):
    def __init__(self):
        super().__init__()
        self.persistence = PersistenceLayer()
        self.checkpoint_manager = CheckpointManager(self.persistence)
        self.planner = AdaptivePlannerEngine(self.persistence)
        # Use existing context from DeterministicRuntime

    def run(self, goal_spec):
        print(f"--- [INIT] APΩ PERSISTENT RUNTIME | GOAL: {goal_spec} ---")
        iteration = 0
        while True:
            iteration += 1
            # 1. PLAN
            self.sm.transition(self.sm.PLAN)
            state = self.state_manager.get_state()
            plan_env = self.planner.build_plan(state, goal_spec, {}, ["factory", "axcontrol", "phoenix"])
            plan = plan_env.model_dump()

            # Save Plan to Persistence
            ctx_data = self.ctx.next_cycle(state, plan)
            self.persistence.save_plan(ctx_data["runtime_id"], ctx_data["cycle"], ctx_data["plan_hash"], plan)

            # 2. VALIDATE
            self.sm.transition(self.sm.VALIDATE)
            self.hash_val.validate(plan)
            self.struct_val.validate(plan)
            self.phase_val.validate_phases(plan["tasks"])

            # 3. EXECUTE
            self.sm.transition(self.sm.EXECUTE)
            self.executor.execute(plan)

            # 4. OBSERVE & LOG
            self.sm.transition(self.sm.OBSERVE)

            # Save Task Results (Simplified mapping)
            for task in plan["tasks"]:
                self.persistence.save_task(plan["plan_id"], task)

            # 5. UPDATE & CONVERGENCE
            self.sm.transition(self.sm.UPDATE)
            new_state = self.state_manager.get_state()

            # Save State & Convergence
            converged = self.goal_eval.evaluate(new_state, goal_spec)
            self.persistence.save_state(ctx_data["runtime_id"], ctx_data["cycle"], ctx_data["state_hash"], new_state)
            self.persistence.save_convergence(ctx_data["runtime_id"], ctx_data["cycle"], ctx_data["state_hash"], ctx_data["plan_hash"], converged)

            # Internal logic update
            if iteration >= 1:
                self.state_manager.update({"goal_achieved": True})

            if converged:
                self.sm.transition(self.sm.TERMINATE)
                print(f"--- [TERMINATE] GOAL ACHIEVED IN {iteration} CYCLES ---")
                print(f"--- [DB] Records persisted to runtime.db ---")
                break

if __name__ == "__main__":
    runtime = PersistentRuntime()
    goal = {"type": "STABILITY", "target": "system"}
    runtime.run(goal)
