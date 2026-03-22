import sys
import os
import json
from pathlib import Path

# Thêm đường dẫn để import
sys.path.append(str(Path(__file__).resolve().parent))

try:
    from adapters.macos_ax import observer

    # Kích hoạt con mắt vật lý của axcontrol
    snap = observer.observe()

    if snap:
        # Giải phẫu dữ liệu thực tế nhìn thấy
        vision_data = {
            "app_name": snap.app,
            "element_role": snap.role,
            "element_label": snap.label,
            "bounding_box": snap.bbox
        }

        # Đưa vào cấu trúc nhận thức JSON
        print(json.dumps({
            "status": "AX_VISION_ACTIVE",
            "message": "Nervous system successfully tapped into macOS Accessibility API.",
            "reality_snapshot": vision_data
        }, indent=4, ensure_ascii=False))

    else:
        print(json.dumps({
            "status": "AX_BLIND",
            "message": "Không có snapshot trả về. Nguyên nhân cốt lõi: MacOS Sandbox EPERM chặn Accessibility."
        }, indent=4))

except Exception as e:
    print(json.dumps({
        "status": "SYS_ERROR",
        "error": str(e)
    }, indent=4))
