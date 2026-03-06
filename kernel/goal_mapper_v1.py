class GoalMapper:
    """
    Goal Mapper
    Resolves high-level string goals to specific capability graph nodes.
    """

    def __init__(self):
        self.ontology_path = Path("/Users/andy/my_too_test/kernel/omni_capability_ontology.json")
        self.mapping_path = Path("/Users/andy/my_too_test/kernel/node_to_agent_map.json")

    def resolve(self, goal: str) -> str:
        """
        Maps a high-level mission goal to a terminal ontology node.
        """
        # Mission -> Terminal Node mapping
        mission_map = {
            "DEEP_AUDIT": "axis_7.economics.value_scoring",
            "SYNC_LOGIC": "axis_5.execution.filesystem",
            "SECURITY_SCAN": "axis_6.security.protection",
            "WEB_AUTO": "axis_3.ui_vision.element_recognition"
        }

        node_id = mission_map.get(goal.upper(), goal)
        return node_id

    def get_agent_for_node(self, node_id: str) -> str:
        """
        Bridges Ontology Node -> Omni Agent
        """
        try:
            import json
            from pathlib import Path
            with open(self.mapping_path, "r") as f:
                data = json.load(f)
                return data.get("mappings", {}).get(node_id, "omega_core_agent")
        except:
            return "omega_core_agent"
