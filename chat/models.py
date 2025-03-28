from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class ChatMessage(BaseModel):
    user_id: str
    message: str
    conversation_id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

class ChatResponse(BaseModel):
    response: str
    sources: Optional[List[Dict[str, str]]] = None
    metadata: Optional[Dict[str, Any]] = None 