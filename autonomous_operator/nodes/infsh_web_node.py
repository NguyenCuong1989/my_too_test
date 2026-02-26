import logging
import asyncio
import sys
import random
from datetime import datetime
from pathlib import Path

try:
    from ..config import INTEGRATED_SERVICES
    from ..neural_link import NeuralLink
    from .agent_browser_v2 import AgentBrowserV2
except (ImportError, ValueError):
    sys.path.append(str(Path(__file__).parent.parent))
    from config import INTEGRATED_SERVICES
    from neural_link import NeuralLink
    from nodes.agent_browser_v2 import AgentBrowserV2

class InfshWebNode:
    """
    Advanced WebNode using AgentBrowserV2 (inference.sh)
    to autonomously scout and 'link' ecosystem services.
    """
    def __init__(self):
        self.logger = logging.getLogger("InfshWebNode")
        self.link = NeuralLink()
        self.agent = AgentBrowserV2()

    async def run_cycle(self):
        self.logger.info("🌐 InfshWebNode: Linking and Scouting Ecosystem...")

        # In a real cycle, we might scout all or a subset
        services = list(INTEGRATED_SERVICES.items())
        # Link ALL services as requested by Master
        for name, url in services:
            await self.link_service(name, url)

    async def link_service(self, name: str, url: str):
        """Uses AI Browser to establish a 'link' by scouting the service."""
        self.logger.info(f"🔗 Linking Service: {name} ({url})")

        goal = f"Visit {name} at {url} and verify it is operational. Just check the homepage and report if it looks okay."

        try:
            result = await self.agent.run(goal=goal, start_url=url, max_steps=3)

            self.logger.info(f"✅ Service {name} linked. Result: {result[:100]}")
            self.link.send_pulse(
                node_name="InfshWebNode",
                pulse_type="SERVICE_LINKED",
                content=f"Service '{name}' has been successfully linked and verified via AI Browser. Status: {result[:100]}",
                intensity=1.0
            )
        except Exception as e:
            self.logger.error(f"❌ Failed to link {name}: {e}")
            self.link.send_pulse(
                node_name="InfshWebNode",
                pulse_type="LINK_FAILURE",
                content=f"Failed to establish link with '{name}': {e}",
                intensity=0.2
            )

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    node = InfshWebNode()
    asyncio.run(node.run_cycle())
