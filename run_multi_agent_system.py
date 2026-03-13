import sys
import os
import time
import json

BASE_DIR = "/Users/andy/my_too_test"
sys.path.append(BASE_DIR)

# Mock some components to ensure smooth execution without third-party dependencies breaking
from unittest.mock import MagicMock
for module in [
    "chromadb", "sentence_transformers", "langchain", "langchain.agents",
    "langchain_google_genai", "langchain.memory", "langchain.prompts",
    "langchain.chains", "ollama", "notion_client"
]:
    sys.modules[module] = MagicMock()

try:
    from hyperai_phoenix.app.brain.coordinator import MetaOptimizationCoordinator
except ImportError as e:
    print(f"ImportError: {e}")
    sys.exit(1)

def main():
    print("🚀 BẮT ĐẦU KÍCH HOẠT HỆ THỐNG MULTI-AGENT (PHOENIX COUNCIL)...")

    # Enable multi_agent in configs if not yet
    config_file = "/Users/andy/my_too_test/hyperai_phoenix/configs/council_weights.json"
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            cfg = json.load(f)
        if not cfg.get("multi_agent_enabled"):
            cfg["multi_agent_enabled"] = True
            with open(config_file, 'w') as f:
                json.dump(cfg, f, indent=2)

    coordinator = MetaOptimizationCoordinator(
        config_path="/Users/andy/my_too_test/hyperai_phoenix/configs",
        data_path="/tmp/daiof_data_test"
    )

    try:
        coordinator.start()
        print("✅ Multi-Agent Coordinator & Council Members Active.")

        time.sleep(1) # Let agents initialize

        print("\n📥 Submitting System Architecture Governance Directive to Council...")
        directive_content = "Xác nhận và kiểm toán hệ thống trúc Canonical (Planner -> Validator -> Orchestrator)"
        directive_id = coordinator.submit_directive(directive_content, source="alpha_prime_omega")

        print(f"⏳ Đang chờ Hội đồng Multi-Agent (Council) phân tích và đưa ra quyết định (Task {directive_id})...")

        # Give it a bit more time for the council to vote
        result = coordinator.get_result(directive_id, timeout=40.0)

        print("\n" + "="*80)
        if result:
            print(f"📊 KẾT QUẢ ĐỒNG THUẬN CỦA MULTI-AGENT COUNCIL:")
            print(f" - Trạng thái: {'Thành công' if result.success else 'Thất bại/Bị từ chối'}")
            print(f" - Điểm tin cậy (Alignment Score): {result.alignment_score}")
            print(f" - Thời gian thực thi: {result.execution_time:.2f}s")
            if result.error_message:
                print(f" - Lý do: {result.error_message}")
            if result.result_data:
                print(f" - Chi tiết phân tích: {json.dumps(result.result_data, indent=2, ensure_ascii=False)}")

            # Wait a few more seconds to see if queue finishes
            time.sleep(2)
        else:
            print("⚠️ Timeout: Hội đồng Multi-Agent đang suy nghĩ quá lâu hoặc xử lý ngầm chưa xong.")
        print("="*80)
        print("🏁 Hoàn thành phiên vận hành Multi-Agent.")

    finally:
        coordinator.stop()

if __name__ == "__main__":
    main()
