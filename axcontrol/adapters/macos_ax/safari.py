"""Safari AX context (stub).

Determines Safari zones to enforce tab-only safe navigation.
"""

from typing import Literal, Optional, Dict

Zone = Literal["ADDRESS_BAR", "WEB_CONTENT", "TOOLBAR_BUTTON", "UNKNOWN"]


def safari_context(role: str, label: str) -> Dict[str, Optional[str]]:
    role = role or ""
    label = label or ""
    zone: Zone = "UNKNOWN"
    if role == "AXTextField":
        zone = "ADDRESS_BAR"
    elif role == "AXWebArea":
        zone = "WEB_CONTENT"
    elif role in {"AXButton", "AXToolbar"}:
        zone = "TOOLBAR_BUTTON"
    return {"zone": zone}
