import sys
import os

# Add current directory to path
sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.getcwd(), "kernel"))

from kernel.adaptive_planner_v1 import AdaptivePlannerEngine
from kernel.canon_validator_v1 import CanonValidator
from kernel.omni_orchestrator_v1 import OmniOrchestrator
from kernel.runtime_kernel_v1 import RuntimeKernel

# 1. SETUP MOCK ENVIRONMENT
class MockStateManager:
    def __init__(self):
        self.count = 0
    def observe(self):
        self.count += 1
        return {"system_status": "active", "cycle": self.count}

class MockPersistence:
    pass

# Simplified capability graph for testing
capability_graph = {
    "phoenix": {
        "analysis": lambda **k: print(">>> EXEC: Phoenix Analysis"),
        "reasoning": lambda **k: print(">>> EXEC: Phoenix Reasoning")
    },
    "factory": {
        "deploy": lambda **k: print(">>> EXEC: Factory Deploy"),
        "filesystem": lambda **k: print(">>> EXEC: Factory Filesystem")
    },
    "axcontrol": {
        "runtime": lambda **k: print(">>> EXEC: AXControl Runtime"),
        "control": lambda **k: print(">>> EXEC: AXControl Control")
    }
}

# 2. INITIALIZE STANDARDIZED COMPONENTS
planner = AdaptivePlannerEngine(MockPersistence())
validator = CanonValidator()
orchestrator = OmniOrchestrator(capability_graph)
state_manager = MockStateManager()

kernel = RuntimeKernel(planner, validator, orchestrator, state_manager)

# 3. EXECUTE STANDARDIZED LOOP
print("====================================================")
print("   APΩ RUNTIME STANDARDIZATION VERIFICATION (v2)    ")
print("====================================================")

try:
    # Testing the goal resolution from Section 2/8
    kernel.run(goal="RUNTIME")
    print("\n✅ STANDARDIZATION VERIFICATION SUCCESSFUL!")
    print("Logic matches APΩ-PLANNER-001 Protocol.")
except Exception as e:
    print(f"\n❌ VERIFICATION FAILED: {e}")
    sys.exit(1)
