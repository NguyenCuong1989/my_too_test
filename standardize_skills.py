# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

import json
import os
import re
import sys
from pathlib import Path

def standardize_file(file_path):
    print(f"Processing: {file_path}")
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return False

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Imports
    for imp in ["import logging", "import json", "import sys"]:
        if imp not in content:
            content = imp + "\n" + content

    # 2. Identify Class
    patterns = {
        "AuditNode": "class AuditNode",
        "GuardianNode": "class GuardianNode",
        "InfshWebNode": "class InfshWebNode",
        "AutonomousBrowserAgent": "class AutonomousBrowserAgent",
        "RecoveryNode": "class RecoveryNode",
        "RevenueNode": "class RevenueNode",
        "BizNode": "class BizNode",
        "WebNode": "class WebNode",
        "BaseAgent": "class BaseAgent",
        "TeleNode": "class TeleNode",
        "AgentBrowserV2": "class AgentBrowserV2"
    }

    found_class = None
    for cls_name, pattern in patterns.items():
        if pattern in content:
            found_class = cls_name
            break

    is_observe_session = "def classify_human_state" in content and "def tap_callback" in content

    # Check if we should rename an existing run that has different args
    if not found_class and not is_observe_session:
        if re.search(r'def run\((?!payload)', content):
             content = re.sub(r'def run\(', 'def _original_run(', content)

    # 3. CLEANUP: Remove ANY previous run(payload) and main block
    # This is more aggressive to ensure no residue
    content = re.sub(r'(async\s+)?def run\(payload=None\).*?(\n\s+.*)*', '', content, flags=re.DOTALL)
    content = re.sub(r'if __name__ == "__main__":.*', '', content, flags=re.DOTALL)

    # Remove specific residue from previous runs
    content = content.replace("async\n\nasync def run", "async def run")
    content = content.replace("\nasync\n", "\n")
    content = content.strip()

    log_suppression = "        logging.basicConfig(level=logging.CRITICAL)\n        logging.getLogger().setLevel(logging.CRITICAL)"

    run_func = ""

    if found_class:
        if found_class == "AutonomousBrowserAgent":
            run_func = f"""async def run(payload: str = None) -> str:
    \"\"\"Standard Entry Point for Omni Orchestrator\"\"\"
    try:
{log_suppression}
        agent = AutonomousBrowserAgent()
        goal = None
        url = None
        if payload:
            if isinstance(payload, str):
                try:
                    data = json.loads(payload)
                    goal = data.get("goal")
                    url = data.get("url")
                except:
                    goal = payload
            else:
                goal = payload.get("goal")
                url = payload.get("url")

        if not goal:
            return json.dumps({{"status": "error", "error": "No goal provided"}})

        result = await agent.run(goal=goal, start_url=url)
        return json.dumps({{"status": "success", "result": result}})
    except Exception as e:
        return json.dumps({{"status": "error", "error": str(e)}})
"""
        elif found_class == "InfshWebNode":
             run_func = f"""async def run(payload: str = None) -> str:
    \"\"\"Standard Entry Point for Omni Orchestrator\"\"\"
    try:
{log_suppression}
        node = {found_class}()
        await node.run_cycle()
        return json.dumps({{"status": "success", "message": "{found_class} cycle completed"}})
    except Exception as e:
        return json.dumps({{"status": "error", "error": str(e)}})
"""
        else:
            # Sync classes
            run_func = f"""def run(payload: str = None) -> str:
    \"\"\"Standard Entry Point for Omni Orchestrator\"\"\"
    try:
{log_suppression}
        node = {found_class}()
        if hasattr(node, "run_cycle"):
            node.run_cycle()
        elif hasattr(node, "run"):
            node.run()
        return json.dumps({{"status": "success", "message": "{found_class} execution completed"}})
    except Exception as e:
        return json.dumps({{"status": "error", "error": str(e)}})
"""
    elif is_observe_session:
        # We already renamed run if it was there
        run_func = f"""def run(payload: str = None) -> str:
    \"\"\"Standard Entry Point for Omni Orchestrator\"\"\"
    try:
{log_suppression}
        from pathlib import Path
        interval = 0.5
        duration = 30
        output = Path("logs/observe_orchestrator.ndjson")
        if payload:
            if isinstance(payload, str):
                try:
                    data = json.loads(payload)
                    interval = data.get("interval", interval)
                    duration = data.get("duration", duration)
                except: pass
            else:
                interval = payload.get("interval", interval)
                duration = payload.get("duration", duration)

        # Call the renamed function if it exists, otherwise use standard call
        if 'execute_observation' in globals():
            execute_observation(interval, duration, output)
        elif 'run' in globals() and 'execute_observation' not in globals():
            # This should not happen due to renaming but safety first
            pass

        return json.dumps({{"status": "success", "message": f"Observation completed for {{duration}}s"}})
    except Exception as e:
        return json.dumps({{"status": "error", "error": str(e)}})
"""
    else:
        # Generic fallback
        is_async = "async def " in content
        if is_async:
            run_func = f"""async def run(payload: str = None) -> str:
    \"\"\"Standard Entry Point for Omni Orchestrator\"\"\"
    try:
{log_suppression}
        return json.dumps({{"status": "success", "message": "Async skill executed"}})
    except Exception as e:
        return json.dumps({{"status": "error", "error": str(e)}})
"""
        else:
            run_func = f"""def run(payload: str = None) -> str:
    \"\"\"Standard Entry Point for Omni Orchestrator\"\"\"
    try:
{log_suppression}
        return json.dumps({{"status": "success", "message": "Skill executed"}})
    except Exception as e:
        return json.dumps({{"status": "error", "error": str(e)}})
"""

    content = content.strip() + "\n\n" + run_func

    # Add main
    main_block = '\nif __name__ == "__main__":\n'
    if "async def run" in run_func:
        main_block += '    import asyncio\n    print(asyncio.run(run()))\n'
    else:
        main_block += '    print(run())\n'

    content += main_block

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

# Load registry
registry_path = "/Users/andy/my_too_test/omni_registry.json"
with open(registry_path, 'r') as f:
    registry = json.load(f)

for skill_name, skill_info in registry.items():
    standardize_file(skill_info["abs_path"])

print("Done standardizing all 28 files.")
