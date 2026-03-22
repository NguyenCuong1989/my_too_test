import json
from pathlib import Path
from typing import Any, Dict


DEFAULT_QUOTA_STATE_PATH = Path("/Users/andy/.gemini/quota_state.json")


class QuotaGuard:
    """Minimal quota-aware read/deny helper for local-first routing."""

    def __init__(self, state_path: Path | str = DEFAULT_QUOTA_STATE_PATH):
        self.state_path = Path(state_path)

    def read_state(self) -> Dict[str, Any]:
        if not self.state_path.exists():
            return {
                "gemini": "unknown",
                "overage_strategy": "unknown",
                "local_fallback": "enabled",
                "routing_mode": "LOCAL_SURVIVAL",
                "reason": "quota_state_missing",
            }

        try:
            return json.loads(self.state_path.read_text())
        except Exception:
            return {
                "gemini": "unknown",
                "overage_strategy": "unknown",
                "local_fallback": "enabled",
                "routing_mode": "LOCAL_SURVIVAL",
                "reason": "quota_state_unreadable",
            }

    def allow_cloud(self, task_class: str) -> tuple[bool, str, Dict[str, Any]]:
        state = self.read_state()
        quota = state.get("gemini", "unknown")
        overage = state.get("overage_strategy", "unknown")

        if task_class == "local-safe":
            return False, "local-safe tasks must not spend cloud quota", state

        if quota in {"exhausted", "warning"} and task_class in {"cloud-optional", "cloud-preferred"}:
            return False, f"quota_state={quota}; route to local", state

        if quota == "exhausted" and task_class == "cloud-required":
            return False, "cloud-required task denied because quota is exhausted", state

        if overage == "never" and quota in {"exhausted", "warning"}:
            return False, f"overage_strategy={overage}; fail-close for cloud path", state

        if quota == "healthy":
            return True, "cloud path allowed", state

        return False, "quota state unresolved; fail-close", state
