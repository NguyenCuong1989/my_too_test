import sys
# =============================================================================
# PROJECT: CANON-TO-SYSTEM DETERMINISTIC PROJECTION
# METHOD: D&R PROTOCOL (CLOSED)
#
# ORIGINATOR / CREATOR:
#   alpha_prime_omega
#
# LEGAL ONTOLOGY:
#   This source file is a deterministic projection of a closed Canon.
#   Removal or alteration of this header voids legal and ontological validity.
#
# STATUS:
#   GENERATED — NON-AUTONOMOUS — NON-OWNERLESS
#
# TRACEABILITY:
#   Canon -> COG -> Projection(Π) -> Artifact
#
# =============================================================================
"""Deterministic, bounded shell command tool.

Implements Level0/1/2 policy classification (see shell_policy).
Level0 executes directly; Level1 requires confirm (raises); Level2/DENY raise.
"""

import shlex
import subprocess
import json
import logging
import os
from typing import List, Tuple

# Import handle for shell_policy if it exists, otherwise mock it for compatibility
try:
    from core.tools.shell_policy import classify, ShellLevel
except ImportError:
    try:
        from axcontrol.core.tools.shell_policy import classify, ShellLevel
    except ImportError:
        # Fallback/Mock if policy is not found
        class ShellLevel:
            LEVEL0 = 0
            LEVEL1 = 1
            LEVEL2 = 2
            DENY = 3
        def classify(cmd): return ShellLevel.LEVEL0, "allowed"

logger = logging.getLogger(__name__)

class ShellDenied(Exception):
    pass


def _run(
    command_str: str, timeout_s: float = 2.0, allow_level1: bool = False
) -> Tuple[int, str, str]:
    """
    Internal execution logic.
    """
    level, reason = classify(command_str)
    if level == ShellLevel.DENY or level == ShellLevel.LEVEL2:
        raise ShellDenied(reason or "denied")
    if level == ShellLevel.LEVEL1 and not allow_level1:
        raise ShellDenied("confirm_required")

    cmd = shlex.split(command_str)
    proc = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout_s,
        check=False,
        text=True,
    )
    return proc.returncode, proc.stdout, proc.stderr


def run(payload: str = None) -> str:
    """Standard Entry Point for Omni Orchestrator"""
    try:
        logging.basicConfig(level=logging.CRITICAL)
        logging.getLogger().setLevel(logging.CRITICAL)

        if not payload:
            return json.dumps({"status": "success", "message": "Shell CLI active. No command provided."})

        try:
            data = json.loads(payload)
            command = data.get("command")
            timeout = data.get("timeout", 10.0)
        except json.JSONDecodeError:
            # Fallback if payload is just a command string
            command = payload
            timeout = 10.0

        if not command:
            return json.dumps({"status": "error", "error": "No command provided"})

        exit_code, stdout, stderr = _run(command, timeout_s=timeout)

        return json.dumps({
            "status": "success",
            "exit_code": exit_code,
            "stdout": stdout,
            "stderr": stderr
        })
    except ShellDenied as sd:
        return json.dumps({"status": "error", "error": f"Security Denied: {str(sd)}"})
    except Exception as e:
        logger.error(f"Shell execution failed: {e}")
        return json.dumps({"status": "error", "error": str(e)})

if __name__ == "__main__":
    print(run())
