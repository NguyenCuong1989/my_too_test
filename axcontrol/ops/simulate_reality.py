import time
import json
from dataclasses import dataclass
from core.The.state_projector import map_state_to_hexagram
from core.canon.existence_state_map import EXISTENCE_STATE_MAP
from core.Menh.Chung import compute_Chung

@dataclass
class MockSnap:
    app: str
    role: str
    label: str
    is_focused: bool = True
    is_enabled: bool = True
    is_stable: bool = True

def simulate_step(step_name, snap):
    print(f"\n=== [BƯỚC: {step_name}] ===")

    # 1. THẾ (Observe & Project)
    hex_bits = map_state_to_hexagram(snap)
    existence = EXISTENCE_STATE_MAP.get(hex_bits, "DIET")
    print(f"[THẾ] App: {snap.app} | Role: {snap.role} | Label: '{snap.label}'")
    print(f"[QUẺ] Hexagram: {hex_bits} -> Trạng thái: {existence}")

    # 2. CHÍNH (Intent - Mocked)
    intent = {
        "intent_id": f"intent_{int(time.time()*1000)}",
        "goal": f"Navigate in {snap.app}",
        "parameters": {"action": "TAB"}
    }
    print(f"[CHÍNH] Ý định: {intent['goal']}")

    # 3. ẤN (Command)
    envelope = {
        "command_id": f"cmd_{int(time.time()*1000)}",
        "type": "NAVIGATE",
        "params": {"key": "TAB"}
    }
    print(f"[ẤN] Lệnh: {envelope['type']}({envelope['params']['key']})")

    # 4. CHỨNG (Audit & Hash)
    state_proof = f"{snap.app}:{snap.role}:{snap.label}"
    effect = {"emitted": "TAB"}
    chung_hash = compute_Chung(state_proof, intent, envelope, effect)

    record = {
        "timestamp": time.time(),
        "state": state_proof,
        "hex": hex_bits,
        "intent": intent["intent_id"],
        "Chung": chung_hash
    }
    print(f"[CHỨNG] Karma Record: {json.dumps(record, indent=2)}")
    print(f"[CÚC] Niêm phong thành công: {chung_hash[:12]}...")

# --- KỊCH BẢN THỰC TẾ ---
# Master muốn tìm kiếm một ghi chú quan trọng.

# Giai đoạn 1: Đang ở Notes, nhưng tiêu điểm chưa đúng
snap1 = MockSnap("Notes", "AXWindow", "Notes")
simulate_step("KHỞI TẠO", snap1)

time.sleep(1)

# Giai đoạn 2: Nhấn TAB để chuyển vào vùng soạn thảo/tìm kiếm
snap2 = MockSnap("Notes", "AXTextArea", "Editor")
simulate_step("LUÂN CHUYỂN", snap2)

print("\n[LẬP] Thực tại khớp với Pháp pháp. Tiếp tục vận hành... thưa Master.")
