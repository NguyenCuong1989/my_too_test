from .graph_search_v1 import GraphSearchPlanner
from .task_graph_builder_v1 import TaskGraphBuilder
from .goal_mapper_v1 import GoalMapper
from .capability_graph_loader_v1 import CapabilityGraphLoader


class AdaptivePlannerEngine:

    def __init__(self, persistence):

        self.persistence = persistence
        self.goal_mapper = GoalMapper()
        self.builder = TaskGraphBuilder()

        loader = CapabilityGraphLoader(persistence)
        graph = loader.load()

        self.search_engine = GraphSearchPlanner(graph)

    def build_plan(self, state, goal, context, capabilities):

        # Canonical start node
        start_node = "phoenix.analysis"

        # Resolve goal node via GoalMapper Γ
        goal_node = self.goal_mapper.resolve(goal)

        # Graph Search Π_adaptive
        path = self.search_engine.search(start_node, goal_node)

        # Task Graph Construction
        plan = self.builder.build(path)

        return plan
