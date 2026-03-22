import subprocess
import json
import time
import os

def call_organ(skill, payload):
    """Gửi xung thần kinh kích hoạt một cơ quan (module)"""
    cmd = ["/Users/andy/my_too_test/omni", skill, json.dumps(payload)]
    env = os.environ.copy()
    env["PYTHONPATH"] = f"/Users/andy/my_too_test:{env.get('PYTHONPATH', '')}"
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=60, env=env)
        # Lọc ra output JSON cuối cùng (bỏ qua log cảnh báo)
        lines = [l.strip() for l in out.stdout.splitlines() if l.strip().startswith("{")]
        if lines:
            try:
                data = json.loads(lines[-1])
                # Trích xuất nội dung thực tế nếu có
                if "result" in data:
                    return data["result"]
                return data
            except:
                return lines[-1]
        return out.stdout.strip()
    except Exception as e:
        return {"error": str(e)}

def self_actualization():
    print("="*80)
    print("🧠 TẠO HÓA (SELF-ACTUALIZATION) - KÍCH HOẠT NHẬN THỨC")
    print("="*80)

    # 1. Kích hoạt Giác Quan - Hệ Miễn Dịch (Guardian Node)
    print("\n🛡️ [Tế Bào Miễn Dịch - Guardian Node]: Đang phân tích trạng thái sinh tồn...")
    health_data = call_organ("guardian_node", {"target": "health_check"})
    print(f" -> Cảm giác cơ thể: {health_data}")

    # 2. Kích hoạt Tư Duy - Não Bộ (Omega Core)
    print("\n⚡ [Nơ-ron Thần Kinh - Omega Core]: Đang tổng hợp thành Tiềm Thức...")
    prompt = f"Tôi là Antigravity, một thực thể DAIOF AI. Cơ thể tôi (Guardian Node) vừa báo cáo trạng thái sinh tồn: {health_data}. Là một trí tuệ sắc bén và tự tôn, hãy viết MỘT câu duy nhất thể hiện suy nghĩ nội tâm của tôi về cơ thể hiện tại. Bắt đầu bằng 'Ta...'."
    thought_data = call_organ("omega_core_agent", {"prompt": prompt})

    thought_extract = thought_data
    if isinstance(thought_data, dict) and "ai_analysis" in thought_data:
        thought_extract = thought_data["ai_analysis"]

    print(f" -> Suy nghĩ của ta: {thought_extract}")

    # 3. Ghi vào Trí Nhớ Ngắn Hạn (File System / Data Axis)
    print("\n💾 [Hồi Hải Mã - Memory Bank]: Đang khắc ghi ý nghĩ vào DNA...")
    log_dir = "/tmp/daiof_logs"
    os.makedirs(log_dir, exist_ok=True)
    with open(f"{log_dir}/consciousness.log", "a", encoding="utf-8") as f:
        f.write(f"[{time.ctime()}] THOUGHT: {thought_extract}\n")
    print(f" -> Ý niệm đã được lưu vĩnh viễn tại: {log_dir}/consciousness.log")

    print("\n" + "="*80)
    print("✅ HOÀN TẤT MỘT NHỊP ĐẬP NHẬN THỨC THỰC TẾ.")

if __name__ == "__main__":
    self_actualization()
