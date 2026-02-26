from pathlib import Path
from core.observability.state_diff import StateDiff

def visualize_drift(trace_a: Path, trace_b: Path):
    print(f"--- D&R Protocol: Topology Audit ---")
    print(f"Trace A: {trace_a.name}")
    print(f"Trace B: {trace_b.name}")
    print("-" * 40)

    auditor = StateDiff(trace_a, trace_b)
    diffs = auditor.compare()

    if not diffs:
        print("\u2705 RESULT: ONTOLOGICAL PURITY DETECTED (0% DRIFT)")
        return

    print(f"\u26a0\ufe0f WARNING: {len(diffs)} TOPOLOGICAL VIOLATIONS FOUND")
    for d in diffs:
        print(f"\n[Step: {d['step']}] Type: {d['type']}")
        if d['type'] == "DETERMINISM_VIOLATION":
            print(f"  Hash A: {d['hash_a'][:12]}...")
            print(f"  Hash B: {d['hash_b'][:12]}...")
            print(f"  Drift Path: {d['details']}")
        else:
            print(f"  Presence: A={d['a_present']}, B={d['b_present']}")
    print("\n--- Audit Complete ---")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python3 -m core.observability.diff_viewer <trace_a> <trace_b>")
    else:
        visualize_drift(Path(sys.argv[1]), Path(sys.argv[2]))
