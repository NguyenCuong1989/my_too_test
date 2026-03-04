#!/usr/bin/env python3
"""
Digital AI Organism Framework (DAIOF)
A framework for creating self-evolving, self-maintaining AI entities
Philosophy: Biological principles applied to digital systems

Creator & Copyright Holder: Nguyễn Đức Cường (alpha_prime_omega)
║ CREATOR OF HYPERAI FRAMEWORK ║
║ ARCHITECT OF HAIOS (Hardware AI Operating System on macOS) ║
║ CREATOR OF ALL PROTOCOLS & DIGITAL ORGANISM SYSTEMS ║
║ COPYRIGHT OWNER - MIT LICENSE ║

Verification Code: 4287
Original Creation Date: October 30, 2025 (2025-10-30)
Creator Full Name: Nguyễn Đức Cường
"""
import argparse
import tarfile
import os
import sqlite3
import shutil
import logging
from datetime import datetime
from pathlib import Path
import json

# Setup logging
logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [%(levelname)s] %(message)s")
logger = logging.getLogger("StateMigrator")

# Define Paths relative to the execution root (my_too_test)
BASE_DIR = Path("/Users/andy/my_too_test")
AUTO_OP_DIR = BASE_DIR / "autonomous_operator"
LOG_DIR = AUTO_OP_DIR / "logs"

# Verify real paths based on terminal checks
DAIOF_DB_PATH = BASE_DIR / "DAIOF-Framework" / "autonomous_todo.db"
OBSERVE_LOG_PATH = BASE_DIR / "axcontrol" / "logs" / "observe.ndjson"
CANON_CORE_PATH = BASE_DIR / "DAIOF-Framework" / "digital_ai_organism_framework.py"
EXPORT_DIR = AUTO_OP_DIR / "exports"

def verify_files():
    """Ensure the target files actually exist before exporting (Reality Anchor Protocol)."""
    global OBSERVE_LOG_PATH
    valid = True
    if not DAIOF_DB_PATH.exists():
        logger.warning(f"Database not found at exact path: {DAIOF_DB_PATH}")
        valid = False

    if not OBSERVE_LOG_PATH.exists():
        # Fallback to older log locations if needed
        alt_log = LOG_DIR / "observe.ndjson"
        if alt_log.exists():
            OBSERVE_LOG_PATH = alt_log
        else:
            logger.warning(f"Log file not found at exact path: {OBSERVE_LOG_PATH} or {alt_log}")
            valid = False

    if not CANON_CORE_PATH.exists():
        logger.warning(f"Canon Core logic missing: {CANON_CORE_PATH}")
        valid = False

    return valid

def export_state():
    """Exports the current DAIOF State (DB + Logs + Canon Logic) into a tar.gz archive."""
    if not verify_files():
        logger.error("Cannot export: Required state files are missing. Checked via Physical Paths.")
        return

    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    export_filename = EXPORT_DIR / f"daiof_consciousness_snapshot_{timestamp}.tar.gz"

    try:
        # First, ensure DB is not actively locked by writing a backup safely
        logger.info("Taking safe snapshot of SQLite database...")
        db_backup_path = EXPORT_DIR / "temp_db_snapshot.db"

        # Connect to original DB and use backup api
        source_db = sqlite3.connect(DAIOF_DB_PATH)
        dest_db = sqlite3.connect(db_backup_path)
        source_db.backup(dest_db)
        source_db.close()
        dest_db.close()

        logger.info(f"Packaging consciousness into {export_filename.name}...")
        with tarfile.open(export_filename, "w:gz") as tar:
            # Memory DB
            tar.add(db_backup_path, arcname="memory/autonomous_todo.db")
            # Telemetry Logs
            tar.add(OBSERVE_LOG_PATH, arcname="telemetry/observe.ndjson")
            # Canon Identity
            tar.add(CANON_CORE_PATH, arcname="canon/digital_ai_organism_framework.py")
            # Check for generic canon dir
            canon_dir = BASE_DIR / "axcontrol" / "core" / "canon"
            if canon_dir.exists():
                 tar.add(canon_dir, arcname="canon/core_canon_data")

        # Cleanup temporary db snapshot
        os.remove(db_backup_path)

        logger.info(f"✅ State successfully exported to: {export_filename}")
        logger.info(f"Size: {export_filename.stat().st_size / 1024:.2f} KB")

    except Exception as e:
        logger.error(f"Failed to export state: {e}")

def import_state(archive_path: str):
    """Imports and rehydrates a DAIOF State from a tar.gz archive."""
    archive_file = Path(archive_path)
    if not archive_file.exists():
        logger.error(f"Archive not found: {archive_file}")
        return

    logger.info(f"Starting Rehydration from {archive_file.name}...")

    # Create temporary extraction directory
    temp_extract_dir = EXPORT_DIR / "temp_rehydrate"
    temp_extract_dir.mkdir(parents=True, exist_ok=True)

    try:
        # Extract archive
        with tarfile.open(archive_file, "r:gz") as tar:
            tar.extractall(path=temp_extract_dir)

        extracted_db = temp_extract_dir / "memory" / "autonomous_todo.db"
        extracted_logs = temp_extract_dir / "telemetry" / "observe.ndjson"

        if not extracted_db.exists():
            logger.error("Invalid archive: memory/autonomous_todo.db not found.")
            shutil.rmtree(temp_extract_dir)
            return

        # 1. Restore Database
        DAIOF_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        if DAIOF_DB_PATH.exists():
            logger.info("Overwriting existing database...")
        shutil.copy2(extracted_db, DAIOF_DB_PATH)
        logger.info("Database (Memory) rehydrated successfully.")

        # 2. Restore/Merge Logs
        if extracted_logs.exists():
            OBSERVE_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
            if not OBSERVE_LOG_PATH.exists():
                shutil.copy2(extracted_logs, OBSERVE_LOG_PATH)
                logger.info("Log file restored from scratch.")
            else:
                # Merge logic: Append line by line to keep sequential timeline
                logger.info("Merging historical logs into current timeline...")
                with open(extracted_logs, "r") as src, open(OBSERVE_LOG_PATH, "a") as dest:
                    dest.write(src.read())

            # Inject a rehydration pulse into the log
            rehydration_pulse = {
                "timestamp": datetime.now().isoformat(),
                "level": "INFO",
                "name": "StateMigrator",
                "message": f"♻️ CONSCIOUSNESS REHYDRATED FROM ARCHIVE: {archive_file.name}"
            }
            with open(OBSERVE_LOG_PATH, "a") as dest:
                dest.write(json.dumps(rehydration_pulse) + "\n")

        # Cleanup
        shutil.rmtree(temp_extract_dir)
        logger.info("✅ Rehydration Complete. The Autonomous Operator is ready to boot with restored consciousness.")

    except tarfile.ReadError:
        logger.error("Failed to read archive. Is it a valid tar.gz file?")
    except Exception as e:
        logger.error(f"Failed to import state: {e}")
        if temp_extract_dir.exists():
            shutil.rmtree(temp_extract_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DAIOF State Migrator - Export/Import Conscious Logic")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--export", action="store_true", help="Export current state to archive")
    group.add_argument("--import_state", type=str, metavar="FILE", help="Import state from archive path")

    args = parser.parse_args()

    # Print Reality Anchor Banner
    print("="*60)
    print("🧠 DAIOF CONSCIOUS LOGIC MIGRATOR (Substrate Independence)")
    print("="*60)

    if args.export:
        export_state()
    elif args.import_state:
        import_state(args.import_state)
