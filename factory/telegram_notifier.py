import requests
import config
import logging

logger = logging.getLogger("ACE_GUARDIAN_TELEGRAM")

def send_telegram_message(message: str, message_thread_id: int = None):
    """
    Sends a message to the Master's Telegram Chat.
    Uses basic requests to avoid heavy dependencies in the worker.
    """
    if not config.TELEGRAM_BOT_TOKEN:
        logger.warning("Telegram Bot Token not configured. Skipping notification.")
        return False

    if not config.TELEGRAM_ADMIN_CHAT_ID:
        # If admin ID is not set, we can't send messages.
        # Master needs to send /start to set it.
        logger.warning("Telegram Admin Chat ID not set. Master needs to send /start.")
        return False

    url = f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": config.TELEGRAM_ADMIN_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    if message_thread_id:
        payload["message_thread_id"] = message_thread_id

    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        return True
    except Exception as e:
        logger.error(f"Failed to send Telegram message: {e}")
        return False

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        test_msg = " ".join(sys.argv[1:])
        if send_telegram_message(test_msg):
            print("Message sent successfully.")
        else:
            print("Failed to send message.")
