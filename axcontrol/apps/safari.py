"""Safari policy."""

from adapters.macos_ax.safari import safari_context


def allow_action(role: str, label: str, action: str) -> bool:
    ctx = safari_context(role, label)
    zone = ctx.get("zone")
    if zone in {"ADDRESS_BAR", "WEB_CONTENT"}:
        return False
    return action == "TAB"
