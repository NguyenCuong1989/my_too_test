import os

# Security
JWT_SECRET = os.getenv("JWT_SECRET", "super-secret-mcp-key")
WHITELISTED_SKILLS = [
    "hello_world_skill",
    "biz_node_sync",
    "web_scout_task",
    "docker_deploy_skill",
    "sli_enrichment"
]

# Skill Integrity Registry (SHA-256)
# Format: { "skill_name": "expected_hash" }
SKILL_REGISTRY = {
    "hello_world_skill": "f548262c71985c4ea3bd68f19d915e35b1dbccfc4790b0708b97f8d775623a42",
    "sli_enrichment": "d290b66a81aebe46104b17543f7accca380977e8d6ef3c8fa43a1bf203d7b446"
}

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INBOX_DIR = os.path.join(BASE_DIR, "inbox")
PROCESSING_DIR = os.path.join(BASE_DIR, "processing")
PROCESSED_DIR = os.path.join(BASE_DIR, "processed")
FAILED_DIR = os.path.join(BASE_DIR, "failed")
TOOLS_DIR = os.path.join(BASE_DIR, "tools")
SCHEMA_PATH = os.path.join(BASE_DIR, "schemas", "task_schema.json")

# Operational
SLEEP_INTERVAL = 2  # Seconds
MAX_RETRIES = 3
CIRCUIT_BREAKER_THRESHOLD = 5
MAX_TASKS_PER_HOUR = 60
MAX_FAILURE_THRESHOLD = 10
LOG_LEVEL = "INFO"
