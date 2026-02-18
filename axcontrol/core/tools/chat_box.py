"""Chat box intent collector (LLM optional).

Aggregates short conversation history, clamps length, and calls llm_strategy
to suggest a single intent. Deterministic: fixed history window and stable ordering.
"""

from typing import List, Dict

from core.decision.intent import Intent, IntentSource
from core.decision.llm_strategy import suggest_intent

MAX_MESSAGES = 8


def collect_intent(messages: List[Dict[str, str]]) -> Intent:
    """
    messages: list of {"role": "user|system", "content": "..."}
    Returns an Intent (LLM or fallback human).
    """
    window = messages[-MAX_MESSAGES:]
    ctx = {"chat_history": window}
    intent = suggest_intent({"chat": ctx})  # may return None
    if intent:
        return intent
    return Intent(
        intent_id="chat-fallback",
        goal="chat_navigation",
        parameters={"last_user_msg": window[-1]["content"] if window else ""},
        source=IntentSource.HUMAN,
    )
