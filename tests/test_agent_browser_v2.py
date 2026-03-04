import asyncio
import logging
import json
import os
import sys
from pathlib import Path

# Add project root to sys.path
BASE_DIR = Path(__file__).parent.parent
sys.path.append(str(BASE_DIR))

from autonomous_operator.nodes.agent_browser_v2 import AgentBrowserV2

async def test_agent_thinking():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger("TestAgentBrowserV2")

    logger.info("Starting AgentBrowserV2 Thinking Test")
    agent = AgentBrowserV2(session_id="test_session")

    # Mock snapshot to test thinking without needing a live browser session immediately
    # This checks if Ollama integration and prompt formatting work
    mock_snapshot = {
        "url": "https://example.com",
        "elements": [
            "@e1 [a] \"More information...\" href=\"https://www.iana.org/domains/example\"",
            "@e2 [h1] \"Example Domain\""
        ]
    }

    goal = "Click on the more information link"

    logger.info(f"Goal: {goal}")
    try:
        decision = await agent._think(goal, mock_snapshot)
        logger.info(f"AI Decision: {json.dumps(decision, indent=2)}")

        # Validation
        if decision.get("action") == "click" and decision.get("ref") == "@e1":
            logger.info("✅ Thinking test PASSED: Agent correctly identified the click action for @e1.")
        else:
            logger.warning(f"⚠️ Thinking test UNEXPECTED RESULT: {decision}")

    except Exception as e:
        logger.error(f"❌ Thinking test FAILED with error: {e}")

async def test_agent_run_integration():
    # Only run this if you want to try a live run (requires infsh and browser setup)
    # For now, let's keep it commented if we don't want to burn time/resources
    # but we can provide the skeleton
    pass

if __name__ == "__main__":
    asyncio.run(test_agent_thinking())
