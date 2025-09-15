from pydantic import BaseModel
from typing import List,Optional
from datetime import datetime


class IngestionResponse(BaseModel):
    """
    Response model for document ingestion API.

    Attributes:
        message (str): Status message for the ingestion operation.
        doc_ids (List[str]): List of document IDs created during ingestion.
    """
    message: str
    doc_ids: List[str]  


class DocumentChunkBase(BaseModel):
    """
    Base model representing a chunk of a document.

    Attributes:
        doc_id (str): Identifier of the original document.
        chunk_id (str): Unique identifier for this chunk.
        chunk_text_snippet (Optional[str]): Text snippet of the chunk. Can be None.
    """
    doc_id: str
    chunk_id: str
    chunk_text_snippet: Optional[str] = None
    

class DocumentChunkCreate(DocumentChunkBase):
    """
    Model used when creating a new document chunk.

    Inherits all fields from DocumentChunkBase.
    """
    pass  

class DocumentChunkResponse(DocumentChunkBase):
    """
    Model for returning document chunk details in API responses.

    Inherits all fields from DocumentChunkBase and adds:
        id (int): Database primary key for the chunk.
        upload_time (datetime): Timestamp when the chunk was uploaded.
    """
    id: int
    upload_time: datetime

    class Config:
        orm_mode = True 
