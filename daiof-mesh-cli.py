# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

#!/usr/bin/env python3
import argparse
import os
import sys
import importlib.util
from pathlib import Path

# Paths setup
BASE_DIR = Path("/Users/andy/my_too_test")
AGENTS_DIR = BASE_DIR / "autonomous_operator" / "nodes" / "agents"
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "autonomous_operator"))
sys.path.append(str(BASE_DIR / "autonomous_operator" / "nodes"))

def list_agents():
    agents = []
    for f in os.listdir(AGENTS_DIR):
        if f.endswith("_agent.py") and not f.startswith("base_"):
            agents.append(f.replace("_agent.py", ""))
    return sorted(agents)

def run_agent(agent_name, action=None, args=None):
    file_name = f"{agent_name.lower().replace('-', '_')}_agent.py"
    file_path = AGENTS_DIR / file_name

    if not file_path.exists():
        print(f"❌ Agent '{agent_name}' ({file_name}) not found.")
        return

    # Dynamic import
    spec = importlib.util.spec_from_file_location(agent_name, file_path)
    module = importlib.util.module_from_spec(spec)
    # Thêm agents path vào sys.path cho module có thể import base_agent
    sys.path.insert(0, str(AGENTS_DIR))
    spec.loader.exec_module(module)

    # Identify the agent class
    class_name = agent_name.replace("-", "").replace("_", "").capitalize() + "Agent"
    if not class_name.endswith("AgentAgent"): # Fix for already ending with agent
        pass

    # Thử tìm class trong module
    agent_class = None
    for attr in dir(module):
        if attr.lower().endswith("agent") and attr != "DAIOFAgent":
            agent_class = getattr(module, attr)
            break

    if not agent_class:
        print(f"❌ Could not find agent class in {file_name}")
        return

    instance = agent_class()
    print(f"🌀 Invoking Agent: {instance.agent_name}...")
    result = instance.run_cycle(command_args=args)
    print(f"✅ Result: {result}")

def main():
    parser = argparse.ArgumentParser(description="DAIOF AI CLI Mesh Control Center")
    parser.add_argument("--list", action="store_true", help="List all specialized agents")
    parser.add_argument("--agent", type=str, help="Target agent name")
    parser.add_argument("--action", type=str, help="Action to execute (default: pulse)")
    parser.add_argument("--args", type=str, help="JSON arguments for the action")
    parser.add_argument("--all", action="store_true", help="Run all agents in sequence")

    args = parser.parse_args()

    if args.list:
        agents = list_agents()
        print("🤖 Available Specialized Agents:")
        for a in agents:
            print(f"  - {a}")
        return

    if args.all:
        agents = list_agents()
        for a in agents:
            try:
                run_agent(a, args.action, args.args)
            except Exception as e:
                print(f"❌ Failed to run {a}: {e}")
        return

    if args.agent:
        run_agent(args.agent, args.action, args.args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
