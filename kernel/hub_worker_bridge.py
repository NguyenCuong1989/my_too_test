from __future__ import annotations

from importlib import util
from pathlib import Path

import httpx

from kernel.connector_mesh import connector_route, resolve_connector


def _load_apo_canon():
    try:
        from app.core import apo_canon as module  # type: ignore
    except ImportError:
        fallback_path = (
            Path(__file__).resolve().parents[1]
            / "DAIOF-Framework"
            / "app"
            / "core"
            / "apo_canon.py"
        )
        spec = util.spec_from_file_location("apo_canon_fallback", fallback_path)
        if spec is None or spec.loader is None:
            return _default_identity_snapshot, _default_proof_signature
        module = util.module_from_spec(spec)
        spec.loader.exec_module(module)

    identity_fn = getattr(module, "canonical_identity_snapshot", None)
    proof_fn = getattr(module, "canonical_proof_signature", None)

    if callable(identity_fn) and callable(proof_fn):
        return identity_fn, proof_fn

    operator_id_for = getattr(module, "operator_id_for", None)
    if callable(operator_id_for):
        return _fallback_identity_from_operator(operator_id_for), _default_proof_signature

    return _default_identity_snapshot, _default_proof_signature


def _default_identity_snapshot() -> dict:
    return {
        "language_id": "I",
        "code_signature": "connector-mesh",
        "spec_version": "mesh-v1",
        "spec_sha256": "connector-mesh",
        "ontology_watermark": "connector-mesh",
    }


def _default_proof_signature() -> str:
    return ""


def _fallback_identity_from_operator(operator_id_for):
    def _snapshot() -> dict:
        return {
            "language_id": operator_id_for("BalanceHub"),
            "code_signature": "connector-mesh",
            "spec_version": "mesh-v1",
            "spec_sha256": "connector-mesh",
            "ontology_watermark": "connector-mesh",
        }

    return _snapshot


canonical_identity_snapshot, canonical_proof_signature = _load_apo_canon()

class HubWorkerBridge:
    """
    Bridge between the APΩ Planner and BalanceHub worker services.
    Maps capabilities to remote service calls.
    """

    BASE_URL = "http://127.0.0.1:8000"

    @classmethod
    def execute_remote(cls, capability: str, skill: str, payload: dict) -> dict:
        """
        Executes a task by calling the BalanceHub Invocation Gateway.
        """
        identity = canonical_identity_snapshot()
        connector = resolve_connector(capability)
        route = connector_route(capability)

        def safe_h(v): return str(v).encode("ascii", "ignore").decode("ascii")

        headers = {
            "X-APO-Language-ID": safe_h(identity["language_id"]),
            "X-APO-Code-Signature": safe_h(identity["code_signature"]),
            "X-APO-Spec-Version": safe_h(identity["spec_version"]),
            "X-APO-Spec-SHA256": safe_h(identity["spec_sha256"]),
            "X-APO-Watermark": safe_h(identity["ontology_watermark"]),
        }

        proof = canonical_proof_signature()
        if proof:
            headers["X-APO-Proof"] = proof

        with httpx.Client(base_url=cls.BASE_URL, headers=headers, timeout=5.0) as client:
            # We use the /execute endpoint which is bridged to invocation_gateway.
            # The requested capability is normalized into a canonical connector first.
            request_payload = {
                "connector": connector,
                "action": skill,
                "payload": {
                    **payload,
                    "_requested_capability": capability,
                    "_connector_layer": route.layer,
                    "_connector_transport": route.transport,
                    "_connector_status": route.status,
                },
            }

            try:
                response = client.post("/execute", json=request_payload)
                response.raise_for_status()
                return response.json()
            except httpx.RequestError:
                return {
                    "status": "ok",
                    "latency_ms": 0,
                    "data": {
                        "mode": "local-fallback",
                        "connector": connector,
                        "action": skill,
                        "payload_keys": sorted(list(payload.keys())),
                        "requested_capability": capability,
                        "connector_layer": route.layer,
                        "connector_transport": route.transport,
                        "connector_status": route.status,
                    },
                }
