#!/usr/bin/env python3
"""audit_classifier.py – Scan AuditRecord logs and report evidence coverage per RFC‑A001 layer.

Usage:
    python -m axcontrol.audit.audit_classifier.py
"""
import json
import pathlib
import sys
from collections import defaultdict

# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------
LOG_DIR = pathlib.Path(__file__).parent.parent / "logs"  # Fixed path relative to script

# Mapping from RFC‑A001 layer to heuristic that identifies relevant records.
LAYER_MAP = {
    "sovereignty": lambda r: r.get("effect", "").startswith("UI_EMIT"),
    "identity": lambda r: "MODEL_ID" in r.get("metadata", {}),
    "routing": lambda r: r.get("policy_outcome", "").startswith("ROUTED") or r.get("effect", "").startswith("ROUTED"),
    "retry": lambda r: r.get("retry_count", 0) > 0,
    "fallback": lambda r: r.get("effect", "").startswith("FALLBACK"),
    "threat": lambda r: r.get("threat_test", False),
    "verdict": lambda r: r.get("verdict_stage", False),
}

# Evidence levels (hard‑proof = Level 1, strong = Level 2, weak = Level 3)
LEVEL_KEY = {
    "level1": lambda r: r.get("evidence_level") == 1,
    "level2": lambda r: r.get("evidence_level") == 2,
    "level3": lambda r: r.get("evidence_level") == 3,
}


def load_records() -> list:
    """Load all JSON AuditRecord files from LOG_DIR."""
    records = []
    if not LOG_DIR.is_dir():
        print(f"[WARN] Log directory {LOG_DIR} does not exist", file=sys.stderr)
        return records
    for p in LOG_DIR.glob("*.json"):
        try:
            with p.open() as f:
                data = json.load(f)
                if isinstance(data, list):
                    records.extend(data)
                else:
                    records.append(data)
        except Exception as e:
            print(f"[WARN] Could not read {p}: {e}", file=sys.stderr)
    return records


def classify(records: list) -> dict:
    """Return a nested dict: {layer: {level1, level2, level3, total}}"""
    # Pre-initialize summary to avoid defaultdict issues in strict typing
    summary = {
        layer: {"level1": 0, "level2": 0, "level3": 0, "total": 0}
        for layer in LAYER_MAP
    }

    for rec in records:
        for layer, predicate in LAYER_MAP.items():
            if predicate(rec):
                summary[layer]["total"] += 1
                for lvl, lvl_pred in LEVEL_KEY.items():
                    if lvl_pred(rec):
                        summary[layer][lvl] += 1
                break  # a record belongs to a single layer
    return summary


def print_table(summary: dict) -> None:
    header = f"{'Layer':<12} {'#L1':>5} {'#L2':>5} {'#L3':>5} {'Total':>6}"
    print(header)
    print("-" * len(header))
    for layer, stats in sorted(summary.items()):
        print(
            f"{layer:<12} {stats['level1']:>5} {stats['level2']:>5} {stats['level3']:>5} {stats['total']:>6}"
        )
    print("\nLegend: L1 = hard‑proof, L2 = strong, L3 = weak evidence.")


def main():
    records = load_records()
    if not records:
        print("[INFO] No audit records found.")
        return
    summary = classify(records)
    print_table(summary)

if __name__ == "__main__":
    main()
