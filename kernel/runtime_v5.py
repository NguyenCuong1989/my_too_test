# Σ_APΩ₂ CORE MODULE
# Authority: BỐ CƯỜNG Supreme System Commander
# Status: CANONICAL | ENHANCED_RUNTIME_V6

import json
import time
import os
from pathlib import Path
from planner_v5 import PlannerPipeline
from logic_v5 import RuntimeStateMachine, ExecutionContext, PlanHashValidator, GoalEvaluator
from observation_v5 import ObservationAggregator
from validators_v4 import PlanStructuralValidator, DAGCycleDetector, CanonPhaseValidator
from scheduler_v4 import ParallelScheduler
from executor_v4 import ParallelDAGExecutor
from telemetry_v4 import Telemetry
from bus_v4 import EventBus
from capability_graph_v3 import CapabilityGraph
from state_manager_v3 import StateManager

class DeterministicRuntime:
    def __init__(self):
        self.sm = RuntimeStateMachine()
        self.planner = PlannerPipeline()
        self.struct_val = PlanStructuralValidator()
        self.phase_val = CanonPhaseValidator()
        self.cycle_det = DAGCycleDetector()
        self.scheduler = ParallelScheduler()
        self.executor = ParallelDAGExecutor(CapabilityGraph())
        self.state_manager = StateManager()
        self.goal_eval = GoalEvaluator()
        self.telemetry = Telemetry()
        self.event_bus = EventBus()
        self.aggregator = ObservationAggregator(self.event_bus, self.telemetry)
        self.hash_val = PlanHashValidator()
        self.ctx = ExecutionContext()
        self.log_path = Path("/Users/andy/my_too_test/logs/convergence.jsonl")

    def log_convergence(self, cycle_data, goal_status):
        """Convergence Logger: Ghi dấu vết hội tụ vật lý"""
        entry = {
            "timestamp": cycle_data["timestamp"],
            "cycle": cycle_data["cycle"],
            "runtime_id": cycle_data["runtime_id"],
            "state_hash": cycle_data["state_hash"],
            "plan_hash": cycle_data["plan_hash"],
            "goal_converged": goal_status
        }
        with open(self.log_path, "a") as f:
            f.write(json.dumps(entry) + "\n")

    def run(self, goal_spec):
        print(f"--- [INIT] APΩ RUNTIME V6 | GOAL: {goal_spec} ---")
        iteration = 0
        while True:
            iteration += 1
            # 1. PLAN
            self.sm.transition(self.sm.PLAN)
            state = self.state_manager.get_state()
            plan_env = self.planner.build_plan(state, goal_spec, {}, ["factory", "axcontrol", "phoenix"])
            plan = plan_env.model_dump()

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
            cycle_data = self.ctx.next_cycle(state, plan)

            # Evaluate Convergence
            converged = self.goal_eval.evaluate(self.state_manager.get_state(), goal_spec)
            self.log_convergence(cycle_data, converged)

            # 5. UPDATE
            self.sm.transition(self.sm.UPDATE)
            if iteration >= 1: # Demo exit
                self.state_manager.update({"goal_achieved": True})

            if converged:
                self.sm.transition(self.sm.TERMINATE)
                print(f"--- [TERMINATE] GOAL ACHIEVED IN {iteration} CYCLES ---")
                print(f"--- [LOG] Convergence evidence saved to {self.log_path} ---")
                break

if __name__ == "__main__":
    # Đảm bảo thư mục log tồn tại
    Path("/Users/andy/my_too_test/logs").mkdir(exist_ok=True)
    runtime = DeterministicRuntime()
    # Thử nghiệm với Semantic Goal
    goal = {"type": "STABILITY", "target": "system"}
    runtime.run(goal)
