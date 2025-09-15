from pydantic import BaseModel
from typing import List,Optional
from datetime import datetime


class IngestionResponse(BaseModel):
    message: str
    doc_ids: List[str]  


class DocumentChunkBase(BaseModel):
    doc_id: str
    chunk_id: str
    chunk_text_snippet: Optional[str] = None
    

class DocumentChunkCreate(DocumentChunkBase):
    pass  

class DocumentChunkResponse(DocumentChunkBase):
    id: int
    upload_time: datetime

    class Config:
        orm_mode = True 
