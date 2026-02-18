"""Notes policy with text guard."""

from core.Menh.stop_reasons import StopReason


def allow_action(role: str, action: str, label: str | None = None):
    """
    Returns tuple (allowed: bool, stop_reason: str|None)
    """
    if role == "AXTextArea":
        return False, StopReason.TEXT_EDIT_BLOCKED.value
    if action != "TAB":
        return False, None
    # TAB allowed across sidebar/list/toolbar elements
    if role in {"AXRow", "AXList", "AXListItem", "AXButton"}:
        return True, None
    return False, None
