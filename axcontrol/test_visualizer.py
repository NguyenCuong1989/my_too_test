import json
from pathlib import Path
from core.observability.diff_viewer import visualize_drift

def create_mock_logs():
    log_a = Path("logs/mock_a.ndjson")
    log_b = Path("logs/mock_b.ndjson")
    log_a.parent.mkdir(exist_ok=True)

    # Trace A (Purity)
    records_a = [
        {"timestamp": "step-000001", "Chung": "hash1", "state_before": {"val": 10}},
        {"timestamp": "step-000002", "Chung": "hash2", "state_before": {"val": 20}}
    ]

    # Trace B (With Drift at step 2)
    records_b = [
        {"timestamp": "step-000001", "Chung": "hash1", "state_before": {"val": 10}},
        {"timestamp": "step-000002", "Chung": "hash2_drift", "state_before": {"val": 25}}
    ]

    with open(log_a, "w") as f:
        for r in records_a: f.write(json.dumps(r) + "\n")
    with open(log_b, "w") as f:
        for r in records_b: f.write(json.dumps(r) + "\n")

    return log_a, log_b

if __name__ == "__main__":
    a, b = create_mock_logs()
    print("Testing DRIFT DETECTED scenario:")
    visualize_drift(a, b)

    print("\nTesting PURITY scenario:")
    visualize_drift(a, a)
