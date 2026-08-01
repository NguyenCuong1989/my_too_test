"""
Simple shared JWT auth for sigma-cos services.
No over-engineering. Just HS256 with a shared secret.
Constraints baked into the token (max_objects, max_depth) so services
don't need to re-validate against a central authority.
"""
from __future__ import annotations
import os
import time
import hmac
import hashlib
import base64
import json
from dataclasses import dataclass


SECRET = os.environ.get("SIGMA_SECRET", "dev-secret-change-me")
DEFAULT_TTL = 24 * 3600


def _b64url(b: bytes) -> str:
    return base64.urlsafe_b64encode(b).rstrip(b"=").decode()


def _b64url_decode(s: str) -> bytes:
    s = s + "=" * (-len(s) % 4)
    return base64.urlsafe_b64decode(s)


def issue_token(subject: str, constraints: dict | None = None, ttl: int = DEFAULT_TTL) -> str:
    """Mint a token. constraints are embedded (max_objects, max_arrays, max_depth)."""
    header = {"alg": "HS256", "typ": "JWT"}
    payload = {
        "sub": subject,
        "constraints": constraints or {"max_objects": 100, "max_arrays": 50, "max_depth": 10},
        "iat": int(time.time()),
        "exp": int(time.time()) + ttl,
    }
    h = _b64url(json.dumps(header, separators=(",", ":")).encode())
    p = _b64url(json.dumps(payload, separators=(",", ":")).encode())
    msg = f"{h}.{p}".encode()
    sig = hmac.new(SECRET.encode(), msg, hashlib.sha256).digest()
    return f"{h}.{p}.{_b64url(sig)}"


@dataclass
class VerifiedToken:
    subject: str
    constraints: dict
    exp: int


class AuthError(Exception):
    pass


def verify_token(token: str) -> VerifiedToken:
    if not token or token.count(".") != 2:
        raise AuthError("malformed token")
    h, p, s = token.split(".")
    msg = f"{h}.{p}".encode()
    expected = _b64url(hmac.new(SECRET.encode(), msg, hashlib.sha256).digest())
    if not hmac.compare_digest(expected, s):
        raise AuthError("bad signature")
    payload = json.loads(_b64url_decode(p))
    if int(time.time()) >= payload["exp"]:
        raise AuthError("expired")
    return VerifiedToken(subject=payload["sub"], constraints=payload.get("constraints", {}), exp=payload["exp"])


def extract_bearer(headers: dict) -> str | None:
    auth = headers.get("authorization") or headers.get("Authorization")
    if not auth:
        return None
    if auth.lower().startswith("bearer "):
        return auth.split(None, 1)[1].strip()
    return None