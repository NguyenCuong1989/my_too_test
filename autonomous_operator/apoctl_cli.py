# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

import sys
import argparse
import logging
from pathlib import Path

# Add paths
BASE_DIR = Path("/Users/andy/my_too_test")
sys.path.append(str(BASE_DIR / "autonomous_operator"))

try:
    import factory_utils
except ImportError:
    factory_utils = None

# Cấu hình LOG
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [APOCTL] [%(levelname)s] %(message)s'
)

class ApoctlCLI:
    def __init__(self):
        self.logger = logging.getLogger("APOCTL")

    def run(self):
        parser = argparse.ArgumentParser(description="Σ_APΩ–COS Software Factory CLI")
        parser.add_argument("operator", help="Canonical Operator ID (O, R, E, P, L, I, F, B)")
        parser.add_argument("action", help="Action description or ID")
        parser.add_argument("--args", help="Optional JSON arguments", default="{}")

        args = parser.parse_args()
        self.execute(args.operator, args.action, args.args)

    def execute(self, op_id, action, extra_args):
        self.logger.info(f"🚀 Executing {op_id} action: {action}")

        # 🛡️ FACTORY LOGIC
        if op_id == "F":
            self.logger.error(f"🚨 Failure Sink: {action}")
            if factory_utils:
                factory_utils.log_to_notion("FAILURE_SINK", "FACTORY", action, priority="High")

        elif op_id == "E":
            self.logger.info(f"⚡ Event Trigger: {action}")
            # Proactive Audit on Failure Trigger
            if any(word in action.lower() for word in ["audit", "failed", "failure"]):
                if factory_utils:
                    self.logger.info("🧠 Protocol O -> E: Initiating Self-Healing Audit...")
                    analysis = factory_utils.self_heal_audit(f"Error Context: {action}")
                    self.logger.info(f"🧠 AI Analysis Result: {analysis}")
                    factory_utils.log_to_notion("AI_AUDIT", "FACTORY", f"Context: {action}\nAnalysis: {analysis}")
                else:
                    self.logger.warning("⚠️ factory_utils not loaded. Skipping AI Audit.")

        elif op_id == "L":
            self.logger.info(f"📊 Logging state: {action}")
            if factory_utils:
                factory_utils.log_to_notion("OBSERVE_LOG", "FACTORY", action)

        elif op_id == "I":
            self.logger.info(f"🤝 Interface update: {action}")
            if factory_utils:
                factory_utils.log_to_notion("INTERFACE_EVENT", "FACTORY", action)

        print(f"DONE: {op_id}:{action}")

if __name__ == "__main__":
    cli = ApoctlCLI()
    cli.run()
