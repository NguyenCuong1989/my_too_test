import asyncio
import logging
import sys
import os
from datetime import datetime
from pathlib import Path

# Thêm path để import từ DAIOF-Framework
BASE_DIR = Path("/Users/andy/my_too_test")
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "autonomous_operator"))
sys.path.append(str(BASE_DIR / "autonomous_operator" / "nodes"))
sys.path.append(str(BASE_DIR / "DAIOF-Framework"))

from config import HEARTBEAT_INTERVAL, LOG_DIR
from nodes.biz_node import BizNode
from nodes.guardian_node import GuardianNode
from nodes.recovery_node import RecoveryNode
from nodes.web_node import WebNode
from nodes.audit_node import AuditNode
from neural_link import NeuralLink

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

logger = logging.getLogger("DAIOF_ORCHESTRATOR")

class AutonomousOperator:
    def __init__(self):
        logger.info("🔥 DAIOF AUTONOMOUS OPERATOR v3.8 (NEURAL-LINKED) ACTIVATED")

        # 🧠 Neural Bridge & Framework Link
        self.link = NeuralLink()
        self.symphony = SymphonyControlCenter() if SymphonyControlCenter else None

        # 🤖 Nodes
        self.biz = BizNode()
        self.guardian = GuardianNode()
        self.recovery = RecoveryNode()
        self.web = WebNode()
        self.audit = AuditNode()

        # 🎼 Register components with Master's Symphony
        if self.symphony:
            self.symphony.register_component("AutonomousOperator_v3", self)
            self.symphony.register_component("BizNode", self.biz)
            self.symphony.register_component("GuardianNode", self.guardian)
            self.symphony.register_component("RecoveryNode", self.recovery)
            self.symphony.register_component("WebNode", self.web)
            self.symphony.register_component("AuditNode", self.audit)

        self.is_running = True

    async def main_loop(self):
        cycle_count = 0
        while self.is_running:
            cycle_count += 1
            start_time = datetime.now()
            logger.info(f"--- 🌀 CYCLE {cycle_count} STARTING (Neural Link Active) ---")

            # Gửi tín hiệu nhịp tim vào hệ thống thần kinh trung tâm
            self.link.send_pulse(
                node_name="Orchestrator",
                pulse_type="HEARTBEAT",
                content=f"Cycle {cycle_count} initiated",
                intensity=1.0
            )

            # 1. Recovery Node
            try:
                self.recovery.run_cycle()
            except Exception as e:
                logger.error(f"Recovery Node failed: {e}")

            # 2. Web Node (Async)
            try:
                await self.web.run_cycle()
            except Exception as e:
                logger.error(f"Web Node failed: {e}")

            # 3. Biz Node
            try:
                self.biz.run_cycle()
            except Exception as e:
                logger.error(f"Biz Node failed: {e}")

            # 4. Guardian Node
            try:
                self.guardian.run_cycle()
            except Exception as e:
                logger.error(f"Guardian Node failed: {e}")

            # 5. Audit Node (Bài kiểm tra)
            try:
                self.audit.run_cycle()
            except Exception as e:
                logger.error(f"Audit Node failed: {e}")

            # 📊 Báo cáo tiến độ lên Symphony
            if self.symphony:
                self.symphony.conduct_symphony()

            duration = datetime.now() - start_time
            logger.info(f"--- ✅ CYCLE {cycle_count} COMPLETED (Duration: {duration}) ---")

            # Lưu PID để Eternal Monitor theo dõi
            with open(BASE_DIR / "autonomous_operator" / "state" / "orchestrator.pid", "w") as f:
                f.write(str(os.getpid()))

            await asyncio.sleep(HEARTBEAT_INTERVAL)

if __name__ == "__main__":
    operator = AutonomousOperator()
    try:
        asyncio.run(operator.main_loop())
    except KeyboardInterrupt:
        logger.info("Stopping Operator...")
        operator.is_running = False
