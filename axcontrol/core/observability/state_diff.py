import json
from pathlib import Path
from typing import List, Dict, Any, Optional

class StateDiff:
    """Computes the topological difference between two deterministic audit traces."""

    def __init__(self, trace_a_path: Path, trace_b_path: Path):
        self.trace_a = self._load_trace(trace_a_path)
        self.trace_b = self._load_trace(trace_b_path)

    def _load_trace(self, path: Path) -> Dict[str, Any]:
        records = {}
        with open(path, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                record = json.loads(line)
                # Key records by the Stable Tick (Iron Hand Step ID)
                ts = record.get("timestamp")
                if ts:
                    records[ts] = record
        return records

    def compare(self) -> List[Dict[str, Any]]:
        diffs: List[Dict[str, Any]] = []
        # Union of all sequence keys
        all_keys = sorted(list(set(self.trace_a.keys()) | set(self.trace_b.keys())))

        for key in all_keys:
            rec_a = self.trace_a.get(key)
            rec_b = self.trace_b.get(key)

            if rec_a is None or rec_b is None:
                diffs.append({
                    "step": key,
                    "type": "MISSING_NODE",
                    "a_present": rec_a is not None,
                    "b_present": rec_b is not None
                })
                continue

            # Explicit casting to Dict for cleaner analysis
            dict_a: Dict[str, Any] = rec_a if isinstance(rec_a, dict) else {}
            dict_b: Dict[str, Any] = rec_b if isinstance(rec_b, dict) else {}

            hash_a = dict_a.get("Chung")
            hash_b = dict_b.get("Chung")

            if hash_a != hash_b:
                diffs.append({
                    "step": key,
                    "type": "DETERMINISM_VIOLATION",
                    "hash_a": hash_a,
                    "hash_b": hash_b,
                    "details": self._deep_diff(rec_a, rec_b)
                })

        return diffs

    def _deep_diff(self, a: Any, b: Any, path: str = "") -> Dict[str, Any]:
        """Recursive diff generator for nested state dictionaries."""
        if a == b:
            return {}

        if type(a) != type(b):
            return {"path": path, "a": f"type({type(a).__name__})", "b": f"type({type(b).__name__})"}

        if isinstance(a, dict):
            keys = set(a.keys()) | set(b.keys())
            res = {}
            for k in keys:
                d = self._deep_diff(a.get(k), b.get(k), f"{path}.{k}" if path else k)
                if d:
                    res[k] = d
            return res

        return {"path": path, "a": a, "b": b}
