# Σ_APΩ₂ CORE MODULE
# Authority: BỐ CƯỐNG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL - AXIS_5_EXECUTION

import json
import logging
import sys
import os

# Ensure autonomous_operator can be resolved
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

try:
    from autonomous_operator.nodes.agents.base_agent import DAIOFAgent
    from autonomous_operator.balance_integration import BalanceGovernor
except (ImportError, ValueError):
    from agents.base_agent import DAIOFAgent

class BalanceHubAgent(DAIOFAgent):
    """⚙️ Axis 5: Execution Control & Tool Orchestration."""
    def __init__(self):
        super().__init__(agent_name="BalanceHub", axis_id="AXIS_5_EXECUTION")
        self.genome.traits["execution_speed"] = 1.0
        try:
            self.governor = BalanceGovernor("http://localhost:8000")
        except NameError:
            self.governor = None # Fallback if import failed

    def execute_atomic_action(self, **kwargs):
        """⚙️ Atomic Function: Command Execution."""
        self.logger.info("⚙️ BalanceHub: Dispatching execution command...")

        connector = kwargs.get("connector")
        action = kwargs.get("action")
        payload = kwargs.get("payload", {})
        cmd = kwargs.get("cmd")

        if self.governor is None:
             return {"status": "error", "error": "BalanceGovernor import failed, simulated stub active."}

        # Backwards compatible for simulated inputs asking for 'status' or missing connector
        if not connector or not action:
            if cmd == "status" or not cmd:
                health = self.governor.get_system_health()
                return {"status": "success", "action": "fetch_health", "result": health}
            else:
                 return {"status": "error", "error": "connector & action required for BalanceHub execution."}

        result = self.governor.execute_governance_action(connector, action, payload)

        return {
            "status": "success",
            "axis": self.axis_id,
            "action": "tool_exec",
            "cmd": cmd,
            "result": result or "Governance action failed"
        }

def run(payload: str = None) -> str:
    """Standard Entry Point for Omni Orchestrator"""
    try:
        agent = BalanceHubAgent()
        return json.dumps(agent.run_cycle(payload))
    except Exception as e:
        return json.dumps({"status": "error", "error": str(e)})

if __name__ == "__main__":
    print(run())
