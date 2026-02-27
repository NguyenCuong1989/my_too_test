import json
import hashlib
from datetime import datetime

VERSION = "1.0.1"
SCHEMA_VERSION = "1.0.0"
COMMIT_HASH = "533ac0f242b91dd29cae4fe36e6ad7d20bee0017" # Pinning to current git state

def run(content):
    """
    SLI Enrichment Skill (Value Engine)
    Standard skill signature for the Factory Worker.

    Expected input (JSON string):
    {
      "company_name": string,
      "domain": string (optional),
      "industry": string (optional),
      "geo": string (optional)
    }
    """
    try:
        # 1. Parse Input
        if isinstance(content, str):
            params = json.loads(content)
        else:
            params = content

        company_name = params.get("company_name", "Unknown")
        domain = params.get("domain", company_name.lower().replace(" ", "") + ".com")

        # 2. Intelligence Gathering (Mock Data for MVP)
        # In production, this would call Apollo.io, Hunter.io, or Gemini 2.0 Search
        mock_leads = [
            {
                "name": "Alex Rivlin",
                "title": "Chief Technology Officer",
                "email": f"alex@{domain}",
                "confidence": 0.92
            },
            {
                "name": "Sarah Chen",
                "title": "Head of Engineering",
                "email": f"sarah.c@{domain}",
                "confidence": 0.85
            }
        ]

        # 3. Data Normalization
        data = {
            "company": company_name,
            "domain": domain,
            "industry": params.get("industry", "Technology/AI"),
            "geo": params.get("geo", "Global"),
            "contacts": mock_leads,
            "intelligence": {
                "source_score": 0.88,
                "verified_at": datetime.utcnow().isoformat() + "Z",
                "signals": ["High growth", "Recent funding", "AI-first"]
            }
        }

        # 4. Deterministic Hash Sealing (RIL Compliance)
        # We seal core data + schema version + code commit to ensure absolute integrity.
        # This prevents drift across code versions or schema changes.
        content_to_seal = {
            "company": data["company"],
            "domain": data["domain"],
            "contacts": data["contacts"],
            "schema_version": SCHEMA_VERSION,
            "commit_hash": COMMIT_HASH
        }

        raw_to_seal = json.dumps(content_to_seal, sort_keys=True)
        seal = hashlib.sha256(raw_to_seal.encode()).hexdigest()

        # 5. Build Final Output with Production Metadata
        result = {
            "version": VERSION,
            "schema_version": SCHEMA_VERSION,
            "seal": seal,
            "data": data,
            "metadata": {
                "execution_time": datetime.utcnow().isoformat() + "Z",
                "commit_hash": COMMIT_HASH,
                "idempotency_safe": True,
                "determinism_score": 1.0
            }
        }

        # 6. Return Normalized JSON
        return json.dumps(result, indent=2)

    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": f"Skill execution failed: {str(e)}"
        })
