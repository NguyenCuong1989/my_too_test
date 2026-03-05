class GoalMapper:

    GOAL_MAP = {
        "STABILITY": ("phoenix", "analysis"),
        "DEPLOYMENT": ("factory", "deploy"),
        "CONTROL": ("axcontrol", "runtime")
    }

    def resolve(self, goal: dict):

        goal_type = goal["type"]

        if goal_type not in self.GOAL_MAP:
            raise Exception(f"Undefined goal type: {goal_type}")

        capability, skill = self.GOAL_MAP[goal_type]

        return f"{capability}.{skill}"
