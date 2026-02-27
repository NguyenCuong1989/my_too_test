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

from config import HEARTBEAT_INTERVAL, LOG_DIR, NOTION_TOKEN, NOTION_DB_ID
from nodes.biz_node import BizNode
from nodes.guardian_node import GuardianNode
from nodes.recovery_node import RecoveryNode
from nodes.web_node import WebNode
from nodes.audit_node import AuditNode
from neural_link import NeuralLink
from balance_integration import BalanceGovernor
from notion_client import Client

# Import từ Framework gốc của Master
try:
    from digital_ai_organism_framework import SymphonyControlCenter
except ImportError:
    SymphonyControlCenter = None

# Cấu hình LOG
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(LOG_DIR / "orchestrator.log"),
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

        # Map nodes for iteration
        self.nodes = {
            "Recovery": self.recovery,
            "WebScout": self.web,
            "BizService": self.biz,
            "Guardian": self.guardian,
            "AuditNode": self.audit
        }

        # 🏛️ Notion Hub (Command Center)
        self.notion = Client(auth=NOTION_TOKEN) if NOTION_TOKEN else None
        self.notion_db_id = NOTION_DB_ID

        # 🎼 Register components with Master's Symphony
        if self.symphony:
            self.symphony.register_component("AutonomousOperator_v3", self)
            for name, node in self.nodes.items():
                self.symphony.register_component(name, node)

        self.is_running = False

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
                self.log_to_notion("Cycle Start", "SYSTEM", f"Initiating Cycle {cycle_count}. Governance Active.")

                # 3. Execute Service Mesh Sequential
                for name, node in self.nodes.items():
                    self.logger.info(f"⚡ Executing Node: {name}")
                    try:
                        if asyncio.iscoroutinefunction(node.run_cycle):
                            await node.run_cycle()
                        else:
                            node.run_cycle()
                    except Exception as node_err:
                        self.logger.error(f"❌ Node {name} failed: {node_err}")
                        self.log_to_notion("NODE_FAILURE", name, str(node_err)[:200], priority="High")

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
                    success = True
                    result_msg = "Command processed successfully."
                    try:
                        if target == "WebScout":
                            self.web.run_cycle() # Basic execution, can be enhanced with args
                        elif target == "BizService":
                            self.biz.run_cycle()
                        elif target == "Guardian":
                            self.guardian.run_cycle()
                        else:
                            result_msg = f"Unknown Target: {target}. Command logged but not executed."
                            self.logger.warning(result_msg)
                    except Exception as exe_err:
                        success = False
                        result_msg = f"Execution Failed: {exe_err}"
                        self.logger.error(result_msg)

                    # Update Status back to Notion
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
    try:
        asyncio.run(operator.main_loop())
    except KeyboardInterrupt:
        operator.logger.info("Stopping Operator...")
        operator.is_running = False
