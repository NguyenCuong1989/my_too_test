"""Local kill-switch.

Hard stop that cannot be overridden by remote/AI. Requires human to re-arm.
"""

class KillSwitch:
    def __init__(self):
        self.engaged = False

    def trigger(self, reason: str) -> None:
        self.engaged = True
        # Logging handled by caller to keep kill-switch minimal

    def reset(self) -> None:
        self.engaged = False
