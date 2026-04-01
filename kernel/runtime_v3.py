import json

class DAGExecutor:
    def __init__(self, capability_graph):
        self.capability_graph = capability_graph

    def execute(self, plan):
        tasks = {t["id"]: t for t in plan["tasks"]}
        edges = plan["edges"]
        dependency_map = {tid: [] for tid in tasks}
        for edge in edges:
            dependency_map[edge["to"]].append(edge["from"])
        executed = set()
        while len(executed) < len(tasks):
            for tid, deps in list(dependency_map.items()):
                if tid in executed: continue
                if all(d in executed for d in deps):
                    task = tasks[tid]
                    executor = self.capability_graph.get_executor(task["capability"])
                    executor.run(task["skill"], task["input"])
                    executed.add(tid)

class APOmegaRuntime:
    def __init__(self, planner, validator, phase_validator, orchestrator, state_manager):
        self.planner = planner
        self.validator = validator
        self.phase_validator = phase_validator
        self.orchestrator = orchestrator
        self.state_manager = state_manager

    def run(self, goal):
        print(f"--- INITIALIZING APΩ RUNTIME: GOAL={goal} ---")
        while True:
            state = self.state_manager.get_state()
            plan = self.planner.build_plan(state, goal, {}, ["factory","axcontrol","phoenix"])
            self.validator.validate(plan)
            self.phase_validator.validate_phases(plan["tasks"])
            self.orchestrator.execute(plan)
            observation = self.state_manager.observe()
            self.state_manager.update(observation)
            if self.state_manager.goal_reached(goal):
                print("--- GOAL REACHED: TERMINATING ---")
                break

if __name__ == "__main__":
    from capability_graph_v3 import CapabilityGraph
    from state_manager_v3 import StateManager
    from dag_planner_v3 import DAGPlanner
    from validators_v3 import CanonValidator, CanonPhaseValidator

    runtime = APOmegaRuntime(
        planner=DAGPlanner(),
        validator=CanonValidator(),
        phase_validator=CanonPhaseValidator(),
        orchestrator=DAGExecutor(CapabilityGraph()),
        state_manager=StateManager()
    )
    runtime.run("SYSTEM_SYNC_V3")
