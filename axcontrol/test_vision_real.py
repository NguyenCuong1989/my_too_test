import sys
import os
import json
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
os.environ["AXCONTROL_SIM"] = "0"

try:
    from adapters.macos_ax import observer

    # Ép buộc quan sát thực tế
    snap = observer.observe()

    if snap:
        vision_data = {
            "app_name": snap.app,
            "element_role": snap.role,
            "element_label": snap.label,
            "bounding_box": snap.bbox
        }
        print(json.dumps({
            "status": "AX_VISION_ACTIVE",
            "message": "Kết nối thành công tới luồng Accessibility gốc (AXTree).",
            "reality_snapshot": vision_data
        }, indent=4, ensure_ascii=False))

    else:
        print(json.dumps({
            "status": "AX_BLIND",
            "message": "Không có snapshot thực tế trả về. Mặc định MacOS đã chặn quyền Sandbox hoặc Accessibility đối với Terminal hiện tại.",
            "diagnostic": "Tiến trình Sandbox hiện tại không được cấp quyền trợ năng."
        }, indent=4))

except Exception as e:
    print(json.dumps({
        "status": "SYS_ERROR",
        "error": str(e)
    }, indent=4))
