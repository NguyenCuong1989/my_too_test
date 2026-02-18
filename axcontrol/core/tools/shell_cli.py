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
from typing import List, Tuple

from core.tools.shell_policy import classify, ShellLevel


class ShellDenied(Exception):
    pass


def run(command_str: str, timeout_s: float = 2.0, allow_level1: bool = False) -> Tuple[int, str, str]:
    """
    Execute an allowlisted command; return (exit_code, stdout, stderr).
    Raises ShellDenied if validation fails or confirmation required.
    """
    level, reason = classify(command_str)
    if level == ShellLevel.DENY or level == ShellLevel.LEVEL2:
        raise ShellDenied(reason or "denied")
    if level == ShellLevel.LEVEL1 and not allow_level1:
        raise ShellDenied("confirm_required")

    cmd = shlex.split(command_str)
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout_s, check=False, text=True)
    return proc.returncode, proc.stdout, proc.stderr
