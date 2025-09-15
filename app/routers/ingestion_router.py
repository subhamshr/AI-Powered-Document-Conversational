from fastapi import APIRouter, UploadFile, File, HTTPException,Query,Depends
from app.schema.rag_schema import IngestionResponse
from app.utils.document_loader import load_pdf,load_txt
from app.services.ingestion_service import ingest_document
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db



doucment_router=APIRouter()
@doucment_router.post("/upload")

async def upload_document(file: UploadFile = File(...),db: AsyncSession = Depends(get_db),strategy: str = Query("recursive", description="Chunking strategy: recursive or semantic")
):
    """
    Upload a document and process it into chunks for the RAG system.

    This endpoint accepts a PDF or TXT file, splits it into chunks based on the
    selected strategy, generates embeddings, and stores them in the database.

    Args:
        file (UploadFile): The document file to upload.
        db (AsyncSession): Database session injected via dependency.
        strategy (str): Chunking strategy, either 'recursive' or 'semantic'. Defaults to 'recursive'.
    """
    try:
        doc_id, chunk_ids = await ingest_document(session=db, file=file, strategy=strategy)  # returns list of tuples (id, embedding, metadata)
    
        return {"doc_id": doc_id, "chunk_ids": chunk_ids, "message": "Ingestion successful"}

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ingestion failed: {str(e)}")

