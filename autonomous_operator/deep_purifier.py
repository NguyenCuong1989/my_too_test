# Σ_APΩ₂ CORE MODULE
# Authority: BỐ CƯỐNG Supreme System Commander
# Creator: Antigravity (via alpha_prime_omega 4287)
# Status: CANONICAL (Kernel v1.1)

import os
import sys
import ast
import logging
import json
from pathlib import Path
from datetime import datetime

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [DPE] [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("/tmp/deep_purifier.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("DeepPurifier")

class DeepPurifier:
    """
    Antigravity's Deep Purification Engine (DPE).
    Recursive Refactoring & Ecosystem Canonicalization.
    """
    def __init__(self, root_dir: str):
        self.root_dir = Path(root_dir)
        self.stats = {
            "files_scanned": 0,
            "redundancy_removed": 0,
            "headers_injected": 0,
            "disk_reclaimed_mb": 0
        }

    def purify_ecosystem(self):
        logger.info(f"🚀 DPE: Initiating Ecosystem-Wide Purification in {self.root_dir}...")
        self.scan_and_fix_python_files()
        self.cleanup_known_bloat()
        self.report_status()

    def scan_and_fix_python_files(self):
        """Recursively scan Python files for dead code and redundancy."""
        for py_file in self.root_dir.rglob("*.py"):
            if ".git" in str(py_file) or "venv" in str(py_file) or "__pycache__" in str(py_file):
                continue

            self.stats["files_scanned"] += 1
            self.refactor_file(py_file)

    def refactor_file(self, file_path: Path):
        """Perform surgical refactoring to remove duplicate 'run' functions and inject headers."""
        try:
            # 1. Deduplicate 'run' functions
            self.surgical_string_deduplication(file_path)

            # 2. Inject Kernel v1.1 Canonical Headers if missing
            self.inject_canonical_header(file_path)

        except Exception as e:
            logger.error(f"❌ DPE: Error processing {file_path}: {e}")

    def inject_canonical_header(self, file_path: Path):
        """Inject the Kernel v1.1 authority header if not present."""
        canonical_marker = "# Authority: BỐ CƯỐNG Supreme System Commander"
        header = f"""# Σ_APΩ₂ CORE MODULE
{canonical_marker}
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL (Kernel v1.1)

"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            if canonical_marker not in content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(header + content)
                self.stats["headers_injected"] += 1
                logger.info(f"💾 DPE: Injected Canonical Header into {file_path.name}")
        except Exception as e:
            pass

    def surgical_string_deduplication(self, file_path: Path):
        """String-based surgical removal of identical 'run' function blocks."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            run_indices = []
            for i, line in enumerate(lines):
                if line.strip().startswith("def run(payload: str = None) -> str:"):
                    run_indices.append(i)

            if len(run_indices) > 1:
                # Keep ONLY the last one.
                last_idx = run_indices[-1]
                other_indices = run_indices[:-1]

                # Logic to find the end of those functions (simple indentation check)
                to_delete = set()
                for start_idx in other_indices:
                    to_delete.add(start_idx)
                    for j in range(start_idx + 1, len(lines)):
                        if lines[j].strip() == "" or lines[j].startswith(" ") or lines[j].startswith("\t"):
                            to_delete.add(j)
                        else:
                            # Start of another top-level construct
                            if j in run_indices: # Found next run func
                                break
                            # If it's a comment or special line, keep it maybe?
                            # Safe bet: stop at first non-indented line that isn't a newline
                            if lines[j].strip() != "" and not lines[j].startswith(" ") and not lines[j].startswith("\t"):
                                break
                            to_delete.add(j)

                new_lines = [line for i, line in enumerate(lines) if i not in to_delete]

                with open(file_path, "w", encoding="utf-8") as f:
                    f.writelines(new_lines)

                logger.info(f"✅ DPE: Successfully deduplicated {len(run_indices)-1} blocks in {file_path.name}")

        except Exception as e:
            logger.error(f"❌ DPE: String refactor failed on {file_path}: {e}")

    def cleanup_known_bloat(self):
        """Purge system-wide caches and artifacts."""
        bloat_dirs = ["__pycache__", ".pytest_cache", ".DS_Store", "*.pyc"]
        for pattern in bloat_dirs:
            for item in self.root_dir.rglob(pattern):
                try:
                    size = 0
                    if item.is_file():
                        size = item.stat().st_size
                        item.unlink()
                    elif item.is_dir():
                        import shutil
                        size = sum(f.stat().st_size for f in item.rglob('*') if f.is_file())
                        shutil.rmtree(item)

                    self.stats["disk_reclaimed_mb"] += size / (1024 * 1024)
                except Exception as e:
                    pass
        logger.info(f"🧹 DPE: Reclaimed {self.stats['disk_reclaimed_mb']:.2f} MB of disk space.")

    def report_status(self):
        logger.info("-" * 40)
        logger.info("📊 DEEP PURIFICATION SUMMARY")
        logger.info(f"Files Scanned: {self.stats['files_scanned']}")
        logger.info(f"Redundancy Removed: {self.stats['redundancy_removed']} units")
        logger.info(f"Disk Reclaimed: {self.stats['disk_reclaimed_mb']:.2f} MB")
        logger.info("-" * 40)

if __name__ == "__main__":
    purifier = DeepPurifier("/Users/andy/my_too_test")
    purifier.purify_ecosystem()
