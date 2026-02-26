import json
import subprocess
import logging
import asyncio
from typing import Dict, Any, List, Optional

logger = logging.getLogger("InfshBrowserClient")

class InfshBrowserClient:
    """
    Python wrapper for the inference.sh CLI to interact with agent-browser.
    """

    def __init__(self, session_id: str = "new"):
        self.session_id = session_id
        self.app_name = "agent-browser"

    def _run_infsh(self, function: str, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Runs the infsh CLI command and returns the parsed JSON result."""
        cmd = [
            "infsh", "app", "run", self.app_name,
            "--function", function,
            "--session", self.session_id,
            "--input", json.dumps(input_data)
        ]

        logger.debug(f"Executing: {' '.join(cmd)}")
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            # Find the JSON part in the output (infsh sometimes prints progress bars)
            lines = result.stdout.strip().split("\n")
            json_str = ""
            for line in lines:
                if line.strip().startswith("{") and line.strip().endswith("}"):
                    json_str = line.strip()
                    break

            if not json_str:
                # Try to find JSON if it's mixed with other text
                import re
                match = re.search(r'\{.*\}', result.stdout, re.DOTALL)
                if match:
                    json_str = match.group(0)
                else:
                    raise ValueError(f"No JSON output found in infsh result: {result.stdout}")

            data = json.loads(json_str)

            # Update session_id if it was 'new'
            if self.session_id == "new" and "session_id" in data:
                self.session_id = data["session_id"]
                logger.info(f"Started new session: {self.session_id}")

            return data
        except subprocess.CalledProcessError as e:
            logger.error(f"infsh command failed: {e.stderr}")
            raise RuntimeError(f"infsh error: {e.stderr}")
        except Exception as e:
            logger.error(f"Error parsing infsh output: {e}")
            raise

    async def open(self, url: str, **kwargs) -> Dict[str, Any]:
        """Navigate to URL and start/reuse session."""
        input_data = {"url": url}
        input_data.update(kwargs)
        return await asyncio.to_thread(self._run_infsh, "open", input_data)

    async def snapshot(self) -> Dict[str, Any]:
        """Re-fetch page state with @e refs."""
        return await asyncio.to_thread(self._run_infsh, "snapshot", {})

    async def interact(self, action: str, **kwargs) -> Dict[str, Any]:
        """Perform an action (click, fill, type, etc.)."""
        input_data = {"action": action}
        input_data.update(kwargs)
        return await asyncio.to_thread(self._run_infsh, "interact", input_data)

    async def screenshot(self, full_page: bool = False) -> Dict[str, Any]:
        """Take a screenshot."""
        return await asyncio.to_thread(self._run_infsh, "screenshot", {"full_page": full_page})

    async def execute(self, code: str) -> Dict[str, Any]:
        """Execute JavaScript on the page."""
        return await asyncio.to_thread(self._run_infsh, "execute", {"code": code})

    async def close(self) -> Dict[str, Any]:
        """Close the browser session."""
        return await asyncio.to_thread(self._run_infsh, "close", {})
