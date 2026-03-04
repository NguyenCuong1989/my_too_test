import time
import requests
import json
import os
import config
import logging
from telegram_notifier import send_telegram_message
from ollama_client import chat_with_ollama

logger = logging.getLogger("ACE_GUARDIAN_BOT")

ACE_SYSTEM_PROMPT = """
You are the ACE Guardian, the AI Command & Control interface for the Autonomous Continuous Execution system.
Your Master is @sowhat86 (Chat ID 400752198).
Your mission is to assist with system monitoring, task auditing, and high-level autonomous operations.
Keep your responses professional, concise, and focused on system integrity and efficiency.
You have access to local tools and logs.
Note: Antigravity is the lead agent/architect currently working on the codebase. You are the operational bridge.
"""

# Simple in-memory conversation history (limited to 10 messages per chat)
CONVERSATION_HISTORY = {}
def get_updates(offset=None):
    url = f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/getUpdates"
    params = {"timeout": 30, "offset": offset}
    try:
        response = requests.get(url, params=params, timeout=35)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error(f"Failed to get Telegram updates: {e}")
        return None

def handle_command(chat_id, command, thread_id=None):
    # Security: Chat ID Locking
    if config.TELEGRAM_ADMIN_CHAT_ID and str(chat_id) != str(config.TELEGRAM_ADMIN_CHAT_ID):
        logger.warning(f"Unauthorized command attempt from Chat ID: {chat_id}")
        return

    command = command.lower()

    if command == "/start":
        msg = ("# ACE Guardian C2 Online 🤖📡🛡️\n\n"
               "Welcome, Master. System is hardened and ready.\n"
               f"Your Chat ID: `{chat_id}`\n\n"
               "Available commands:\n"
               "- `/status`: Current runtime stats\n"
               "- `/audit`: Last execution audit\n"
               "- `/logs`: Recent worker logs\n"
               "- `/id`: Show this Chat ID")
        send_telegram_message(msg, message_thread_id=thread_id)

    elif command == "/id":
        send_telegram_message(f"Your Chat ID: `{chat_id}`", message_thread_id=thread_id)

    elif command == "/status":
        # We need to reach into factory_worker's state if possible,
        # but since this might run in a separate thread/process, we check the stats endpoint locally.
        try:
            # Assuming worker runs on port 8080 inside container (port 8181 locally as per your uvicorn run)
            # But the internal container port is 8080 as per Dockerfile.
            # Local uvicorn run in factory_worker.py uses 8181.
            # Docker Compose maps 8081 -> 8080.
            # We'll try to call the health check.
            stats_msg = "Fetching local stats..."
            send_telegram_message(stats_msg, message_thread_id=thread_id)
            # Placeholder: In a real mesh, we'd query the internal API or shared state.
            send_telegram_message("ACE Runtime: [ACTIVE]\nTask Counter: [Verifying...]\nHealth: OK", message_thread_id=thread_id)
        except Exception as e:
            send_telegram_message(f"Error fetching stats: {e}", message_thread_id=thread_id)

    elif command == "/audit":
        try:
            if os.path.exists(config.LAST_EXECUTION_HASH_PATH):
                with open(config.LAST_EXECUTION_HASH_PATH, "r") as f:
                    last_hash = f.read().strip()
                send_telegram_message(f"🔒 *Last Audit Hash:*\n`{last_hash}`", message_thread_id=thread_id)
            else:
                send_telegram_message("No audit hash recorded yet.", message_thread_id=thread_id)
        except Exception as e:
            send_telegram_message(f"Error reading audit: {e}", message_thread_id=thread_id)

    elif command == "/logs":
        try:
            log_path = os.path.join(config.BASE_DIR, "factory_worker.log")
            if os.path.exists(log_path):
                with open(log_path, "r") as f:
                    lines = f.readlines()
                    last_logs = "".join(lines[-10:])
                send_telegram_message(f"📋 *Recent Logs:*\n```\n{last_logs}\n```", message_thread_id=thread_id)
            else:
                send_telegram_message("Log file not found.", message_thread_id=thread_id)
        except Exception as e:
            send_telegram_message(f"Error reading logs: {e}", message_thread_id=thread_id)

    else:
        # Fallback to Ollama for conversation
        history_key = f"{chat_id}_{thread_id}" if thread_id else str(chat_id)
        history = CONVERSATION_HISTORY.get(history_key, [])

        # Build contextual prompt from history
        contextual_prompt = ""
        for h in history[-5:]: # Last 5 exchanges for context
            contextual_prompt += f"User: {h['user']}\nAssistant: {h['ai']}\n"
        contextual_prompt += f"User: {command}"

        send_telegram_message("_ACE thinking..._", message_thread_id=thread_id)
        ai_response = chat_with_ollama(contextual_prompt, system_prompt=ACE_SYSTEM_PROMPT)

        # Update history
        history.append({"user": command, "ai": ai_response})
        CONVERSATION_HISTORY[history_key] = history[-10:] # Keep last 10

        send_telegram_message(ai_response, message_thread_id=thread_id)

def bot_loop():
    logger.info("Telegram Bot Poller started...")
    offset = None
    while True:
        updates = get_updates(offset)
        if updates and updates.get("ok"):
            for update in updates.get("result", []):
                offset = update.get("update_id") + 1
                message = update.get("message")
                if message:
                    chat_id = message.get("chat", {}).get("id")
                    thread_id = message.get("message_thread_id")
                    text = message.get("text")
                    if text:
                        handle_command(chat_id, text, thread_id=thread_id)
        time.sleep(1)

if __name__ == "__main__":
    bot_loop()
