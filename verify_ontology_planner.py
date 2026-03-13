import sys
from pathlib import Path
import json

# Setup Paths
BASE_DIR = Path("/Users/andy/my_too_test")
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "kernel"))

from kernel.adaptive_planner_v1 import AdaptivePlannerEngine

def test_ontology_plan():
    planner = AdaptivePlannerEngine(persistence_layer=None)

    goal = "DEEP_AUDIT"
    print(f"🚀 Testing Ontology Plan for Goal: {goal}")

    plan = planner.build_plan(state={}, goal=goal)

    print("\nGenerated Plan (Capability Path):")
    for i, step in enumerate(plan, 1):
        print(f"{i}. {step}")

    # Check if security scan is included in the plan
    security_included = any("security.protection.scan" in step for step in plan)
    print(f"\n🛡️ Security Layer (Σ) Included: {security_included}")

    if plan:
        print("\n✅ Ontology Pathfinding Successful.")
    else:
        print("\n❌ Ontology Pathfinding Failed.")

if __name__ == "__main__":
    test_ontology_plan()
策划
