# =============================================================================
# PROJECT: CANON-TO-SYSTEM DETERMINISTIC PROJECTION
# METHOD: D&R PROTOCOL (CLOSED)
#
# ORIGINATOR / CREATOR:
#   alpha_prime_omega
#
# LEGAL ONTOLOGY:
#   This source file is a deterministic projection of a closed Canon.
#   Removal or alteration of this header voids legal and ontological validity.
#
# STATUS:
#   GENERATED — NON-AUTONOMOUS — NON-OWNERLESS
#
# TRACEABILITY:
#   Canon -> COG -> Projection(Π) -> Artifact
#
# =============================================================================
"""
Summarize observation NDJSON logs (local, no network).

- Counts per type/sub/app/role/hex/state.
- Prints top-N simple stats.
"""

import argparse
import json
from collections import Counter
from pathlib import Path


def load_records(path: Path):
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except Exception:
                continue


def summarize(path: Path, top: int):
    c_type = Counter()
    c_sub = Counter()
    c_app = Counter()
    c_role = Counter()
    c_hex = Counter()
    c_state = Counter()
    n = 0
    for rec in load_records(path):
        n += 1
        c_type[rec.get("type")] += 1
        if rec.get("sub"):
            c_sub[rec.get("sub")] += 1
        if rec.get("app"):
            c_app[rec.get("app")] += 1
        if rec.get("role"):
            c_role[rec.get("role")] += 1
        if rec.get("hex"):
            c_hex[rec.get("hex")] += 1
        if rec.get("state"):
            c_state[rec.get("state")] += 1
    print(f"File: {path}")
    print(f"Total records: {n}")
    print(f"Type: {c_type}")
    if c_sub:
        print(f"Sub: {c_sub.most_common(top)}")
    if c_app:
        print(f"App: {c_app.most_common(top)}")
    if c_role:
        print(f"Role: {c_role.most_common(top)}")
    if c_hex:
        print(f"Hex: {c_hex.most_common(top)}")
    if c_state:
        print(f"State: {c_state}")


def main():
    ap = argparse.ArgumentParser(description="Summarize observation NDJSON logs.")
    ap.add_argument("logfile", type=Path, help="NDJSON log file")
    ap.add_argument("--top", type=int, default=10, help="Top-N for app/role/hex")
    args = ap.parse_args()
    summarize(args.logfile, args.top)


if __name__ == "__main__":
    main()
