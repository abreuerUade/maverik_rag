from pydantic import BaseModel
from typing import List, Tuple

class ChatRequest(BaseModel):
    userProfile: str
    chatHistory: List[Tuple[str, str]]
    input: str


class ChatResponse(BaseModel):
    response: str
