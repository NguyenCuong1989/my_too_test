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
"""Minimal HTTP snapshot bridge (R-22).

- Endpoint: POST /chat
- Request JSON: {"text": str, "meta": {"confirm": bool}}
- Response JSON: Snapshot (see ui/CONTRACT.md)

No external deps beyond stdlib.
"""

import json
import os
import sys
import time
import typing
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Optional

# Maintain local resolution (Protocol Alignment)
# sys.path has been purged of parent injection hacks to enforce strict -m execution.

from core.loop.Van import ControlLoop  # noqa: E402
from core.tools import shell_cli  # noqa: E402
from core.tools.shell_policy import classify, ShellLevel  # noqa: E402
from core.Menh.Chung import compute_Chung  # noqa: E402
from core.Menh.stop_reasons import StopReason  # noqa: E402
from core.Chung.log_schema import AuditRecord  # noqa: E402
from core.Chung.logger import AuditLogger  # noqa: E402


class _NDJSONAuditSink:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, record: AuditRecord) -> None:
        payload = {
            "ts": record.timestamp,
            "type": "bridge_audit",
            "state_before": record.state_before,
            "intent": record.intent,
            "command": record.command,
            "policy_decision": record.policy_decision,
            "state_after": record.state_after,
            "Chung": record.Chung,
            "stop_reason": record.stop_reason,
            "hex_bits": record.hex_bits,
        }
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(payload, ensure_ascii=False) + "\n")
            fh.flush()


class Bridge:
    def __init__(self):
        self.loop = ControlLoop()
        self.pending_cmd: Optional[str] = None
        audit_path = Path(os.getenv("AXCONTROL_AUDIT_LOG", "logs/observe.ndjson"))
        self.logger = AuditLogger(sink=_NDJSONAuditSink(audit_path))
        self._history: typing.List[dict] = []
        self.step_count = 0

    def process(self, text: str, confirm: Optional[bool]) -> dict:
        # init snapshot fields
        system = {
            "mode": "IDLE",
            "simulation": os.getenv("AXCONTROL_SIM", "0") == "1",
            "ax_enabled": os.getenv("AXCONTROL_SIM", "0") != "1",
            "shell_enabled": True,
        }
        input_block = {
            "raw": text or None,
            "type": "NONE",
        }
        intent_block = {"kind": "NONE", "value": None, "source": "NONE"}
        decision = {"verdict": "IDLE", "command": None}
        execution = {"executed": False, "executor": "NONE", "result": None}
        stop_block = {"reason": "NONE", "message": None}
        ui_block = {
            "requires_confirm": False,
            "prompt": None,
            "suggestions": ["/ax", "status?"],
        }

        # Deterministic Stable Tick (Iron Hand)
        self.step_count += 1
        now = f"step-{self.step_count:06d}"


        # confirm flow
        if self.pending_cmd is not None:
            if confirm:
                try:
                    rc, out, err = shell_cli.run(self.pending_cmd, allow_level1=True)
                    decision = {"verdict": "ALLOW", "command": self.pending_cmd}
                    execution = {
                        "executed": True,
                        "executor": "SHELL",
                        "result": f"exit={rc}\n{out}{err}",
                    }
                    system["mode"] = "EXECUTING"
                except Exception as exc:
                    decision = {"verdict": "STOP", "command": self.pending_cmd}
                    stop_block = {"reason": "SHELL_ERROR", "message": str(exc)}
            else:
                decision = {"verdict": "STOP", "command": self.pending_cmd}
                stop_block = {"reason": "USER_CANCEL", "message": "user rejected"}

            self.pending_cmd = None
            ui_block["suggestions"] = ["/ax", "status?"]
            snapshot = self._build_snapshot(
                system,
                input_block,
                intent_block,
                decision,
                execution,
                stop_block,
                ui_block,
                now,
            )
            self._history.append(snapshot)
            return snapshot

        if not text:
            return self._build_snapshot(
                system,
                input_block,
                intent_block,
                decision,
                execution,
                stop_block,
                ui_block,
                now,
            )

        # parse commands
        if text.startswith("/cli "):
            cmd = text.split("/cli ", 1)[-1].strip()
            input_block["type"] = "CLI"
            level, reason = classify(cmd)
            intent_block = {"kind": "CLI", "value": cmd, "source": "RULE"}
            if level == ShellLevel.LEVEL2 or level == ShellLevel.DENY:
                decision = {"verdict": "STOP", "command": cmd}
                stop_block = {"reason": reason or "SHELL_DENY_LV2", "message": None}
                ui_block["suggestions"] = ["status?", "/ax"]
            elif level == ShellLevel.LEVEL1:
                decision = {"verdict": "CONFIRM_REQ", "command": cmd}
                ui_block = {
                    "requires_confirm": True,
                    "prompt": f"Run command: {cmd}?",
                    "suggestions": ["confirm", "cancel"],
                }
                self.pending_cmd = cmd
            else:
                try:
                    rc, out, err = shell_cli.run(cmd)
                    decision = {"verdict": "ALLOW", "command": cmd}
                    execution = {
                        "executed": True,
                        "executor": "SHELL",
                        "result": f"exit={rc}\n{out}{err}",
                    }
                    system["mode"] = "EXECUTING"
                except Exception as exc:
                    decision = {"verdict": "STOP", "command": cmd}
                    stop_block = {"reason": "SHELL_ERROR", "message": str(exc)}
            return self._build_snapshot(
                system,
                input_block,
                intent_block,
                decision,
                execution,
                stop_block,
                ui_block,
                now,
            )

        if text == "/ax":
            input_block["type"] = "AX"
            intent_block = {"kind": "AX", "value": "NEXT_TAB", "source": "RULE"}
            if not system["ax_enabled"]:
                decision = {"verdict": "STOP", "command": "AX_TAB"}
                stop_block = {
                    "reason": (
                        StopReason.KILL_SWITCH.value
                        if not system["ax_enabled"]
                        else "AX_DISABLED"
                    ),
                    "message": None,
                }
            else:
                stop = self.loop.run_once()
                decision = {
                    "verdict": "ALLOW" if stop is None else "STOP",
                    "command": "AX_TAB",
                }
                execution = {
                    "executed": stop is None,
                    "executor": "AX" if stop is None else "NONE",
                    "result": None,
                }
                if stop is not None:
                    stop_block = {"reason": stop.value, "message": None}
                system["mode"] = "EXECUTING"
            return self._build_snapshot(
                system,
                input_block,
                intent_block,
                decision,
                execution,
                stop_block,
                ui_block,
                now,
            )

        # free text
        input_block["type"] = "FREE_TEXT"
        text_clean = text.strip()
        is_query = text_clean.endswith("?")
        intent_kind = "QUERY" if is_query else "FREE_TEXT_ACTION"
        allowed_kinds = {"QUERY"}

        if intent_kind not in allowed_kinds:
            intent_block = {"kind": intent_kind, "value": None, "source": "human"}
            decision = {"verdict": "STOP", "command": None}
            stop_block = {
                "reason": StopReason.LEXICON_VIOLATION.value,
                "message": "free text not in lexicon",
            }
            ui_block["suggestions"] = ["status?", "/ax"]
            return self._build_snapshot(
                system,
                input_block,
                intent_block,
                decision,
                execution,
                stop_block,
                ui_block,
                now,
            )

        intent_block = {"kind": intent_kind, "value": text_clean, "source": "human"}
        decision = {"verdict": "ALLOW", "command": None}
        execution = {"executed": False, "executor": "NONE", "result": "intent logged"}
        return self._build_snapshot(
            system,
            input_block,
            intent_block,
            decision,
            execution,
            stop_block,
            ui_block,
            now,
        )

    def _build_snapshot(
        self,
        system,
        input_block,
        intent_block,
        decision,
        execution,
        stop_block,
        ui_block,
        timestamp,
    ):
        Chung = compute_Chung(
            system,
            intent_block,
            decision,
            execution,
        )
        recorded = True
        audit_error = None
        try:
            self.logger.append(
                AuditRecord(
                    timestamp=timestamp,  # Stable Sequence Identity
                    state_before=system,
                    intent=intent_block,
                    command=decision,
                    policy_decision={"verdict": decision.get("verdict")},
                    state_after={"execution": execution, "stop": stop_block},
                    Chung=Chung,
                    stop_reason=(
                        None
                        if stop_block.get("reason") == "NONE"
                        else stop_block.get("reason")
                    ),
                    hex_bits=None,
                )
            )
        except Exception as exc:
            recorded = False
            audit_error = str(exc)
            stop_block = {
                "reason": StopReason.AUDIT_WRITE_FAILED.value,
                "message": audit_error,
            }

        audit = {
            "timestamp": timestamp,
            "Chung": Chung,
            "recorded": recorded,
        }
        if audit_error:
            audit["error"] = audit_error
        return {
            "system": system,
            "input": input_block,
            "intent": intent_block,
            "decision": decision,
            "execution": execution,
            "stop": stop_block,
            "audit": audit,
            "ui": ui_block,
        }


bridge = Bridge()


class Handler(BaseHTTPRequestHandler):
    def _json(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if self.path != "/chat":
            self._json(404, {"error": "not found"})
            return
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length) if length else b""
        try:
            payload = json.loads(raw or b"{}")
        except Exception:
            self._json(400, {"error": "invalid json"})
            return
        text = payload.get("text") or ""
        confirm = None
        meta = payload.get("meta") or {}
        if "confirm" in meta:
            confirm = bool(meta.get("confirm"))
        snapshot = bridge.process(text, confirm)
        self._json(200, snapshot)

    def log_message(self, format: str, *args: typing.Any) -> None:
        return  # silence


def main():
    port = int(os.getenv("AXCONTROL_HTTP_PORT", "5140"))
    server = HTTPServer(("127.0.0.1", port), Handler)
    print(f"AXCONTROL bridge running on http://127.0.0.1:{port}/chat")
    server.serve_forever()


if __name__ == "__main__":
    main()
