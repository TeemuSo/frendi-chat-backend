from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
from .models import Message, MessageResponse

router = APIRouter(prefix="/api")

# Simple in-memory storage (replace with database in production)
messages = []

@router.get("/messages", response_model=List[MessageResponse])
async def get_messages():
    """Get all messages."""
    return messages

@router.post("/messages", response_model=MessageResponse)
async def create_message(message: Message):
    """Create a new message."""
    new_message = {
        "id": str(len(messages) + 1),
        "content": message.content,
        "timestamp": message.timestamp or datetime.now()
    }
    messages.append(new_message)
    return new_message

@router.get("/messages/{message_id}", response_model=MessageResponse)
async def get_message(message_id: str):
    """Get a specific message by ID."""
    for msg in messages:
        if msg["id"] == message_id:
            return msg
    raise HTTPException(status_code=404, detail="Message not found") 