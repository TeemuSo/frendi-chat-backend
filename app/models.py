from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Message(BaseModel):
    content: str
    timestamp: Optional[datetime] = None

class MessageResponse(BaseModel):
    id: str
    content: str
    timestamp: datetime 