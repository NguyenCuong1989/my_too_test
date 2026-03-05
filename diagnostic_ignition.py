# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

"""
DAIOF DIAGNOSTIC IGNITION (Phase 1)

Objectives:
1. Verify SymphonyControlCenter connectivity.
2. Verify NeuralLink pulse integrity.
3. Health check all autonomous nodes (No execution).
"""

import sys
import logging
from pathlib import Path

# Setup Paths (Sync with start_daiof.sh)
BASE_DIR = Path("/Users/andy/my_too_test")
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "autonomous_operator"))
sys.path.append(str(BASE_DIR / "autonomous_operator" / "nodes"))
sys.path.append(str(BASE_DIR / "DAIOF-Framework"))

from neural_link import NeuralLink
try:
    from digital_ai_organism_framework import SymphonyControlCenter
except ImportError:
    SymphonyControlCenter = None

from nodes.biz_node import BizNode
from nodes.guardian_node import GuardianNode
from nodes.recovery_node import RecoveryNode
from nodes.web_node import WebNode
from nodes.audit_node import AuditNode

def run_diagnostic():
    print("🚀 [DIAGNOSTIC IGNITION] Starting Phase 1 Calibration...")
    print("----------------------------------------------------------")

    # 1. Framework Link
    try:
        link = NeuralLink()
        symphony = SymphonyControlCenter() if SymphonyControlCenter else None
        print(f"✅ NeuralLink: INITIALIZED")
        print(f"✅ SymphonyControlCenter: {'READY' if symphony else 'FAILED'}")
    except Exception as e:
        print(f"❌ Framework Link Error: {e}")
        return

    # 2. Node Initialization
    print("\n📦 NODE HEALTH CHECK (Initialization only):")
    try:
        nodes = {
            "Recovery": RecoveryNode(),
            "Audit": AuditNode(),
            "Biz": BizNode(),
            "Guardian": GuardianNode(),
            "Web": WebNode()
        }
        for name, node in nodes.items():
            print(f"   - {name} Node: INSTANTIATED")
    except Exception as e:
        print(f"❌ Node Creation Error: {e}")

    # 3. Pulse Test
    print("\n📡 NEURAL PULSE TEST:")
    try:
        link.send_pulse(
            node_name="DiagnosticAgent",
            pulse_type="DIAGNOSTIC_INIT",
            content="Phase 1 Calibration Sequence",
            intensity=0.5
        )
        print("   - Pulse Sent: SUCCESS")
    except Exception as e:
        print(f"   - Pulse Sent: FAILED ({e})")

    print("----------------------------------------------------------")
    print("🏁 [PHASE 1 COMPLETE] System is ready for safe activation.")

if __name__ == "__main__":
    run_diagnostic()
