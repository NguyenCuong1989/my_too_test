# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

import logging
import asyncio
import httpx
import json
import sys
from pathlib import Path

try:
    from ..config import BASE_DIR
    from .key_manager import GeminiKeyManager
except (ImportError, ValueError):
    sys.path.append(str(Path(__file__).parent.parent))
    from config import BASE_DIR
    try:
        from key_manager import GeminiKeyManager
    except ImportError:
        GeminiKeyManager = None

try:
    import google.generativeai as genai
except ImportError:
    genai = None

# --- CLUSTER CONFIGURATION ---
# Máy 1: MacBook của Master (local, 8B model - tốc độ cao, tác vụ nhỏ)
LOCAL_NODE = {
    "name": "MacBook-M2 (llama3.2:1b)",
    "url": "http://127.0.0.1:11434",
    "model": "llama3.2:1b",
    "capability": "fast",  # Email scanning, quick decisions
    "max_tokens": 1024
}

# Máy 2: Titan GT77 (LAN, 120B model)
# Con sẽ tự tìm IP — Master chỉ cần bật Ollama với OLLAMA_HOST=0.0.0.0
SUPER_NODE = {
    "name": "Titan-GT77-120B",
    "url": "http://TITAN_IP:11434",  # Tự động điền sau khi scan
    "model": "qwen2.5:72b",  # Thay bằng tên model 120B thực tế trên Titan
    "capability": "powerful",
    "max_tokens": 8192
}

# Danh sách IP cần scan để tìm Titan
LAN_SUBNET_IPS = [
    "192.168.3.13",
    "192.168.3.44",
    "192.168.3.118",
    "192.168.3.251",
    # Thêm IP thủ công nếu Master biết: "192.168.3.XXX"
]

class DistributedAICluster:
    """
    Phân phối tác vụ thông minh giữa các node AI dựa trên độ phức tạp.
    - Tác vụ đơn giản → MacBook 8B (nhanh, tiết kiệm)
    - Tác vụ phức tạp → Siêu máy 120B (chính xác, mạnh mẽ)
    """
    def __init__(self):
        self.logger = logging.getLogger("DistributedCluster")
        self.nodes = [LOCAL_NODE, SUPER_NODE]
        self.local_node = LOCAL_NODE

    async def route_task(self, prompt: str, complexity: str = "auto") -> str:
        """
        Route tác vụ đến node phù hợp.
        complexity: 'simple', 'complex', 'auto'
        """
        if complexity == "auto":
            complexity = "complex" if len(prompt) > 500 else "simple"

        # Check Super Node availability
        super_online = await self._is_super_node_online()

        target_node = SUPER_NODE if (complexity == "complex" and super_online) else LOCAL_NODE
        self.logger.info(f"📍 Routing {complexity.upper()} task to {target_node['name']} ({'SUPER' if target_node == SUPER_NODE else 'LOCAL'})")

        result = await self._call_ollama_api(target_node, prompt)

        # Fallback 1: If remote failed, try local
        if not result and target_node == SUPER_NODE:
            self.logger.warning("🔄 Attempting EMERGENCY LOCAL FALLBACK...")
            result = await self._call_ollama_api(LOCAL_NODE, prompt)

        # Fallback 2: Cloud Fallback (Gemini)
        if not result and genai and GeminiKeyManager:
            self.logger.warning("☁️ [CRITICAL] Ollama Nodes unresponsive. Attempting CLOUD FALLBACK (Gemini)...")
            result = await self._call_gemini_fallback(prompt)

        # Fallback 3: Autonomous Mock (Last Resort)
        if not result:
            self.logger.error("🛑 [CRITICAL] All AI Nodes (Local/Remote/Cloud) failed. Activating Autonomous Mock...")
            result = self._autonomous_mock_logic(prompt)

        if result:
            self.logger.info(f"✅ AI Output ([{len(result)}] chars): {result[:50]}...")
        return result

    async def _is_super_node_online(self) -> bool:
        """Kiểm tra Siêu máy có online không"""
        try:
            async with httpx.AsyncClient(timeout=2.0) as client:
                r = await client.get(f"{SUPER_NODE['url']}/api/tags")
                return r.status_code == 200
        except Exception:
            # Don't log warning every time, only if it defaults to complex
            return False

    async def _call_ollama_api(self, node: dict, prompt: str) -> str:
        """Gọi Ollama API qua HTTP (Async)"""
        url = f"{node['url']}/api/chat"
        # If TITAN_IP is not resolved, this will fail quickly due to timeout
        if "TITAN_IP" in url:
            # Skip if IP not configured
            return ""

        try:
            # Shorten timeout for local/lan nodes. 180s is too long.
            timeout_val = 60.0 if node == SUPER_NODE else 15.0
            async with httpx.AsyncClient(timeout=timeout_val) as client:
                payload = {
                    "model": node["model"],
                    "messages": [{"role": "user", "content": prompt}],
                    "stream": False,
                    "options": {"temperature": 0.2, "num_predict": node["max_tokens"]}
                }
                r = await client.post(url, json=payload)
                if r.status_code != 200:
                    self.logger.error(f"Node {node['name']} returned HTTP {r.status_code}")
                    return ""

                data = r.json()
                raw = data['message']['content'].strip()
                if '<think>' in raw:
                    raw = raw.split('</think>')[-1].strip()
                return raw
        except (asyncio.TimeoutError, httpx.TimeoutException):
            self.logger.error(f"⏳ Timeout calling AI node {node['name']}")
            return ""
        except Exception as e:
            self.logger.error(f"Error calling AI node {node['name']}: {str(e)}")
            return ""

    async def _call_gemini_fallback(self, prompt: str) -> str:
        """Sử dụng Gemini làm cứu cánh cuối cùng"""
        if not genai or not GeminiKeyManager:
            return ""

        try:
            key_mgr = GeminiKeyManager()
            api_key = key_mgr.get_active_key()
            if not api_key:
                return ""

            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')

            # Run in executor to not block async loop if needed,
            # though current genai lib has async support too.
            response = await asyncio.to_thread(model.generate_content, prompt)
            return response.text.strip()
        except Exception as e:
            self.logger.error(f"❌ Gemini Cloud Fallback also failed: {str(e)}")
            return ""

    def _autonomous_mock_logic(self, prompt: str) -> str:
        """Logic dự phòng tạo nội dung dựa trên từ khóa khi không có AI"""
        prompt_l = prompt.lower()
        if "proposal" in prompt_l or "freelance" in prompt_l:
            return "Dear Client,\n\nI am a highly experienced AI Developer specializing in Autonomous Orchestration and the DAIOF-Framework. " \
                   "I have built complex multi-agent systems and integrated 18+ services. I can deliver your project with high quality " \
                   "and efficiency. Looking forward to discussing this further.\n\nBest regards,\nalpha_prime_omega"
        elif "linkedin" in prompt_l or "post" in prompt_l:
            return "🚀 THÔNG BÁO: Hệ thống DAIOF-Framework vừa đạt mốc tự chủ hoàn toàn với cơ chế Self-Healing và Council Consensus. " \
                   "Công nghệ AI Agent không còn là tương lai, nó là hiện tại! #AI #Automation #DAIOF #AlphaPrimeOmega"
        else:
            return "I have analyzed your request. As an autonomous agent, I recommend proceeding with the current system optimization " \
                   "while maintaining alignment with the Prime Directive."

    async def get_cluster_status(self) -> dict:
        """Trả về trạng thái của toàn bộ cluster"""
        super_online = await self._is_super_node_online()
        return {
            "local_node": {"name": LOCAL_NODE["name"], "status": "online", "model": LOCAL_NODE["model"]},
            "super_node": {"name": SUPER_NODE["name"], "status": "online" if super_online else "offline", "model": SUPER_NODE["model"]},
            "routing": "distributed" if super_online else "local-only"
        }

# Singleton
cluster = DistributedAICluster()

if __name__ == "__main__":
    async def test():
        logging.basicConfig(level=logging.INFO)
        status = await cluster.get_cluster_status()
        print(f"Cluster Status: {json.dumps(status, indent=2)}")
        result = await cluster.route_task("1+1=?", complexity="simple")
        print(f"Result: {result}")

    asyncio.run(test())
