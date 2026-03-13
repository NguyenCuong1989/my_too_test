#!/usr/bin/env python3
# Σ_APΩ₂ CORE MODULE - OPERATIONAL WRAPPER
# Authority: BỐ CƯỐNG Supreme System Commander
# Status: CANONICAL COMPATIBILITY LAYER

import sys
import os
import logging
from unittest.mock import MagicMock

# Programmatic Logging (Bypassing Shell Redirection)
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("/tmp/phoenix_boot.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("PHOENIX_WRAPPER")

# 1. Mock problematic modules for Python 3.14 compatibility
for module in [
    "chromadb", "sentence_transformers", "langchain", "langchain.agents",
    "langchain_google_genai", "langchain.memory", "langchain.prompts",
    "langchain.chains", "google_auth_oauthlib", "google_auth_oauthlib.flow",
    "googleapiclient", "googleapiclient.discovery", "google.auth.transport.requests",
    "ollama", "notion_client", "playwright", "playwright.async_api",
    "google.generativeai", "google.ai.generativelanguage", "google.genai"
]:
    sys.modules[module] = MagicMock()

# Specific fixes for common attribute access
sys.modules["google_auth_oauthlib.flow"].InstalledAppFlow = MagicMock()
sys.modules["googleapiclient.discovery"].build = MagicMock()

# 2. Setup paths
BASE_DIR = "/Users/andy/my_too_test"
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, "autonomous_operator"))

# 3. Import and Run
logger.info("🔥 DAIOF PHOENIX OPERATIONAL WRAPPER (Kernel v1.1) STARTING...")
try:
    from autonomous_operator.orchestrator_v3 import AutonomousOperator
    import asyncio

    operator = AutonomousOperator()
    # Start Phoenix Bridge
    logger.info("🧠 Initializing Phoenix Cognitive Heart...")
    operator.phoenix.start()

    # Run Orchestrator
    logger.info("🚀 Entering Autonomous Main Loop...")
    asyncio.run(operator.main_loop())
except KeyboardInterrupt:
    logger.info("\n🛑 Stopping Operator via Master request...")
    if 'operator' in locals():
        operator.phoenix.stop()
except Exception as e:
    logger.error(f"🚨 CRITICAL SYSTEM FAILURE: {e}")
    import traceback
    traceback.print_exc()
