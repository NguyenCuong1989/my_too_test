import logging
import asyncio
import httpx
import json
import sys
from pathlib import Path

try:
    from ..config import BASE_DIR
except (ImportError, ValueError):
    sys.path.append(str(Path(__file__).parent.parent))
    from config import BASE_DIR

# --- CLUSTER CONFIGURATION ---
# Máy 1: MacBook của Master (local, 8B model - tốc độ cao, tác vụ nhỏ)
LOCAL_NODE = {
    "name": "MacBook-M2 (qwen3:8b)",
    "url": "http://127.0.0.1:11434",
    "model": "qwen3:8b",
    "capability": "fast",  # Email scanning, quick decisions
    "max_tokens": 2048
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
            # Tự động phán đoán dựa trên độ dài prompt
            complexity = "complex" if len(prompt) > 500 else "simple"

        if complexity == "complex" and await self._is_super_node_online():
            self.logger.info(f"🚀 Routing COMPLEX task to {SUPER_NODE['name']}")
            return await self._call_ollama(SUPER_NODE, prompt)
        else:
            self.logger.info(f"⚡ Routing SIMPLE task to {LOCAL_NODE['name']}")
            return await self._call_ollama_local(prompt)

    async def _is_super_node_online(self) -> bool:
        """Kiểm tra Siêu máy có online không"""
        try:
            async with httpx.AsyncClient(timeout=3.0) as client:
                r = await client.get(f"{SUPER_NODE['url']}/api/tags")
                return r.status_code == 200
        except:
            self.logger.warning(f"⚠️ {SUPER_NODE['name']} offline — fallback to local")
            return False

    async def _call_ollama(self, node: dict, prompt: str) -> str:
        """Gọi một Ollama node qua HTTP API"""
        try:
            async with httpx.AsyncClient(timeout=120.0) as client:
                payload = {
                    "model": node["model"],
                    "messages": [{"role": "user", "content": prompt}],
                    "stream": False,
                    "options": {"temperature": 0.2, "num_predict": node["max_tokens"]}
                }
                r = await client.post(f"{node['url']}/api/chat", json=payload)
                data = r.json()
                raw = data['message']['content'].strip()
                if '<think>' in raw:
                    raw = raw.split('</think>')[-1].strip()
                return raw
        except Exception as e:
            self.logger.error(f"Cluster call error: {e}")
            return ""

    async def _call_ollama_local(self, prompt: str) -> str:
        """Gọi local node (sync-safe wrapper)"""
        import ollama
        try:
            response = ollama.chat(
                model=LOCAL_NODE["model"],
                messages=[{"role": "user", "content": prompt}],
                options={"temperature": 0.2}
            )
            raw = response['message']['content'].strip()
            if '<think>' in raw:
                raw = raw.split('</think>')[-1].strip()
            return raw
        except Exception as e:
            self.logger.error(f"Local AI error: {e}")
            return ""

    async def get_cluster_status(self) -> dict:
        """Trả về trạng thái của toàn bộ cluster"""
        super_online = await self._is_super_node_online()
        return {
            "local_node": {"name": LOCAL_NODE["name"], "status": "online", "model": LOCAL_NODE["model"]},
            "super_node": {"name": SUPER_NODE["name"], "status": "online" if super_online else "offline", "model": SUPER_NODE["model"]},
            "routing": "distributed" if super_online else "local-only"
        }

# Singleton để các Node dùng chung
cluster = DistributedAICluster()

if __name__ == "__main__":
    async def test():
        status = await cluster.get_cluster_status()
        print(f"Cluster Status: {json.dumps(status, indent=2)}")
        result = await cluster.route_task("Phân tích xu hướng AI năm 2026", complexity="simple")
        print(f"Result: {result[:200]}")

    asyncio.run(test())
