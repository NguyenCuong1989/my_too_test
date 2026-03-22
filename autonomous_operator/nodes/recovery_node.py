# Σ_APΩ₂ CORE MODULE
# Authority: BỐ CƯỐNG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

import sys
import logging
import os
import json
from pathlib import Path
import datetime

try:
    from autonomous_operator.nodes.agents.base_agent import DAIOFAgent
except (ImportError, ValueError):
    from agents.base_agent import DAIOFAgent

class RecoveryNode(DAIOFAgent):
    """Node: Hồi phục (Health & Recovery)
    Giám sát sức khỏe các dịch vụ lõi (Ollama, SQLite, ...).
    """
    def __init__(self):
        super().__init__("RecoveryService", axis_id="AXIS_0")

    def execute_atomic_action(self, **kwargs):
        """Thực thi kiểm tra sức khỏe thực tế."""
        ollama_status = self.check_ollama_health()

        result = {
            "status": "stable" if ollama_status["online"] else "unstable",
            "ollama": ollama_status,
            "timestamp": datetime.datetime.now().isoformat()
        }

        return result

    def check_ollama_health(self):
        """Monitor Ollama health and reachability"""
        try:
            import requests
            response = requests.get("http://localhost:11434/api/tags", timeout=5)
            if response.status_code == 200:
                return {"online": True, "status_code": 200, "message": "Ollama local service is ONLINE"}
            else:
                return {"online": False, "status_code": response.status_code, "message": "Ollama returned warning status"}
        except Exception as e:
            return {"online": False, "error": str(e), "message": "Ollama local service is DOWN or unreachable"}

    def run_cycle(self, command_args=None):
        return super().run_cycle(command_args)

def run(payload: str = None) -> str:
    """Standard Entry Point for Omni Orchestrator"""
    try:
        node = RecoveryNode()
        result = node.run_cycle(payload)
        return json.dumps({"status": "success", "result": result})
    except Exception as e:
        return json.dumps({"status": "error", "error": str(e)})

if __name__ == "__main__":
    print(run())
