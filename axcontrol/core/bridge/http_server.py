"""Minimal HTTP snapshot bridge (R-22).

- Endpoint: POST /chat
- Request JSON: {"text": str, "meta": {"confirm": bool}}
- Response JSON: Snapshot (see ui/CONTRACT.md)

No external deps beyond stdlib.
"""
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime
from pathlib import Path
from typing import Optional

sys.path.append(str(Path(__file__).resolve().parents[2]))

from core.loop.Van import ControlLoop
from core.tools import shell_cli
from core.tools.shell_policy import classify, ShellLevel
from core.tools.chat_box import collect_intent
from core.Chinh.command import CommandType
from core.Menh.Chung import compute_Chung
from core.Menh.stop_reasons import StopReason


class Bridge:
    def __init__(self):
        self.loop = ControlLoop()
        self.pending_cmd: Optional[str] = None

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
        execution = {"executed": False, "AnLenh": "NONE", "result": None}
        stop_block = {"reason": "NONE", "message": None}
        ui_block = {"requires_confirm": False, "prompt": None}

        now = datetime.utcnow().isoformat() + "Z"

        # confirm flow
        if self.pending_cmd is not None:
            if confirm:
                try:
                    rc, out, err = shell_cli.run(self.pending_cmd, allow_level1=True)
                    decision = {"verdict": "ALLOW", "command": self.pending_cmd}
                    execution = {"executed": True, "AnLenh": "SHELL", "result": f"exit={rc}\n{out}{err}"}
                    system["mode"] = "EXECUTING"
                except Exception as exc:
                    decision = {"verdict": "STOP", "command": self.pending_cmd}
                    stop_block = {"reason": "SHELL_ERROR", "message": str(exc)}
            else:
                decision = {"verdict": "STOP", "command": self.pending_cmd}
                stop_block = {"reason": "USER_CANCEL", "message": "user rejected"}
            self.pending_cmd = None
            snapshot = self._build_snapshot(system, input_block, intent_block, decision, execution, stop_block, ui_block, now)
            return snapshot

        if not text:
            return self._build_snapshot(system, input_block, intent_block, decision, execution, stop_block, ui_block, now)

        # parse commands
        if text.startswith("/cli "):
            cmd = text[len("/cli ") :].strip()
            input_block["type"] = "CLI"
            level, reason = classify(cmd)
            intent_block = {"kind": "CLI", "value": cmd, "source": "RULE"}
            if level == ShellLevel.LEVEL2 or level == ShellLevel.DENY:
                decision = {"verdict": "STOP", "command": cmd}
                stop_block = {"reason": reason or "SHELL_DENY_LV2", "message": None}
            elif level == ShellLevel.LEVEL1:
                decision = {"verdict": "CONFIRM_REQ", "command": cmd}
                ui_block = {"requires_confirm": True, "prompt": f"Run command: {cmd}?"}
                self.pending_cmd = cmd
            else:
                try:
                    rc, out, err = shell_cli.run(cmd)
                    decision = {"verdict": "ALLOW", "command": cmd}
                    execution = {"executed": True, "AnLenh": "SHELL", "result": f"exit={rc}\n{out}{err}"}
                    system["mode"] = "EXECUTING"
                except Exception as exc:
                    decision = {"verdict": "STOP", "command": cmd}
                    stop_block = {"reason": "SHELL_ERROR", "message": str(exc)}
            return self._build_snapshot(system, input_block, intent_block, decision, execution, stop_block, ui_block, now)

        if text == "/ax":
            input_block["type"] = "AX"
            intent_block = {"kind": "AX", "value": "NEXT_TAB", "source": "RULE"}
            if not system["ax_enabled"]:
                decision = {"verdict": "STOP", "command": "AX_TAB"}
                stop_block = {"reason": StopReason.KILL_SWITCH.value if not system["ax_enabled"] else "AX_DISABLED", "message": None}
            else:
                stop = self.loop.run_once()
                decision = {"verdict": "ALLOW" if stop is None else "STOP", "command": "AX_TAB"}
                execution = {"executed": stop is None, "AnLenh": "AX" if stop is None else "NONE", "result": None}
                if stop is not None:
                    stop_block = {"reason": stop.value, "message": None}
                system["mode"] = "EXECUTING"
            return self._build_snapshot(system, input_block, intent_block, decision, execution, stop_block, ui_block, now)

        # free text
        input_block["type"] = "FREE_TEXT"
        intent = collect_intent([{"role": "user", "content": text}])
        intent_block = {"kind": intent.goal or "QUERY", "value": intent.parameters.get("action") if intent.parameters else intent.goal, "source": intent.source.value}
        decision = {"verdict": "ALLOW", "command": None}
        execution = {"executed": False, "AnLenh": "NONE", "result": "intent logged"}
        return self._build_snapshot(system, input_block, intent_block, decision, execution, stop_block, ui_block, now)

    def _build_snapshot(self, system, input_block, intent_block, decision, execution, stop_block, ui_block, timestamp):
        audit = {
            "timestamp": timestamp,
            "Chung": compute_Chung(
                system,
                intent_block,
                decision,
                execution,
            ),
            "recorded": True,
        }
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

    def log_message(self, fmt, *args):
        return  # silence


def main():
    port = int(os.getenv("AXCONTROL_HTTP_PORT", "5140"))
    server = HTTPServer(("127.0.0.1", port), Handler)
    print(f"AXCONTROL bridge running on http://127.0.0.1:{port}/chat")
    server.serve_forever()


if __name__ == "__main__":
    main()
