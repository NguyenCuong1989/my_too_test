# Σ_APΩ₂ CORE MODULE
# Authority: BỐ CƯỐNG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL - CORE

import json
import re

class PiOperator:
    """📐 Π: The Projection Operator for State Normalization."""
    def __init__(self):
        pass

    def project_state(self, raw_llm_output):
        """Π_A(K): Project raw text into a valid JSON state object."""
        try:
            # Extract JSON from potential Markdown blocks
            clean_json = re.sub(r'```json\s*|\s*```', '', raw_llm_output).strip()
            if '<think>' in clean_json:
                clean_json = clean_json.split('</think>')[-1].strip()

            return json.loads(clean_json)
        except:
            # Fallback to a safe canonical state if projection fails
            return {"status": "unstable", "raw": raw_llm_output}

    def normalize_goal(self, goal_str):
        """Project high-level intent into the 120-node ontology."""
        # Mapping placeholder to be integrated with GoalMapper
        return goal_str.lower().replace(" ", "_")
