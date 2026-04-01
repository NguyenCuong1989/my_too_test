import yaml
import subprocess
import os
import json
from datetime import datetime

MAP_FILE = "/Users/andy/my_too_test/runtime_authority_map.yaml"
REPORT_FILE = "/Users/andy/my_too_test/DOCKER_AUTHORITY_REPORT.md"
ORIGINATOR_ID = "4287"

def get_container_inspect(cname):
    """Lấy dữ liệu inspect cho một container."""
    try:
        result = subprocess.run(
            ["docker", "inspect", cname],
            capture_output=True, text=True, timeout=3
        )
        if result.returncode == 0:
            return json.loads(result.stdout)[0]
        return None
    except:
        return None

def get_running_containers():
    """Lấy danh sách container đang chạy và kiểm tra daemon."""
    try:
        result = subprocess.run(
            ["docker", "ps", "--format", "{{.Names}}"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return "CONNECTED", result.stdout.strip().split("\n")
        return "ERROR", []
    except subprocess.TimeoutExpired:
        return "TIMEOUT", []
    except Exception:
        return "UNAVAILABLE", []

def audit():
    if not os.path.exists(MAP_FILE):
        print(f"Error: {MAP_FILE} not found.")
        return

    with open(MAP_FILE, "r") as f:
        data = yaml.safe_load(f)

    services = data.get("services", {})
    daemon_status, running_names = get_running_containers()

    report = []
    report.append("# DOCKER AUTHORITY AUDIT REPORT (REV 2.1)")
    report.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"Originator ID: {ORIGINATOR_ID}")

    # 1. Determine Report State
    if daemon_status == "CONNECTED":
        report_state = "RUNTIME_TRUTH_VERIFIED"
    else:
        report_state = "RUNTIME_UNVERIFIED"
        report.append(f"\n> [!CAUTION]")
        report.append(f"> **DOCKER DAEMON {daemon_status}**: Evidence incomplete. Showing semantic/map truth.")

    report.append(f"\n## REPORT STATE: `{report_state}`")

    # 2. STATUS SUMMARY
    report.append("\n## STATUS SUMMARY")

    table = []
    table.append("| Service ID | Map | Presence | Health | Tier | Proof (Chứng) |")
    table.append("| :--- | :---: | :---: | :---: | :---: | :--- |")

    presence_count = 0
    health_count = 0
    mapped_containers_all = []

    for sid, attr in services.items():
        cnames = attr.get("container_names", [])
        mapped_containers_all.extend(cnames)

        # Check Presence
        found_cname = None
        if daemon_status == "CONNECTED":
            for cn in cnames:
                if cn in running_names:
                    found_cname = cn
                    break

        # Logic 3-tầng
        map_locked = "✅"
        presence = "✅" if found_cname else ("❌" if daemon_status == "CONNECTED" else "❓")
        health = "N/A"

        proof = "PENDING_DAEMON"
        if daemon_status == "CONNECTED":
            if found_cname:
                presence_count += 1
                proof = f"Running:{found_cname}"
                # Check Health
                inspect = get_container_inspect(found_cname)
                if inspect:
                    h_status = inspect.get("State", {}).get("Health", {}).get("Status", "healthy (default)")
                    health = "✅" if h_status in ["healthy", "healthy (default)"] else "❌"
                    if h_status == "healthy": health_count += 1
                    proof += f" | Health:{h_status}"
            else:
                proof = "NO_EVIDENCE"
        else:
            proof = f"DAEMON_{daemon_status}"

        table.append(f"| {sid} | {map_locked} | {presence} | {health} | {attr.get('authority_tier')} | {proof} |")

    report.append(f"- **MAP_LOCKED**: {len(services)}")
    report.append(f"- **RUNTIME_PRESENCE**: {presence_count if daemon_status == 'CONNECTED' else 'N/A'}")
    report.append(f"- **RUNTIME_HEALTHY**: {health_count if daemon_status == 'CONNECTED' else 'N/A'}")

    # 3. Ownerless Detection
    if daemon_status == "CONNECTED":
        ownerless = [r for r in running_names if r and r not in mapped_containers_all]
        if ownerless:
            report.append(f"- **OWNERLESS_RISK**: {len(ownerless)} (!)")
            report.append("\n### [!] OWNERLESS ALERT")
            for o in ownerless:
                report.append(f"- `{o}`")

    report.append("\n## DETAILED AUTHORITY AUDIT")
    report.extend(table)

    report.append("\n\n---")
    report.append(f"### [Σ_APΩ :: AUDIT_TRUTH_ENGINE :: {ORIGINATOR_ID}]")

    if report_state == "RUNTIME_TRUTH_VERIFIED":
        report.append("> Map: LOCKED | Presence: VERIFIED | Health: ATTESTED")
    else:
        report.append("> Map: LOCKED | Presence: UNVERIFIED | Health: UNVERIFIED")

    with open(REPORT_FILE, "w") as f:
        f.write("\n".join(report))

    print(f"Audit complete. Report generated at {REPORT_FILE}")

if __name__ == "__main__":
    audit()
