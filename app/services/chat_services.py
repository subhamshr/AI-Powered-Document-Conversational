from app.utils.pinecone_client import index
from langchain_openai import ChatOpenAI,OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate
from app.utils.embeddings import get_embeddings
from langchain.agents import initialize_agent, Tool, AgentType
import uuid
from typing import Optional
from app.services.redis_service import get_chat_history,append_chat_history
import json
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.booking_services import create_booking
from openai import OpenAI
from app.core.config import settings
from app.schema.booking_schema import BookingCreate



client = OpenAI(api_key=settings.OPENAI_API_KEY)

tools = [
    {
        "type": "function",
        "name": "book_interview",
        "description": "Schedule an interview booking with user details",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The full name of the person booking the interview"
                },
                "email": {
                    "type": "string",
                    "description": "The email address of the person booking the interview"
                },
                "date": {
                    "type": "string",
                    "description": "The date of the interview in YYYY-MM-DD format"
                },
                "time": {
                    "type": "string",
                    "description": "The time of the interview in HH:MM"
                }
            },
            "required": ["name", "email", "date", "time"]
        }
    }
]


client = OpenAI(api_key=settings.OPENAI_API_KEY)

async def chat_with_rag(question: str, session: AsyncSession):
    """
    Process a user's question using Retrieval-Augmented Generation (RAG) and handle booking requests.

    Steps:
        1. Retrieve conversation history from Redis.
        2. Retrieve relevant document context using Pinecone embeddings.
        3. Construct a prompt incorporating context, history, and the user's question.
        4. Call the OpenAI GPT-4o-mini model with tools for possible function execution.
        5. If a function call to book an interview is returned and all required fields are present, create the booking.
        6. Append user question and assistant answer to chat history.

    Args:
        question (str): User's question or request.
        session (AsyncSession): Async database session for booking creation.

    Returns:
        str: The assistant's answer or confirmation of booking.
    """

    session_id = str(uuid.uuid4())

    history =  get_chat_history(session_id)
    history_text = "\n".join(f"{m['role']}: {m['content']}" for m in history)

    query_embedding = get_embeddings(question)
    results = index.query(vector=query_embedding, top_k=3, include_metadata=True)
    retrieved_text = "\n\n".join(match['metadata']['text'] for match in results['matches'])

    prompt = f"""
You are a helpful assistant. 
- Use ONLY the given context to answer user questions.  
- If the user wants to book an interview, do NOT immediately generate a function call if details are missing.  
- If required fields (name, email, date, time) are not provided, politely ask the user to provide them.  
- Only when all required fields are present, generate the function call.
    Context: {retrieved_text}
    History:{history}
    Question: {question}
    """

    response = client.responses.create(
        model="gpt-4o-mini",
        tools=tools,  
        input=[{"role": "user", "content": prompt}],
        
    )

    for item in response.output:
        if item.type == "function_call" and item.name == "book_interview":
            function_args = json.loads(item.arguments)
            await create_booking(session, BookingCreate(**function_args))
            return "Booking is successful"

    answer = response.output_text

    append_chat_history(session_id, {"role": "user", "content": question})
    append_chat_history(session_id, {"role": "assistant", "content": answer})

    return answer

