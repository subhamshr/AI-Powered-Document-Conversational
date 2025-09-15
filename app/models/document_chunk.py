from datetime import datetime
from sqlalchemy import Boolean, Column, String, Integer, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base



class DocumentChunk(Base):
    """
    SQLAlchemy ORM model for storing chunks of documents.

    Each document can be split into multiple chunks for processing
    in a Retrieval-Augmented Generation (RAG) system or other NLP tasks.

    Attributes:
        id (int): Primary key, auto-incremented.
        doc_id (str): Identifier of the original document.
        chunk_id (str): Unique identifier for this chunk.
        filename (str): Name of the original uploaded file.
        upload_time (datetime): Timestamp when the chunk was created.
        chunk_text_snippet (str): Text content of the chunk.
    """
    __tablename__ = "document_chunks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    doc_id: Mapped[str] = mapped_column(String(50), nullable=False)
    chunk_id: Mapped[str] = mapped_column(String(50), nullable=False)
    filename: Mapped[str] = mapped_column(String(255))
    upload_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    chunk_text_snippet: Mapped[str] = mapped_column(Text)
    
    
    