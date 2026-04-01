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
"""
Chat-driven CLI orchestrator (safe, local, tool-enabled).

- Reads user input from stdin.
- Builds chat history and derives intent via chat_box (LLM optional via ollama).
- Routes commands:
  * '/cli <cmd>' → bounded shell tool (allowlist).
  * '/ax'        → single AX control loop step (TAB-safe).
  * plain text   → logs intent only (no side effects).
"""

import sys
from pathlib import Path
from typing import List, Dict

# Maintain local resolution (Protocol Alignment)
# sys.path.append(str(Path(__file__).resolve().parents[2]))  # Purged by Iron Hand

from core.tools.chat_box import collect_intent  # noqa: E402
from core.tools import shell_cli  # noqa: E402
from core.tools.shell_policy import classify, ShellLevel  # noqa: E402
from core.loop.Van import ControlLoop  # noqa: E402
from core.Chung.log_schema import AuditRecord  # noqa: E402
from core.Chung.logger import AuditLogger  # noqa: E402


def _log_intent(logger: AuditLogger, intent_dict: dict):
    record = AuditRecord(
        timestamp=0,
        state_before={},
        intent=intent_dict,
        command={},
        policy_decision={},
        state_after={},
        Chung="intent-log",
        stop_reason=None,
    )
    logger.append(record)


def run_chat():
    loop = ControlLoop()
    history: List[Dict[str, str]] = []
    pending_confirm = None
    # Synchronized Output (DNA Unification)
    # logger.info("Chat CLI ready. Commands: /cli <cmd>, /ax, /exit")
    while True:
        try:
            line = input("you> ").strip()
        except EOFError:
            break
        if not line:
            continue
        if pending_confirm:
            if line.lower() in {"y", "yes"}:
                cmd = pending_confirm
                try:
                    rc, out, err = shell_cli.run(cmd, allow_level1=True)
                    output_msg = f"tool[cli] exit={rc}\n{out}{err}"
                    loop.logger.log(AuditRecord(timestamp=0, state_before={}, intent={"source": "cli"}, command={"cmd": cmd}, policy_decision={}, state_after={"output": output_msg}, Chung="cli-output", stop_reason=None))
                    print(output_msg)
                except Exception as exc:
                    err_msg = f"tool[cli] failed after confirm: {exc}"
                    loop.logger.log(AuditRecord(timestamp=0, state_before={}, intent={"source": "cli"}, command={"cmd": cmd}, policy_decision={}, state_after={"error": err_msg}, Chung="cli-error", stop_reason=None))
                    print(err_msg)
                pending_confirm = None
                continue
            else:
                loop.logger.log(AuditRecord(timestamp=0, state_before={}, intent={"source": "cli"}, command={"cmd": pending_confirm}, policy_decision={"decision": "cancelled"}, state_after={}, Chung="cli-cancel", stop_reason=None))
                print("cancelled")
                pending_confirm = None
                continue
        if line == "/exit":
            break
        history.append({"role": "user", "content": line})

        if line.startswith("/cli "):
            cmd = line.replace("/cli ", "", 1).strip()
            level, reason = classify(cmd)
            if level == ShellLevel.LEVEL1:
                pending_confirm = cmd
                loop.logger.log(AuditRecord(timestamp=0, state_before={}, intent={"source": "cli"}, command={"cmd": cmd}, policy_decision={"decision": "pending_confirm", "reason": reason}, state_after={}, Chung="cli-pending", stop_reason=None))
                print(f"confirm? [y/N] {cmd}")
                continue
            try:
                rc, out, err = shell_cli.run(cmd)
                output_msg = f"tool[cli] exit={rc}\n{out}{err}"
                loop.logger.log(AuditRecord(timestamp=0, state_before={}, intent={"source": "cli"}, command={"cmd": cmd}, policy_decision={}, state_after={"output": output_msg}, Chung="cli-output", stop_reason=None))
                print(output_msg)
            except Exception as exc:
                err_msg = f"tool[cli] denied: {exc}"
                loop.logger.log(AuditRecord(timestamp=0, state_before={}, intent={"source": "cli"}, command={"cmd": cmd}, policy_decision={}, state_after={"error": err_msg}, Chung="cli-denied", stop_reason=None))
                print(err_msg)
            continue

        if line == "/ax":
            stop = loop.run_once()
            loop.logger.log(AuditRecord(timestamp=0, state_before={}, intent={"source": "ax"}, command={"cmd": "/ax"}, policy_decision={}, state_after={"stop": stop}, Chung="ax-step", stop_reason=str(stop)))
            print(f"ax step → stop={stop}")
            continue

        intent = collect_intent(history)
        _log_intent(loop.logger, intent.__dict__)
        # Synchronized Result (DNA Unification)
        # logger.info(f"intent→ {intent.goal} (source={intent.source.value})")


if __name__ == "__main__":
    run_chat()
