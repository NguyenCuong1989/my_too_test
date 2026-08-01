"""
Minimal HTTP client for service-to-service calls.
Uses container DNS directly. No retries, no circuit breakers — KISS.
Auth token is issued once and reused.
"""
from __future__ import annotations
import os
import json
import urllib.request
import urllib.error
from auth import issue_token


SERVICE_REGISTRY = {
    # service_name -> (host, port)
    "mcp-router":    (os.environ.get("MCP_HOST", "mcp-router"),    int(os.environ.get("MCP_PORT", "3000"))),
    "factory-worker":(os.environ.get("FACTORY_HOST", "factory-worker"), int(os.environ.get("FACTORY_PORT", "8082"))),
    "ai-sidecar":    (os.environ.get("AI_HOST", "ai-sidecar"),    int(os.environ.get("AI_PORT", "8100"))),
    "firebase-emu":  (os.environ.get("FIREBASE_HOST", "firebase-emulator"), int(os.environ.get("FIREBASE_PORT", "4400"))),
    # Optional external services — only listed if reachable
    "balancehub-api": (os.environ.get("BALANCEHUB_HOST", "balancehub-api"), int(os.environ.get("BALANCEHUB_PORT", "8000"))),
}


class Connector:
    def __init__(self, service_name: str):
        self.service_name = service_name
        self.token = issue_token(service_name)

    def call(self, target: str, method: str, path: str, body: dict | None = None, timeout: float = 5.0):
        if target not in SERVICE_REGISTRY:
            raise ValueError(f"unknown target: {target}")
        host, port = SERVICE_REGISTRY[target]
        url = f"http://{host}:{port}{path}"
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header("Authorization", f"Bearer {self.token}")
        req.add_header("Content-Type", "application/json")
        req.add_header("X-Source-Service", self.service_name)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return {"status": resp.status, "body": json.loads(resp.read().decode() or "{}")}
        except urllib.error.HTTPError as e:
            raw = e.read().decode() if e.fp else ""
            try:
                parsed = json.loads(raw)
            except Exception:
                parsed = {"raw": raw}
            return {"status": e.code, "body": parsed, "error": str(e)}
        except Exception as e:
            return {"status": 0, "body": {}, "error": f"{type(e).__name__}: {e}"}

    def health(self, target: str):
        return self.call(target, "GET", "/health")