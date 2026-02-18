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
"""Shell command policy classifier (Level 0/1/2).

Level0: read-only, auto-allow.
Level1: local write, require confirm.
Level2: dangerous, hard deny.
"""

import shlex
from typing import Tuple


LEVEL0 = {
    "pwd": [],
    "ls": ["-l", "-a"],
    "whoami": [],
    "git": ["status"],
    "cat": [],
    "head": ["-n"],
    "tail": ["-n"],
}

LEVEL1 = {
    "mkdir": [],
    "touch": [],
    "echo": [],
    "git": ["commit"],
}

LEVEL2 = {"rm", "sudo", "chmod", "kill", "curl", "wget"}


class ShellLevel:
    LEVEL0 = "LEVEL0"
    LEVEL1 = "LEVEL1"
    LEVEL2 = "LEVEL2"
    DENY = "DENY"


def classify(command_str: str) -> Tuple[str, str | None]:
    """Return (level, reason_if_deny)."""
    try:
        cmd = shlex.split(command_str)
    except ValueError:
        return ShellLevel.DENY, "PARSE_ERROR"
    if not cmd:
        return ShellLevel.DENY, "EMPTY_COMMAND"

    name, *args = cmd
    if name in LEVEL2:
        return ShellLevel.LEVEL2, "SHELL_DENY_LV2"

    # git subcommands
    if name == "git" and args:
        sub = args[0]
        if sub == "status" and _flags_ok(args[1:], LEVEL0["git"]):
            return ShellLevel.LEVEL0, None
        if sub == "commit":
            return ShellLevel.LEVEL1, None
        return ShellLevel.DENY, "GIT_SUBCOMMAND_DENY"

    if name in LEVEL0:
        if _flags_ok(args, LEVEL0[name]):
            return ShellLevel.LEVEL0, None
        return ShellLevel.DENY, "FLAG_DENY"

    if name in LEVEL1:
        return ShellLevel.LEVEL1, None

    return ShellLevel.DENY, "NOT_ALLOWLISTED"


def _flags_ok(args, allowed_flags) -> bool:
    allowed = set(allowed_flags)
    for a in args:
        if a.startswith("-") and a not in allowed:
            return False
    return True
