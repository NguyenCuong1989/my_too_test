#!/usr/bin/env python3
"""run_audit.py – Pilot audit script for AXCONTROL.

Aggregates findings from audit_classifier and produces audit_report.json.
"""
import json
import os
import pathlib
import sys

# Ensure we can import from the audit directory
sys.path.append(str(pathlib.Path(__file__).parent))

from audit_classifier import classify, load_records

REPORT_PATH = pathlib.Path(__file__).parent / "audit_report.json"

def aggregate_verdict():
    records = load_records()
    if not records:
        print("[FAIL] No records found to audit.")
        return

    summary = classify(records)

    verdict = "COMPLIANT"
    layer_status = {}

    # RFC-A001 Logic: Hard-proof layers (Sovereignty, Routing) MUST have Level 1
    # Check Sovereignty (requires Level 1)
    if summary.get("sovereignty", {}).get("level1", 0) > 0:
        layer_status["sovereignty"] = "PROVEN"
    else:
        layer_status["sovereignty"] = "NOT ESTABLISHED"
        verdict = "NON-COMPLIANT"

    # Check Routing (requires Level 1)
    if summary.get("routing", {}).get("level1", 0) > 0:
        layer_status["routing"] = "PROVEN"
    else:
        layer_status["routing"] = "NOT ESTABLISHED"
        verdict = "NON-COMPLIANT"

    # Check Identity (can be Permissible with Level 2)
    if summary.get("identity", {}).get("level2", 0) > 0:
        layer_status["identity"] = "PERMISSIBLE"
    elif summary.get("identity", {}).get("level1", 0) > 0:
        layer_status["identity"] = "PROVEN"
    else:
        layer_status["identity"] = "NOT ESTABLISHED"

    # Check Retry (requires Level 1/2 for COMPLIANT)
    if summary.get("retry", {}).get("level1", 0) > 0 or summary.get("retry", {}).get("level2", 0) > 0:
        layer_status["retry"] = "PROVEN"
    else:
        layer_status["retry"] = "NOT ESTABLISHED"
        # We don't fail the whole audit for Retry yet in this pilot

    report = {
        "verdict": verdict,
        "layers": layer_status,
        "raw_summary": summary
    }

    with open(REPORT_PATH, "w") as f:
        json.dump(report, f, indent=2)

    print(f"--- PILOT AUDIT VERDICT: {verdict} ---")
    for layer, status in layer_status.items():
        print(f"Layer {layer:<12}: {status}")
    print(f"\nReport written to {REPORT_PATH}")

if __name__ == "__main__":
    aggregate_verdict()
