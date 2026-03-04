import requests
import json
import config
import logging

logger = logging.getLogger("ACE_OLLAMA_CLIENT")

def chat_with_ollama(prompt: str, system_prompt: str = None):
    """
    Sends a prompt to the local Ollama instance.
    """
    url = f"{config.OLLAMA_BASE_URL}/api/generate"

    full_prompt = prompt
    if system_prompt:
        full_prompt = f"System: {system_prompt}\n\nUser: {prompt}\n\nAssistant:"

    payload = {
        "model": config.OLLAMA_MODEL,
        "prompt": full_prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload, timeout=120) # Long timeout for 8B models on local hardware
        response.raise_for_status()
        result = response.json()
        return result.get("response", "No response from AI.")
    except Exception as e:
        logger.error(f"Ollama request failed: {e}")
        return f"Error connecting to Ollama brain: {e}"

if __name__ == "__main__":
    # Simple CLI test
    import sys
    test_input = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Hello, who are you?"
    print(f"Ollama Response: {chat_with_ollama(test_input)}")
