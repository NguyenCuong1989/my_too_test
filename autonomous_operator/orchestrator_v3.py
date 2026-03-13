# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

import asyncio
import logging
import sys
import os
import json
from datetime import datetime
from pathlib import Path

# Thêm path để import từ DAIOF-Framework
BASE_DIR = Path("/Users/andy/my_too_test")
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "autonomous_operator"))
sys.path.append(str(BASE_DIR / "autonomous_operator" / "nodes"))
sys.path.append(str(BASE_DIR / "DAIOF-Framework"))
sys.path.append(str(BASE_DIR / "balancehub"))

try:
    from app.core import apo_canon
except ImportError:
    apo_canon = None

from config import HEARTBEAT_INTERVAL, LOG_DIR, NOTION_TOKEN, NOTION_DB_ID
from nodes.biz_node import BizNode
from nodes.guardian_node import GuardianNode
from nodes.recovery_node import RecoveryNode
from nodes.web_node import WebNode
from nodes.audit_node import AuditNode
from neural_link import NeuralLink
from balance_integration import BalanceGovernor
from notion_client import Client
from hyperai_phoenix.app.brain.coordinator import MetaOptimizationCoordinator

# Import từ Framework gốc của Master
try:
    from digital_ai_organism_framework import SymphonyControlCenter
except ImportError:
    SymphonyControlCenter = None

# Cấu hình LOG
class NdjsonFormatter(logging.Formatter):
    def format(self, record):
        log_obj = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "name": record.name,
            "message": record.getMessage()
        }
        return json.dumps(log_obj)

ndjson_handler = logging.FileHandler("/tmp/observe.ndjson")
ndjson_handler.setFormatter(NdjsonFormatter())

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("/tmp/orchestrator.log"),
        ndjson_handler,
        logging.StreamHandler(sys.stdout)
    ]
)

class AutonomousOperator:
    def __init__(self):
        self.logger = logging.getLogger("DAIOF_ORCHESTRATOR")
        self.logger.info("🔥 DAIOF AUTONOMOUS OPERATOR v3.9 (GOVERNANCE-ENABLED) ACTIVATED")

        # 🧠 Neural Bridge & Framework Link
        self.link = NeuralLink()
        self.symphony = SymphonyControlCenter() if SymphonyControlCenter else None
        self.governor = BalanceGovernor() # Master's Economic Governor (BalanceHub)

        # 🤖 Nodes Initialization
        self.biz = BizNode()
        self.guardian = GuardianNode()
        self.recovery = RecoveryNode()
        self.web = WebNode()
        self.audit = AuditNode()

        # 🧠 PHOENIX COGNITIVE HEART (Kernel v1.1)
        self.phoenix = MetaOptimizationCoordinator(
            config_path="/Users/andy/my_too_test/hyperai_phoenix/configs",
            data_path="/tmp/daiof_data"
        )

        # Map nodes for iteration (Static Nodes)
        self.nodes = {
            "Recovery": self.recovery,
            "WebScout": self.web,
            "BizService": self.biz,
            "Guardian": self.guardian,
            "AuditNode": self.audit
        }

        # ⚖️ CANONICAL TOPOLOGY GROUPS (O -> R -> E -> P -> L -> I -> F -> B)
        self.operator_sequence = ["O", "R", "E", "P", "L", "I", "F", "B"]
        self.canonical_groups = {op: [] for op in self.operator_sequence}
        self.rebuild_canonical_topology()

        # 🌐 Dynamic AI CLI Mesh Loading
        self.load_mesh_agents()

        # 🏛️ Notion Hub (Command Center)
        self.notion = Client(auth=NOTION_TOKEN) if NOTION_TOKEN else None
        self.notion_db_id = NOTION_DB_ID

        # 🎼 Register components with Master's Symphony
        if self.symphony:
            self.symphony.register_component("AutonomousOperator_v3", self)
            for name, node in self.nodes.items():
                self.symphony.register_component(name, node)

        self.is_running = False

    def load_mesh_agents(self):
        """Tự động quét và nạp các Specialized Agents từ thư mục agents/."""
        import importlib.util
        agents_dir = BASE_DIR / "autonomous_operator" / "nodes" / "agents"
        if not agents_dir.exists():
            return

        self.logger.info("📡 Scanning for Specialized Agents in Mesh...")
        # Thêm agents path vào sys.path một lần duy nhất
        if str(agents_dir) not in sys.path:
            sys.path.insert(0, str(agents_dir))

        for f in os.listdir(agents_dir):
            if f.endswith("_agent.py") and not f.startswith("base_"):
                agent_name = f.replace("_agent.py", "").replace("_", " ").title().replace(" ", "")
                file_path = agents_dir / f

                try:
                    spec = importlib.util.spec_from_file_location(agent_name, file_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)

                    # Tìm agent class (vd: StripeAgent)
                    agent_class = None
                    for attr in dir(module):
                        if attr.lower().endswith("agent") and attr != "DAIOFAgent":
                            agent_class = getattr(module, attr)
                            break

                    if agent_class:
                        instance = agent_class()
                        # Use the canonical agent_name if available in instance
                        final_id = getattr(instance, "agent_name", agent_name)
                        self.nodes[final_id] = instance
                        self.logger.info(f"✅ Mesh Agent Registered: {final_id}")
                except Exception as e:
                    self.logger.error(f"❌ Failed to load Mesh Agent {f}: {e}")

        # Re-build topology after dynamic loading
        self.rebuild_canonical_topology()

    def rebuild_canonical_topology(self):
        """Map all registered nodes to their Σ_APΩ–COS operator ID."""
        for op in self.operator_sequence:
            self.canonical_groups[op] = []

        for name, node in self.nodes.items():
            op_id = "I" # Default to Interface
            if apo_canon:
                op_id = apo_canon.operator_id_for(name)

            # Manual overrides for nodes not in balancehub binding mapping
            if name == "Recovery": op_id = "O"
            elif name == "WebScout": op_id = "P"
            elif name == "Guardian": op_id = "L"
            elif name == "AuditNode": op_id = "L"
            elif name == "BizService": op_id = "I"

            if op_id in self.canonical_groups:
                self.canonical_groups[op_id].append(name)

        self.logger.info(f"⚖️ Canonical Topology Rebuilt: { {k: v for k, v in self.canonical_groups.items() if v} }")

    async def main_loop(self):
        """Vòng lặp điều hành chính — Trực chiến 24/7"""
        self.is_running = True
        cycle_count = 0
        self.logger.info("🚀 Orchestrator: TERRITORY GOVERNANCE ACTIVE")

        while self.is_running:
            cycle_count += 1
            start_time = datetime.now()
            self.logger.info(f"--- 🌀 CYCLE {cycle_count} STARTING ---")

            try:
                # 0. Poll Commands from Notion (Master's Directives)
                await self.poll_notion_commands()

                # 1. Governance Check (BalanceHub)
                health_data = self.governor.get_system_health()
                if health_data:
                    self.logger.info(f"⚖️ Governance: GSSI {health_data.get('gssi', 'N/A')}")

                # 2. Log Cycle Start to Notion
                self.log_to_notion("Cycle Start", "SYSTEM", f"Initiating Cycle {cycle_count}. Σ_APΩ–COS Topology Active.")

                # 3. Execute Service Mesh strictly by Canonical Order (O -> E -> P -> L -> I -> F -> B)
                # Note: Handling δ(s) state transition with Fail-Closed logic.
                cycle_healthy = True

                for op_id in self.operator_sequence:
                    if not cycle_healthy and op_id not in ["F", "B"]:
                        # Skip processing normal nodes if system state is invalid
                        continue

                    node_names = self.canonical_groups.get(op_id, [])
                    for name in node_names:
                        node = self.nodes[name]
                        self.logger.info(f"⚡ [OP:{op_id}] Executing Node: {name}")
                        try:
                            result = None
                            if asyncio.iscoroutinefunction(node.run_cycle):
                                result = await node.run_cycle()
                            else:
                                result = node.run_cycle()

                            # 🛡️ FAIL-CLOSED DETECTION: If node returns False or explicit Failure
                            if result is False:
                                self.logger.warning(f"⚠️ Node {name} returned failure state. Activating Fail-Closed.")
                                cycle_healthy = False

                        except Exception as node_err:
                            self.logger.error(f"❌ Node {name} crashed: {node_err}")
                            self.log_to_notion("NODE_FAILURE", name, str(node_err)[:200], priority="High")
                            cycle_healthy = False # Protocol violation/crash leads to ⊥

                # 4. Global Service Orchestration (Governance Logging)
                self.service_orchestration()

                # 5. Log Cycle Completion & Governance Stats
                summary = f"Cycle {cycle_count} complete."
                if health_data:
                    summary += f" System GSSI: {health_data.get('gssi', 'N/A')}"

                self.log_to_notion("Cycle Complete", "SYSTEM", summary)

                duration = datetime.now() - start_time
                self.logger.info(f"✅ CYCLE {cycle_count} FINISHED (Duration: {duration})")
                self.logger.info(f"💤 Sleeping for {HEARTBEAT_INTERVAL} seconds...")
                await asyncio.sleep(HEARTBEAT_INTERVAL)

            except Exception as e:
                self.logger.error(f"🚨 CRITICAL ERROR in main loop: {e}")
                self.log_to_notion("SYSTEM_ERROR", "FAILURE", str(e)[:200], priority="High")
                await asyncio.sleep(60)

    async def poll_notion_commands(self):
        """Đọc lệnh (Command) từ Dashboard Notion để thực thi ngay lập tức."""
        if not self.notion or not self.notion_db_id:
            return
        self.logger.info("📡 Checking for Master's directives in Notion...")
        try:
            results = self.notion.databases.query(
                **{
                    "database_id": self.notion_db_id,
                    "filter": {
                        "property": "Status",
                        "select": {
                            "equals": "Execute"
                        }
                    }
                }
            )
            tasks = results.get('results', [])
            if tasks:
                self.logger.info(f"⚡ Found {len(tasks)} commands awaiting execution!")
                for task in tasks:
                    page_id = task['id']
                    props = task.get('properties', {})

                    # Extract Command Metadata
                    cmd_name_obj = props.get("Command Name", {}).get("title", [])
                    cmd_name = cmd_name_obj[0]["plain_text"] if cmd_name_obj else "Unknown"

                    target_obj = props.get("Target", {}).get("select", {})
                    target = target_obj.get("name", "Local") if target_obj else "Local"

                    args_obj = props.get("Arguments", {}).get("rich_text", [])
                    args = args_obj[0]["plain_text"] if args_obj else ""

                    self.logger.info(f"⚔️ Executing Directive: [{target}] {cmd_name}")

                    # Log execution start
                    self.log_to_notion(f"Executing: {cmd_name}", target, f"Target: {target} | Args: {args}")

                    # Execute logic based on Target
                    result_msg = "Command processed successfully."
                    success = True
                    try:
                        # ⚖️ CANON LY: Execution and Audit must be bound
                        node_to_run = self.nodes.get(target)
                        if not node_to_run:
                            result_msg = f"Unknown Target: {target}. Command logged but not executed."
                            self.logger.warning(result_msg)
                            success = False
                        else:
                            # ⚡ Execute Node with Arguments
                            if asyncio.iscoroutinefunction(node_to_run.run_cycle):
                                await node_to_run.run_cycle(command_args=args)
                            else:
                                node_to_run.run_cycle(command_args=args)

                            # 📑 AUDIT LOG (Mandatory Proof)
                            self.link.log_service_event(
                                service="Orchestrator",
                                e_type="COMMAND_EXEC",
                                content=f"Executed {cmd_name} on {target} with args: {args}",
                                meta=json.dumps({"task_id": page_id, "success": True})
                            )

                    except Exception as exe_err:
                        success = False
                        result_msg = f"Execution Failed: {exe_err}"
                        self.logger.error(result_msg)
                        self.link.log_service_event(
                            service="Orchestrator",
                            e_type="COMMAND_FAILURE",
                            content=f"Failed {cmd_name} on {target}: {exe_err}",
                            meta=json.dumps({"task_id": page_id, "success": False})
                        )

                    # Update Status back to Notion (Verdict)
                    new_status = "Complete" if success else "Failed"
                    self.notion.pages.update(
                        page_id=page_id,
                        properties={
                            "Status": {"select": {"name": new_status}},
                            "Snippet": {"rich_text": [{"text": {"content": result_msg[:1000]}}]}
                        }
                    )
                    self.logger.info(f"✅ Directive Status Updated: {new_status}")
        except Exception as e:
            self.logger.error(f"Failed to poll Notion commands: {e}")

    def log_to_notion(self, event_type, category, message, priority="Medium"):
        """Gửi log vận hành trực tiếp lên Notion Dashboard."""
        if not self.notion or not self.notion_db_id:
            return
        try:
            self.notion.pages.create(
                parent={"database_id": self.notion_db_id},
                properties={
                    "Name": {"title": [{"text": {"content": f"⚙️ {event_type}: Pulse"}}]},
                    "Status": {"select": {"name": "Operation Log"}},
                    "Category": {"select": {"name": category}},
                    "Sentiment": {"select": {"name": "Neutral"}},
                    "Priority": {"select": {"name": priority}},
                    "Reason": {"rich_text": [{"text": {"content": event_type}}]},
                    "Snippet": {"rich_text": [{"text": {"content": message[:1500]}}]}
                }
            )
        except Exception as e:
            self.logger.error(f"Failed to log to Notion: {e}")

    def service_orchestration(self):
        """Global Service Health Monitoring."""
        log_count = len(self.link.get_service_logs(10))
        self.logger.info(f"🏢 Service Mesh Audit: {log_count} recent events registered.")
        if log_count > 50:
             self.link.log_service_event("Orchestrator", "STATUS", "Service mesh traffic high, resources optimal.")

if __name__ == "__main__":
    operator = AutonomousOperator()
    # Start Phoenix Bridge
    operator.phoenix.start()
    try:
        asyncio.run(operator.main_loop())
    except KeyboardInterrupt:
        operator.logger.info("Stopping Operator...")
        operator.phoenix.stop()
        operator.is_running = False
