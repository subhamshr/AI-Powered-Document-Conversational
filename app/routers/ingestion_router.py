from fastapi import APIRouter, UploadFile, File, HTTPException,Query,Depends
from app.schema.rag_schema import IngestionResponse
from app.utils.document_loader import load_pdf,load_txt
from app.services.ingestion_service import ingest_document
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db



doucment_router=APIRouter()
# , response_model=IngestionResponse
@doucment_router.post("/upload")
async def upload_document(file: UploadFile = File(...),db: AsyncSession = Depends(get_db),strategy: str = Query("recursive", description="Chunking strategy: recursive or semantic")
):
    try:
        doc_id, chunk_ids = await ingest_document(session=db, file=file, strategy=strategy)  # returns list of tuples (id, embedding, metadata)
    
        return {"doc_id": doc_id, "chunk_ids": chunk_ids, "message": "Ingestion successful"}

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ingestion failed: {str(e)}")

