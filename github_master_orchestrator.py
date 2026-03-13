import time
from kernel.adaptive_planner_v1 import AdaptivePlannerEngine
from kernel.omni_orchestrator_v1 import OmniOrchestrator
from kernel.canon_validator_v1 import CanonValidator
from kernel.goal_mapper_v1 import GoalMapper

class GitHubMasterOrchestrator:
    """
    The High-Level Agent responsible for managing the Unified GitHub System.
    Coordinates 20 BalanceHub workers via the Adaptive Planner.
    """

    def __init__(self):
        # Mock capability graph - in a real scenario, this would be more complex
        # Note: Local capabilities take precedence. Remote capabilities are handled by the bridge in OmniOrchestrator.
        self.capability_graph = {
            "github": {
                "list_repos": None,
                "sync_logic": None,
                "audit_repo": None
            },
            "asana": {
                "create_task": None,
                "get_status": None,
                "update_audit_task": None
            },
            "memory": {
                "status": None,
                "sync": None
            },
            "system": {
                "health": None
            }
        }

        self.planner = AdaptivePlannerEngine(self.capability_graph)
        self.validator = CanonValidator()
        self.orchestrator = OmniOrchestrator(self.capability_graph)

    def run_mission(self, goal_str: str):
        print(f"🚀 Master: Starting Mission for Goal: {goal_str}")

        # 1. Plan
        state = {"cycle": 1, "status": "active"}
        plan = self.planner.build_plan(state, goal_str)

        # 2. Validate
        try:
            self.validator.validate(plan)
        except Exception as e:
            print(f"❌ Master: Plan Validation Failed: {e}")
            return

        # 3. Execute (Coordinates the 20 services)
        self.orchestrator.execute(plan)

        print(f"✅ Master: Mission Complete for Goal: {goal_str}")

if __name__ == "__main__":
    import sys
    goal = sys.argv[1] if len(sys.argv) > 1 else "DEEP_AUDIT"

    master = GitHubMasterOrchestrator()
    master.run_mission(goal)
