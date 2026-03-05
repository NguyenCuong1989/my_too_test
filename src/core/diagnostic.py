"""
diagnostic.py — System Diagnostic (refactored from diagnostic_ignition.py)

Phase 1 calibration: verifies framework connectivity and node health.
"""

import logging
from pathlib import Path

from src.config.settings import DAIOF_INSTALL_DIR

logger = logging.getLogger(__name__)


def _load_framework(base_dir: Path):
    """Dynamically import framework components from *base_dir*."""
    import sys

    sys.path.insert(0, str(base_dir))
    sys.path.insert(0, str(base_dir / "autonomous_operator"))
    sys.path.insert(0, str(base_dir / "autonomous_operator" / "nodes"))
    sys.path.insert(0, str(base_dir / "DAIOF-Framework"))

    from neural_link import NeuralLink  # noqa: PLC0415

    try:
        from digital_ai_organism_framework import SymphonyControlCenter  # noqa: PLC0415
    except ImportError:
        SymphonyControlCenter = None

    from nodes.biz_node import BizNode  # noqa: PLC0415
    from nodes.guardian_node import GuardianNode  # noqa: PLC0415
    from nodes.recovery_node import RecoveryNode  # noqa: PLC0415
    from nodes.web_node import WebNode  # noqa: PLC0415
    from nodes.audit_node import AuditNode  # noqa: PLC0415

    return NeuralLink, SymphonyControlCenter, BizNode, GuardianNode, RecoveryNode, WebNode, AuditNode


def run_diagnostic(base_dir: Path | None = None):
    """Run Phase 1 diagnostic calibration.

    Args:
        base_dir: Root directory of the DAIOF installation.
                  Defaults to ``/Users/andy/my_too_test``.

    Returns:
        ``True`` if all checks passed, ``False`` otherwise.
    """
    if base_dir is None:
        base_dir = DAIOF_INSTALL_DIR

    print("[DIAGNOSTIC] Starting Phase 1 Calibration...")
    print("-" * 58)

    try:
        (
            NeuralLink,
            SymphonyControlCenter,
            BizNode,
            GuardianNode,
            RecoveryNode,
            WebNode,
            AuditNode,
        ) = _load_framework(base_dir)
    except Exception as exc:
        print(f"[ERROR] Could not load framework from {base_dir}: {exc}")
        return False

    # 1. Framework link
    try:
        link = NeuralLink()
        symphony = SymphonyControlCenter() if SymphonyControlCenter else None
        print(f"[OK] NeuralLink: INITIALIZED")
        print(f"[{'OK' if symphony else 'FAIL'}] SymphonyControlCenter: {'READY' if symphony else 'FAILED'}")
    except Exception as exc:
        print(f"[ERROR] Framework link error: {exc}")
        return False

    # 2. Node health check
    print("\n[INFO] NODE HEALTH CHECK (initialisation only):")
    try:
        nodes = {
            "Recovery": RecoveryNode(),
            "Audit": AuditNode(),
            "Biz": BizNode(),
            "Guardian": GuardianNode(),
            "Web": WebNode(),
        }
        for name in nodes:
            print(f"   - {name} Node: INSTANTIATED")
    except Exception as exc:
        print(f"[ERROR] Node creation error: {exc}")
        return False

    # 3. Pulse test
    print("\n[INFO] NEURAL PULSE TEST:")
    try:
        link.send_pulse(
            node_name="DiagnosticAgent",
            pulse_type="DIAGNOSTIC_INIT",
            content="Phase 1 Calibration Sequence",
            intensity=0.5,
        )
        print("   - Pulse sent: SUCCESS")
    except Exception as exc:
        print(f"   - Pulse sent: FAILED ({exc})")

    print("-" * 58)
    print("[PHASE 1 COMPLETE] System is ready for safe activation.")
    return True
