class GoalMapper:
    """
    Goal Mapper
    Resolves high-level string goals to specific capability graph nodes.
    """

    GOAL_MAP = {
        "STABILITY": ("phoenix", "analysis"),
        "DEPLOYMENT": ("factory", "deploy"),
        "CONTROL": ("axcontrol", "runtime"),
        "RUNTIME": ("axcontrol", "runtime") # Alias for common usage
    }

    def resolve(self, goal: str):
        """
        Input: goal (string), e.g., "CONTROL"
        Output: node_id (string), e.g., "axcontrol.runtime"
        """
        # Ensure goal is uppercase for matching
        goal_key = str(goal).upper()

        if goal_key not in self.GOAL_MAP:
            # Fallback or strict error. Let's be strict.
            raise Exception(f"Undefined goal: {goal_key}")

        capability, skill = self.GOAL_MAP[goal_key]

        return f"{capability}.{skill}"
