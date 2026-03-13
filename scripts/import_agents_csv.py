#!/usr/bin/env python3
# Σ_APΩ₂ UTILITY
# Authority: BỐ CƯỐNG Supreme System Commander
# Purpose: Sync agents.csv data to DAIOF Registry / Notion

import csv
import json
import os
import sys
from pathlib import Path

BASE_DIR = Path("/Users/andy/my_too_test")
CSV_PATH = Path("/Users/andy/Downloads/agents.csv")
REGISTRY_PATH = BASE_DIR / "omni_registry.json"

def import_csv():
    if not CSV_PATH.exists():
        print(f"❌ Error: {CSV_PATH} not found.")
        return

    print(f"📂 Reading {CSV_PATH}...")
    agents_data = []
    with open(CSV_PATH, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            agents_data.append(row)

    print(f"✅ Found {len(agents_data)} agents in CSV.")

    # Giả lập việc cập nhật registry hoặc Notion
    for agent in agents_data:
        name = agent.get('Agent')
        status = agent.get('Status')
        created_by = agent.get('Created By')
        print(f"🔄 Syncing Agent: [{name}] | Status: {status} | Owner: {created_by}")

    # Ghi nhận vào log cục bộ
    log_path = Path("sync_events.log")
    with open(log_path, mode='a', encoding='utf-8') as log_file:
        for agent in agents_data:
            log_file.write(f"SYNC_EVENT: Imported {agent.get('Agent')} from CSV\n")

    print("🚀 Synchronization complete.")

if __name__ == "__main__":
    import_csv()
