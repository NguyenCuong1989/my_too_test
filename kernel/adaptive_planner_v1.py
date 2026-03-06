import json
from pathlib import Path
from graph_search_v1 import GraphSearchPlanner
from goal_mapper_v1 import GoalMapper
from task_graph_builder_v1 import TaskGraphBuilder

class AdaptivePlannerEngine:

    def __init__(self, persistence_layer):
        self.persistence = persistence_layer
        self.goal_mapper = GoalMapper()
        self.graph_search = None # Initialized during search
        self.task_builder = TaskGraphBuilder()

    def _load_formal_ontology(self):
        """
        Loads the formal ontology graph from omni_capability_ontology.json.
        """
        ontology_path = Path("/Users/andy/my_too_test/kernel/omni_capability_ontology.json")
        try:
            with open(ontology_path, "r") as f:
                data = json.load(f)
                return data.get("graph", {})
        except Exception as e:
            print(f"Warning: Failed to load formal ontology: {e}")
            return {}

    def build_plan(self, state: dict, goal: str, context: dict = None, allowed_capabilities: list = None):
        """
        Π_adaptive (Adaptive Planner)
        Translates a goal string into a DAG task graph using the 120-node Ontology.
        """
        print(f"Π_adaptive: Generating plan for goal: {goal}")

        # 1. Resolve Goal to Graph Nodes
        start_node = "command.telegram.receive" # New Canonical Start
        end_node = self.goal_mapper.resolve(goal)

        # 2. Load Formal Ontology (≈120 nodes)
        # Integration with omni_capability_ontology.json will follow
        graph = self._load_formal_ontology()

        self.graph_search = GraphSearchPlanner(graph)

        # 3. Compute Shortest Path
        path = self.graph_search.search(start_node, end_node)

        if not path:
            raise Exception(f"Π_adaptive: Planning failure. No path found from {start_node} to {end_node}")

        # 4. Build Task Graph (τ)
        # Standardized to return { "tasks": [...], "edges": [...] }
        plan = self.task_builder.build(path)

        return plan
