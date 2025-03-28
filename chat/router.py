from fastapi import APIRouter, HTTPException
from .models import ChatMessage, ChatResponse
from .knowledge.zep import ZepService

router = APIRouter(prefix="/chat", tags=["chat"])

# Initialize services
zep_service = ZepService()

@router.post("", response_model=ChatResponse)
async def chat(message: ChatMessage):
    """
    Process a chat message using ZepAI knowledge graph.
    """
    try:
        result = await zep_service.process_query(
            query=message.message,
            user_id=message.user_id
        )

        return ChatResponse(
            response=result["response"],
            metadata=result["metadata"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 