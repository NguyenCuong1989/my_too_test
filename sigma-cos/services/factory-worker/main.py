"""factory-worker: takes tasks, dispatches to ai-sidecar or runs local logic."""
from __future__ import annotations
import os
import sys
import time
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel

# Add /app/common to path so we share the same auth/sigma/connector modules
sys.path.insert(0, "/app/common")
from auth import issue_token, verify_token, extract_bearer, AuthError  # noqa
from sigma import SigmaState, aggregate, validate  # noqa
from connector import Connector  # noqa


SERVICE = "factory-worker"
app = FastAPI(title=SERVICE)
connector = Connector(SERVICE)


class Task(BaseModel):
    task: str
    payload: dict | None = None
    forward_to: str | None = None  # optional: forward to ai-sidecar / another service


@app.get("/health")
def health():
    return {"ok": True, "service": SERVICE, "time": time.time()}


@app.post("/auth/token")
def token(req: Request):
    body = req.json() if hasattr(req, "json") else {}
    sub = body.get("subject") or SERVICE
    return {"token": issue_token(sub, body.get("constraints"))}


@app.post("/process")
async def process(task: Task, request: Request):
    token = extract_bearer(request.headers)
    try:
        claims = verify_token(token) if token else None
    except AuthError as e:
        raise HTTPException(status_code=401, detail=str(e))

    state = SigmaState()
    aggregate(state, task.payload or {})
    ok, msg = validate(state, claims.constraints if claims else {})
    if not ok:
        raise HTTPException(status_code=400, detail=msg)

    # optional forward
    forward_result = None
    if task.forward_to and task.forward_to in ("ai-sidecar", "mcp-router", "factory-worker"):
        # ai-sidecar's /process expects {prompt, payload}; translate
        target_body = {"task": task.task, "payload": task.payload}
        target_path = "/process"
        if task.forward_to == "ai-sidecar":
            target_body = {"prompt": task.task, "payload": task.payload}
        forward_result = connector.call(task.forward_to, "POST", target_path, target_body)

    return {
        "ok": True,
        "service": SERVICE,
        "task": task.task,
        "sigma": {"objects": state.objects, "arrays": state.arrays, "max_depth": state.max_depth, "keys": sorted(state.keys)},
        "validation": msg,
        "forwarded_to": task.forward_to,
        "forward_result": forward_result,
    }


@app.post("/relay")
async def relay(req: Request):
    """Forward arbitrary call to any registered service."""
    token = extract_bearer(req.headers)
    try:
        verify_token(token)
    except AuthError as e:
        raise HTTPException(status_code=401, detail=str(e))
    body = await req.json()
    target = body.pop("target", None)
    if not target:
        raise HTTPException(status_code=400, detail="target required")
    return connector.call(target, body.get("method", "POST"), body.get("path", "/"), body.get("data"))