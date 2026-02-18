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

sys.path.append(str(Path(__file__).resolve().parents[2]))

from core.tools.chat_box import collect_intent
from core.tools import shell_cli
from core.tools.shell_policy import classify, ShellLevel
from core.loop.control_loop import ControlLoop
from core.decision.command import CommandEnvelope, CommandType
from core.decision.policy import PolicyVerdict, PolicyOutcome
from core.audit.log_schema import AuditRecord
from core.audit.logger import AuditLogger
from core.safety.determinism_hash import compute_determinism_hash


def _log_intent(logger: AuditLogger, intent_dict: dict):
    record = AuditRecord(
        timestamp=0,
        state_before={},
        intent=intent_dict,
        command={},
        policy_decision={},
        state_after={},
        determinism_hash="intent-log",
        stop_reason=None,
    )
    logger.append(record)


def run_chat():
    loop = ControlLoop()
    history: List[Dict[str, str]] = []
    pending_confirm = None
    print("Chat CLI ready. Commands: /cli <cmd>, /ax, /exit")
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
                    print(f"tool[cli] exit={rc}\n{out}{err}")
                except Exception as exc:
                    print(f"tool[cli] failed after confirm: {exc}")
                pending_confirm = None
                continue
            else:
                print("cancelled")
                pending_confirm = None
                continue
        if line == "/exit":
            break
        history.append({"role": "user", "content": line})

        if line.startswith("/cli "):
            cmd = line[len("/cli ") :].strip()
            level, reason = classify(cmd)
            if level == ShellLevel.LEVEL1:
                pending_confirm = cmd
                print(f"confirm? [y/N] {cmd}")
                continue
            try:
                rc, out, err = shell_cli.run(cmd)
                print(f"tool[cli] exit={rc}\n{out}{err}")
            except Exception as exc:
                print(f"tool[cli] denied: {exc}")
            continue

        if line == "/ax":
            stop = loop.run_once()
            print(f"ax step → stop={stop}")
            continue

        intent = collect_intent(history)
        _log_intent(loop.logger, intent.__dict__)
        print(f"intent→ {intent.goal} (source={intent.source.value})")


if __name__ == "__main__":
    run_chat()
