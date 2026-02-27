import logging
import asyncio
import sys
import random
import json
from datetime import datetime
from pathlib import Path
from playwright.async_api import async_playwright

try:
    from ..config import INTEGRATED_SERVICES
    from ..neural_link import NeuralLink
except (ImportError, ValueError):
    sys.path.append(str(Path(__file__).parent.parent))
    from config import INTEGRATED_SERVICES
    from neural_link import NeuralLink

class WebNode:
    """Node OMNI: Có khả năng điều khiển Browser & Giám sát Hệ sinh thái toàn cầu"""
    def __init__(self):
        self.logger = logging.getLogger("WebNode")
        self.link = NeuralLink()

    async def run_cycle(self):
        self.logger.info("🌐 WebNode: Scanning Ecosystem Organs...")

        # Chọn ngẫu nhiên 3 dịch vụ từ danh sách của Master để kiểm tra trong chu kỳ này
        services = list(INTEGRATED_SERVICES.items())
        targets = random.sample(services, min(len(services), 3))

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()

            for name, url in targets:
                await self.scout_service(context, name, url)

            await browser.close()

    async def scout_service(self, context, name, url):
        """Kiểm tra một dịch vụ và gửi xung thần kinh về trung tâm"""
        self.logger.info(f"🔎 Scouting: {name} ({url})")
        page = await context.new_page()
        try:
            start_time = datetime.now()
            response = await page.goto(url, timeout=20000, wait_until="domcontentloaded")
            latency = (datetime.now() - start_time).total_seconds()

            status = response.status if response else "Unknown"

            if status == 200:
                self.logger.info(f"✅ {name} is OK. Latency: {latency:.2f}s")
                self.link.send_pulse(
                    node_name="WebNode",
                    pulse_type="ECOSYSTEM_HEALTH",
                    content=f"Service '{name}' is responsive (200 OK)",
                    intensity=1.0
                )
                self.link.log_service_event(
                    service="WebScoutService",
                    e_type="STATUS",
                    content=f"Service {name} verified healthy. Latency: {latency:.2f}s",
                    meta=json.dumps({"url": url, "latency": latency})
                )
            else:
                self.logger.warning(f"⚠️ {name} returned status: {status}")
                self.link.send_pulse(
                    node_name="WebNode",
                    pulse_type="ECOSYSTEM_WARNING",
                    content=f"Service '{name}' returned status {status}",
                    intensity=0.5
                )
                self.link.log_service_event(
                    service="WebScoutService",
                    e_type="SLA_BREACH",
                    content=f"Service {name} returned non-200 status: {status}",
                    meta=json.dumps({"url": url, "status": status})
                )

            await page.close()
        except Exception as e:
            self.logger.error(f"❌ Failed to scout {name}: {e}")
            self.link.send_pulse(
                node_name="WebNode",
                pulse_type="ECOSYSTEM_FAILURE",
                content=f"Service '{name}' is unreachable: {e}",
                intensity=0.1
            )

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    node = WebNode()
    asyncio.run(node.run_cycle())
