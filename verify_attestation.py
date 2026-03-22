import yaml
import os
import hashlib
import sys
import subprocess
import json

# PATHS
MAP_FILE = "/Users/andy/my_too_test/runtime_authority_map.yaml"
ORIGINATOR_ID = "4287"

class AttestationEngine:
    def __init__(self):
        self.map_data = self._load_map()

    def _load_map(self):
        if not os.path.exists(MAP_FILE):
            return None
        with open(MAP_FILE, "r") as f:
            return yaml.safe_load(f)

    def verify_map_admissibility(self, service_id):
        """Tier 1: Kiểm tra tính hợp lệ của bản đồ (Map Attestation)."""
        if not self.map_data:
            return False, "E_NO_MAP: Authority Map missing."

        originator = self.map_data.get("metadata", {}).get("originator", "")
        if ORIGINATOR_ID not in originator:
            return False, f"E_INVALID_ORIGINATOR: Expected {ORIGINATOR_ID}."

        services = self.map_data.get("services", {})
        if service_id not in services:
            return False, f"E_OWNERLESS: Service ID {service_id} not in map."

        attr = services[service_id]
        # container_names (REV 2.1)
        required_keys = ["container_names", "authority_tier", "survival_class", "role"]
        for key in required_keys:
            if key not in attr:
                return False, f"E_INCOMPLETE_ATTR: Missing {key} for {service_id}."

        return True, f"MAP_VALID: {service_id} structure is lawful."

    def verify_runtime_evidence(self, service_id):
        """Tier 2: Kiểm tra thực tại runtime nâng cao (Health-aware Runtime Attestation)."""
        is_map_valid, msg = self.verify_map_admissibility(service_id)
        if not is_map_valid:
            return False, msg

        container_names = self.map_data["services"][service_id]["container_names"]

        last_err = "No container found."
        for cname in container_names:
            try:
                # Lấy toàn bộ inspect JSON để phân tích sâu
                result = subprocess.run(
                    ["docker", "inspect", cname],
                    capture_output=True, text=True, timeout=5
                )
                if result.returncode != 0:
                    last_err = f"E_RUNTIME_MISSING: {cname} not found."
                    continue

                info = json.loads(result.stdout)[0]
                state = info.get("State", {})
                is_running = state.get("Running", False)
                started_at = state.get("StartedAt", "unknown")

                if not is_running:
                    return False, f"E_RUNTIME_STOPPED: {cname} exists but NOT running."

                # Kiểm tra Health (nếu có)
                health = state.get("Health", {})
                health_status = health.get("Status", "N/A (No healthcheck)")

                if health_status == "unhealthy":
                    return False, f"E_RUNTIME_UNHEALTHY: {cname} is running but UNHEALTHY."

                evidence = {
                    "container": cname,
                    "status": "RUNNING",
                    "health": health_status,
                    "started_at": started_at
                }

                return True, f"RUNTIME_VERIFIED: {json.dumps(evidence)}"
            except subprocess.TimeoutExpired:
                return False, "E_DAEMON_TIMEOUT: Docker daemon is unresponsive."
            except Exception as e:
                last_err = f"E_DAEMON_ERROR: {str(e)}"

        return False, last_err

    def get_canon_hash(self):
        if not self.map_data: return "0" * 64
        content = yaml.dump(self.map_data, sort_keys=True)
        return hashlib.sha256(content.encode()).hexdigest()

def main():
    engine = AttestationEngine()
    if len(sys.argv) < 3:
        print("Usage: python3 verify_attestation.py <mode: map|runtime> <service_id>")
        sys.exit(1)

    mode = sys.argv[1]
    service = sys.argv[2]

    if mode == "map":
        valid, msg = engine.verify_map_admissibility(service)
    elif mode == "runtime":
        valid, msg = engine.verify_runtime_evidence(service)
    else:
        print(f"Unknown mode: {mode}")
        sys.exit(1)

    if valid:
        print(f"[✓] {msg}")
        print(f"[#] CanonHash: {engine.get_canon_hash()[:16]}")
    else:
        print(f"[!] ATTESTATION FAILED: {msg}")
        sys.exit(1)

if __name__ == "__main__":
    main()
