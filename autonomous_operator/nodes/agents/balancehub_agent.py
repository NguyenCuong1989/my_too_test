# Σ_APΩ₂ CORE MODULE
# Authority: BỐ CƯỐNG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

import json
import logging
from autonomous_operator.nodes.agents.base_agent import DAIOFAgent
from autonomous_operator.balance_integration import BalanceGovernor

class BalanceHubAgent(DAIOFAgent):
    def __init__(self):
        super().__init__(agent_name="BalanceHub", axis_id="AXIS_5")
        self.governor = BalanceGovernor("http://localhost:8000")

    def execute_atomic_action(self, **kwargs):
        """🎯 Atomic Function for BalanceHub via API Contract"""
        self.logger.info("Executing atomic action for BalanceHub via BalanceGovernor...")
        connector = kwargs.get("connector")
        action = kwargs.get("action")
        payload = kwargs.get("payload", {})

        # If no explicit action mapped, try fetching system health instead
        if not connector or not action:
            health = self.governor.get_system_health()
            return {"status": "success", "agent": "BalanceHub", "health": health}

        result = self.governor.execute_governance_action(connector, action, payload)
        if result is None:
             return {"status": "error", "error": "BalanceHub unreachable or execution failed"}

        return {"status": "success", "agent": "BalanceHub", "result": result}

def run(payload: str = None) -> str:
    """Standard Entry Point for Omni Orchestrator"""
    try:
        agent = BalanceHubAgent()
        return json.dumps(agent.run_cycle(payload))
    except Exception as e:
        return json.dumps({"status": "error", "error": str(e)})

if __name__ == "__main__":
    print(run())
