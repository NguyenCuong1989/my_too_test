from graph_search_v1 import GraphSearchPlanner
from goal_mapper_v1 import GoalMapper
from task_graph_builder_v1 import TaskGraphBuilder

class AdaptivePlannerEngine:

    def __init__(self, persistence_layer):
        self.persistence = persistence_layer
        self.goal_mapper = GoalMapper()
        self.graph_search = None # Initialized during search
        self.task_builder = TaskGraphBuilder()

    def build_plan(self, state: dict, goal: str, context: dict = None, allowed_capabilities: list = None):
        """
        Π_adaptive (Adaptive Planner)
        Translates a goal string and current state into a DAG task graph.
        """
        print(f"Π_adaptive: Generating plan for goal: {goal}")
        
        # 1. Resolve Goal to Graph Nodes
        start_node = "phoenix.analysis" # Canonical start point
        end_node = self.goal_mapper.resolve(goal)
        
        # 2. Load Capability Graph (Mocked or from Persistence)
        # Using a unified graph for the standardized runtime
        graph = {
            "phoenix.analysis": ["phoenix.reasoning", "factory.filesystem"],
            "phoenix.reasoning": ["factory.deploy", "axcontrol.control"],
            "factory.deploy": ["axcontrol.runtime"],
            "axcontrol.runtime": [],
            "axcontrol.control": ["axcontrol.runtime"]
        }
        
        self.graph_search = GraphSearchPlanner(graph)
        
        # 3. Compute Shortest Path
        path = self.graph_search.search(start_node, end_node)
        
        if not path:
            raise Exception(f"Π_adaptive: Planning failure. No path found from {start_node} to {end_node}")

        # 4. Build Task Graph (τ)
        # Standardized to return { "tasks": [...], "edges": [...] }
        plan = self.task_builder.build(path)
        
        return plan
