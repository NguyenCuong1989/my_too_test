import asyncio
import logging
import json
import sys
import re
from datetime import datetime
from pathlib import Path

try:
    import ollama
except ImportError:
    pass # Assume ollama is installed or handled elsewhere if needed

from .infsh_browser_client import InfshBrowserClient

try:
    from ..neural_link import NeuralLink
except (ImportError, ValueError):
    sys.path.append(str(Path(__file__).parent.parent))
    from neural_link import NeuralLink

LOCAL_MODEL = "qwen3:8b"
logger = logging.getLogger("AgentBrowserV2")

class AgentBrowserV2:
    """
    Advanced Browser Agent using inference.sh (v2).
    Uses InfshBrowserClient for precise element interaction via @e refs.
    """

    def __init__(self, session_id: str = "new"):
        self.client = InfshBrowserClient(session_id=session_id)
        self.link = NeuralLink()
        self.model = LOCAL_MODEL
        self.history = []

    async def _think(self, goal: str, page_snapshot: Dict[str, Any]) -> dict:
        """Ask Ollama for the next step based on snapshot data."""

        url = page_snapshot.get("url", "unknown")
        # Extract elements from snapshot. Agent-browser returns them in 'elements' or similar
        # Based on docs: '@e1 [a] "Home" href="/"'
        elements = page_snapshot.get("elements", [])
        if not elements:
            # If snapshot doesn't return list, try parsing raw text if available
            raw_elements = page_snapshot.get("raw_text", "")
        else:
            raw_elements = "\n".join(elements[:50]) # Use first 50 elements

        prompt = f"""You are an advanced Browser Agent (v2) using the inference.sh framework.
Goal: {goal}
Current URL: {url}

Available Elements (with @e refs):
{raw_elements}

History:
{json.dumps(self.history[-5:], ensure_ascii=False)}

Rules:
1. Use '@e<number>' refs for actions on elements.
2. Form actions: Use 'fill' with 'ref' and 'text'.
3. Navigation: If no ref is suitable, use 'goto' with 'url'.
4. Finish: Use 'done' when the goal is achieved.

Return ONLY a JSON object:
{{
  "action": "click|fill|type|press|hover|scroll|goto|done",
  "ref": "@e1",  // Required for element actions
  "text": "...", // Required for fill/type/press
  "url": "...",  // Required for goto
  "reason": "...",
  "done": false
}}
"""
        try:
            # Using ollama directly as in v1
            import ollama
            resp = ollama.chat(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                options={"temperature": 0.1}
            )
            raw = resp["message"]["content"].strip()
            if "<think>" in raw:
                raw = raw.split("</think>")[-1].strip()
            # Clean JSON blocks
            raw = re.sub(r'```json\s*|\s*```', '', raw).strip()
            return json.loads(raw)
        except Exception as e:
            logger.error(f"Ollama think error: {e}")
            return {"action": "done", "reason": f"AI thinking failed: {e}", "done": True}

    async def run(self, goal: str, start_url: str = None, max_steps: int = 15) -> str:
        logger.info(f"🚀 AgentBrowserV2 START: {goal}")
        self.link.send_pulse("AgentBrowserV2", "TASK_START", goal, 1.0)

        try:
            if start_url:
                logger.info(f"Opening: {start_url}")
                snapshot = await self.client.open(start_url)
            else:
                snapshot = await self.client.snapshot()

            for step in range(max_steps):
                logger.info(f"🔄 Step {step + 1}/{max_steps} | URL: {snapshot.get('url')}")

                decision = await self._think(goal, snapshot)
                logger.info(f"🧠 AI Decision: {decision.get('action')} -> {decision.get('ref') or decision.get('url', '')}")

                self.history.append({
                    "step": step + 1,
                    "url": snapshot.get("url"),
                    "decision": decision
                })

                if decision.get("done") or decision.get("action") == "done":
                    result = decision.get("reason", "Task completed")
                    break

                # Map decision to interact action
                action = decision.get("action")
                kwargs = {}
                if "ref" in decision: kwargs["ref"] = decision["ref"]
                if "text" in decision: kwargs["text"] = decision["text"]
                if "url" in decision: kwargs["url"] = decision["url"]

                # Execute interaction
                if action == "goto":
                    snapshot = await self.client.open(kwargs["url"])
                else:
                    await self.client.interact(action, **kwargs)
                    # Always re-snapshot after interaction
                    snapshot = await self.client.snapshot()

            await self.client.close()
            self.link.send_pulse("AgentBrowserV2", "TASK_DONE", result[:200], 0.9)
            return result

        except Exception as e:
            error_msg = f"Fatal error in AgentBrowserV2: {e}"
            logger.error(error_msg)
            self.link.send_pulse("AgentBrowserV2", "TASK_ERROR", error_msg, 0.1)
            # Try to close session
            try: await self.client.close()
            except: pass
            return error_msg

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--goal", type=str, required=True)
    parser.add_argument("--url", type=str, default=None)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    agent = AgentBrowserV2()
    asyncio.run(agent.run(args.goal, args.url))
