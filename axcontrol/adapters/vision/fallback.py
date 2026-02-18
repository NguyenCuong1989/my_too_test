"""Vision fallback stub.

Provides deterministic placeholder to keep interface stable without pixel access.
"""

from typing import Optional, Dict, Any


def vision_click_center(snapshot: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Stub: return a deterministic center point if bbox provided, else None.
    """
    bbox = snapshot.get("bbox")
    if not bbox:
        return None
    x, y, w, h = bbox
    return {"x": x + w // 2, "y": y + h // 2}
