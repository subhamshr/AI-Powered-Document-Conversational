from fastapi import APIRouter, Depends, HTTPException
from app.schema.chat_schema import ChatResponse,ChatRequest
from app.services.chat_services import chat_with_rag
import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db


chat_router = APIRouter(
    prefix='/chatgpt',
    tags=['Chatgpt']
)

@chat_router.post("/query", response_model=ChatResponse,)
async def chat_endpoint(payload: ChatRequest,session: AsyncSession = Depends(get_db)):
    """
    Handle a user query and return an answer using the RAG system.

    This endpoint receives a user's question, retrieves relevant context
    from the document database using a Retrieval-Augmented Generation (RAG)
    approach, and returns a generated answer.

    Args:
        payload (ChatRequest): Request model containing the user's question.
        session (AsyncSession): Database session injected via dependency.

    Returns:
        ChatResponse: Response model containing the generated answer.
    """
    answer = await chat_with_rag(payload.question,session)
    return ChatResponse(answer=answer)

