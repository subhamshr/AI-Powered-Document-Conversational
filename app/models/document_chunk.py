from datetime import datetime
from sqlalchemy import Boolean, Column, String, Integer, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base



class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    doc_id: Mapped[str] = mapped_column(String(50), nullable=False)
    chunk_id: Mapped[str] = mapped_column(String(50), nullable=False)
    filename: Mapped[str] = mapped_column(String(255))
    upload_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    chunk_text_snippet: Mapped[str] = mapped_column(Text)
    
    
    