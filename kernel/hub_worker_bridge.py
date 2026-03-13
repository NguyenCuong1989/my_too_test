import httpx
from app.core.apo_canon import canonical_identity_snapshot, canonical_proof_signature

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
        # Map capability to specific BalanceHub endpoints if needed,
        # but the standard way is via the Invocation Gateway.

        identity = canonical_identity_snapshot()

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

        with httpx.Client(base_url=cls.BASE_URL, headers=headers, timeout=30.0) as client:
            # We use the /execute endpoint which is bridged to invocation_gateway
            response = client.post(
                "/execute",
                json={
                    "connector": capability.capitalize(), # e.g. "Github"
                    "action": skill,
                    "payload": payload
                }
            )
            response.raise_for_status()
            return response.json()
