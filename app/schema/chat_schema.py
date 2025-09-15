from pydantic import BaseModel
from typing import List, Optional
from typing import Union, Dict,Any


class ChatRequest(BaseModel):
    """
    Pydantic model representing a user's query to the ChatGPT RAG system.

    Attributes:
        question (str): The user's question or input text for the AI.
    """
    question: str

class ChatResponse(BaseModel):
    """
    Pydantic model representing the AI's response to a user's query.

    Attributes:
        answer (str): Generated answer from the RAG system.
    """
    answer: str




