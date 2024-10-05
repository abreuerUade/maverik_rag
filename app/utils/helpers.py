from langchain_core.messages import AIMessage, HumanMessage
from typing import List, Tuple

# Historial de chat global
chat_history: List[Tuple[str, str]] = []


def format_chat_history(history: List[Tuple[str, str]]):
    buffer = []
    for human, ai in history:
        buffer.append(HumanMessage(content=human))
        buffer.append(AIMessage(content=ai))
    return buffer
