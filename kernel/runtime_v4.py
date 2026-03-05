from registry_v4 import CapabilityRegistry
from validators_v4 import SkillSchemaValidator, PlanStructuralValidator, DAGCycleDetector, CanonPhaseValidator
from scheduler_v4 import ParallelScheduler
from executor_v4 import ParallelDAGExecutor
from telemetry_v4 import Telemetry, FailureManager
from bus_v4 import EventBus
from dag_planner_v3 import DAGPlanner
from capability_graph_v3 import CapabilityGraph
from state_manager_v3 import StateManager

class APOmegaRuntime:
    def __init__(self, planner, structural_validator, cycle_detector, phase_validator, orchestrator, state_manager, telemetry, event_bus):
        self.planner = planner
        self.structural_validator = structural_validator
        self.cycle_detector = cycle_detector
        self.phase_validator = phase_validator
        self.orchestrator = orchestrator
        self.state_manager = state_manager
        self.telemetry = telemetry
        self.event_bus = event_bus

    def run(self, goal):
        print(f"--- STARTING FULL APΩ PIPELINE: GOAL={goal} ---")
        while True:
            cycle_timer = self.telemetry.measure("runtime_cycle_time")
            state = self.state_manager.get_state()

            # 1. Plan
            plan_timer = self.telemetry.measure("planner_latency")
            plan = self.planner.build_plan(state, goal, {}, ["factory", "axcontrol", "phoenix"])
            plan_timer()

            # 2. Validate
            self.structural_validator.validate(plan)
            if self.cycle_detector.has_cycle(plan):
                raise Exception("Plan contains a cycle")
            self.phase_validator.validate_phases(plan["tasks"])

            # 3. Execute
            exec_timer = self.telemetry.measure("task_execution_time")
            self.orchestrator.execute(plan)
            exec_timer()

            # 4. Observe
            observation = self.state_manager.observe()
            self.state_manager.update(observation)

            cycle_timer()
            self.event_bus.publish("CYCLE_COMPLETED", {"goal": goal})

            if self.state_manager.goal_reached(goal):
                print("--- GOAL REACHED: TERMINATING ---")
                break

def bootstrap_runtime():
    registry = CapabilityRegistry()
    # Mock registration
    registry.register("factory", {"skills": {"deploy": {"input_schema": {}}}})

    runtime = APOmegaRuntime(
        planner=DAGPlanner(),
        structural_validator=PlanStructuralValidator(),
        cycle_detector=DAGCycleDetector(),
        phase_validator=CanonPhaseValidator(),
        orchestrator=ParallelDAGExecutor(CapabilityGraph()),
        state_manager=StateManager(),
        telemetry=Telemetry(),
        event_bus=EventBus()
    )
    return runtime

if __name__ == "__main__":
    runtime = bootstrap_runtime()
    runtime.run("deploy_runtime_module")
