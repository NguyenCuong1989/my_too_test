"""System Settings policy (safe navigation)."""


def allow_action(role: str, action: str, label: str | None = None) -> bool:
    if action != "TAB":
        return False
    # Allow TAB navigation across rows/buttons; block toggles/enter implied
    return role in {"AXRow", "AXButton", "AXTextField", "AXGroup"}
