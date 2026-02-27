import logging
import requests
import json
from pathlib import Path

class BalanceGovernor:
    """Bridges the Orchestrator with BalanceHub for economic and runtime governance."""
    def __init__(self, hub_url="http://localhost:8000"):
        self.logger = logging.getLogger("BalanceGovernor")
        self.hub_url = hub_url

    def get_system_health(self):
        """Lấy chỉ số GSSI (Global System Stability Index)"""
        try:
            resp = requests.get(f"{self.hub_url}/system/health", timeout=5)
            if resp.status_code == 200:
                data = resp.json()
                self.logger.info(f"📊 BalanceHub GSSI: {data.get('gssi', 'N/A')}")
                return data
        except Exception as e:
            self.logger.error(f"❌ Failed to reach BalanceHub: {e}")
        return None

    def get_economic_weight(self):
        """Lấy chỉ số COMPUTE_W (Economic Weight)"""
        try:
            resp = requests.get(f"{self.hub_url}/system/economic-weight", timeout=5)
            if resp.status_code == 200:
                return resp.json()
        except Exception:
            pass
        return None

    def execute_governance_action(self, connector, action, payload=None):
        """Gửi lệnh thực thi qua governance gateway của BalanceHub"""
        try:
            url = f"{self.hub_url}/execute"
            data = {
                "connector": connector,
                "action": action,
                "payload": payload or {},
                "request_id": f"gov-{int(Path('/dev/urandom').stat().st_atime)}" # Simple unique ID
            }
            resp = requests.post(url, json=data, timeout=10)
            return resp.json()
        except Exception as e:
            self.logger.error(f"❌ Governance execution failed: {e}")
        return None
