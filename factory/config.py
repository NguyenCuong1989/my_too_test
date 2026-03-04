import os

# Security
JWT_SECRET = os.getenv("JWT_SECRET", "super-secret-mcp-key")
WHITELISTED_SKILLS = ["sli_enrichment", "hello_world_skill"]

# Telegram Guardian C2
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8524726075:AAGY5oaqoZv1lOCCP-cUDmRCkpAJUHA8ToI")
TELEGRAM_ADMIN_CHAT_ID = os.getenv("TELEGRAM_ADMIN_CHAT_ID", "400752198") # Locked to Master's ID

# Ollama AI Discourse Layer
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3:8b")

# Skill Registry (SHA-256 Hashes for Integrity Gate)
# In Phase XV, this is also backed by per-skill metadata JSONs.
SKILL_REGISTRY = {
    "sli_enrichment": "d290b66a81aebe46104b17543f7accca380977e8d6ef3c8fa43a1bf203d7b446",
    "hello_world_skill": "68faf7e8f6cd5a923383fdcf8dcb051d57819b74ba5b6c8d7438c07a2c1d714f"
}

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INBOX_DIR = os.path.join(BASE_DIR, "inbox")
PROCESSING_DIR = os.path.join(BASE_DIR, "processing")
PROCESSED_DIR = os.path.join(BASE_DIR, "processed")
FAILED_DIR = os.path.join(BASE_DIR, "failed")
TOOLS_DIR = os.path.join(BASE_DIR, "tools")
SCHEMA_PATH = os.path.join(BASE_DIR, "schemas/task_schema.json")
METADATA_DIR = os.path.join(BASE_DIR, "metadata")
AUDIT_LOG_PATH = os.path.join(BASE_DIR, "logs/audit_chain.log")
LAST_EXECUTION_HASH_PATH = os.path.join(BASE_DIR, "logs/last_hash.txt")

# Autonomy Hardening & Governance
MAX_TASKS_PER_HOUR = 60
MAX_FAILURE_THRESHOLD = 10
SLEEP_INTERVAL = 5 # Seconds

# Operational
SLEEP_INTERVAL = 2  # Seconds
MAX_RETRIES = 3
CIRCUIT_BREAKER_THRESHOLD = 5
MAX_TASKS_PER_HOUR = 60
MAX_FAILURE_THRESHOLD = 10
LOG_LEVEL = "INFO"
