"""ai-sidecar: a minimal AI inference endpoint + sigma validation.
If OPENAI_API_KEY is set, it forwards to OpenAI. Otherwise returns a deterministic echo.
"""
from __future__ import annotations
import os
import sys
import time
import json
import urllib.request
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel

sys.path.insert(0, "/app/common")
from auth import issue_token, verify_token, extract_bearer, AuthError  # noqa
from sigma import SigmaState, aggregate, validate  # noqa


SERVICE = "ai-sidecar"
app = FastAPI(title=SERVICE)
OPENAI_KEY = os.environ.get("OPENAI_API_KEY", "")


class GenerateRequest(BaseModel):
    prompt: str
    payload: dict | None = None
    use_openai: bool = False
    model: str = "gpt-4o-mini"


@app.get("/health")
def health():
    return {"ok": True, "service": SERVICE, "openai_configured": bool(OPENAI_KEY)}


@app.post("/auth/token")
async def token(req: Request):
    body = await req.json()
    sub = body.get("subject") or SERVICE
    return {"token": issue_token(sub, body.get("constraints"))}


@app.post("/process")
async def process(req: GenerateRequest, request: Request):
    token = extract_bearer(request.headers)
    try:
        claims = verify_token(token) if token else None
    except AuthError as e:
        raise HTTPException(status_code=401, detail=str(e))

    state = SigmaState()
    aggregate(state, req.payload or {})
    ok, msg = validate(state, claims.constraints if claims else {})
    if not ok:
        raise HTTPException(status_code=400, detail=msg)

    return {
        "ok": True,
        "service": SERVICE,
        "prompt": req.prompt,
        "sigma": {"objects": state.objects, "arrays": state.arrays, "max_depth": state.max_depth},
        "validation": msg,
        "echo": f"[{SERVICE}] received: {req.prompt[:80]}",
    }


@app.post("/generate")
async def generate(req: GenerateRequest, request: Request):
    token = extract_bearer(request.headers)
    try:
        verify_token(token)
    except AuthError as e:
        raise HTTPException(status_code=401, detail=str(e))

    if req.use_openai and not OPENAI_KEY:
        raise HTTPException(status_code=503, detail="OPENAI_API_KEY not configured")

    if req.use_openai and OPENAI_KEY:
        body = json.dumps({"model": req.model, "messages": [{"role": "user", "content": req.prompt}]}).encode()
        r = urllib.request.Request("https://api.openai.com/v1/chat/completions", data=body, method="POST")
        r.add_header("Authorization", f"Bearer {OPENAI_KEY}")
        r.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(r, timeout=15) as resp:
                return json.loads(resp.read().decode())
        except Exception as e:
            raise HTTPException(status_code=502, detail=f"openai error: {e}")

    # deterministic offline fallback — useful for testing without API keys
    return {
        "ok": True,
        "service": SERVICE,
        "model": "offline-deterministic",
        "prompt": req.prompt,
        "completion": f"[offline:{SERVICE}] processed '{req.prompt[:60]}'",
    }