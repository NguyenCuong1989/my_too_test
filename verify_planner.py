import sys
import os

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from kernel.adaptive_planner_v1 import AdaptivePlannerEngine

class MockCursor:
    def __init__(self, rows):
        self.rows = rows
    def execute(self, query):
        pass
    def fetchall(self):
        return self.rows

class MockPersistence:
    def __init__(self, rows):
        self.conn = self
        self.rows = rows
    def cursor(self):
        return MockCursor(self.rows)

def test_planner():
    # Define a simple capability graph
    # phoenix.analysis -> factory.deploy -> axcontrol.runtime
    graph_edges = [
        ("phoenix.analysis", "factory.deploy"),
        ("factory.deploy", "axcontrol.runtime")
    ]

    persistence = MockPersistence(graph_edges)
    planner = AdaptivePlannerEngine(persistence)

    # Goal: CONTROL
    goal = {"type": "CONTROL"}

    print(f"Testing planner for goal: {goal}")
    plan = planner.build_plan({}, goal, {}, ["factory", "axcontrol", "phoenix"])

    print("\nGenerated Plan:")
    print(f"Plan ID: {plan['plan_id']}")
    print("Tasks:")
    for task in plan['tasks']:
        print(f"  [{task['id']}] {task['phase']} -> {task['capability']}.{task['skill']}")

    print("\nEdges:")
    for edge in plan['edges']:
        print(f"  {edge['from']} -> {edge['to']}")

    # Verification
    expected_path = ["phoenix.analysis", "factory.deploy", "axcontrol.runtime"]
    actual_path = [f"{t['capability']}.{t['skill']}" for t in plan['tasks']]

    assert actual_path == expected_path, f"Path mismatch: {actual_path} != {expected_path}"
    print("\n✅ Planner verification successful!")

if __name__ == "__main__":
    try:
        test_planner()
    except Exception as e:
        print(f"\n❌ Planner verification failed: {e}")
        sys.exit(1)
