"""Finder policy and helpers."""

def allow_action(role: str, action: str, label: str | None = None) -> bool:
    # Finder safe mode: allow TAB navigation only
    return action == "TAB"
