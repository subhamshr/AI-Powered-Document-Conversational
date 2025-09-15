from fastapi import APIRouter, UploadFile, File, HTTPException
from langchain.text_splitter import RecursiveCharacterTextSplitter,CharacterTextSplitter
from app.utils.document_loader import load_pdf,load_txt
from app.utils.embeddings import get_embeddings
import uuid
from app.utils.pinecone_client import index
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.models.document_chunk import DocumentChunk
from app.schema.rag_schema import DocumentChunkBase

async def ingest_document(session: AsyncSession,file: UploadFile,strategy: str = "recursive") -> str:
    text=await file_reader(file)
    doc_id = str(uuid.uuid4())
    chunks = chunk_text(text)
    vectors_to_upsert = []
    chunk_ids = []
    for chunk in chunks:
        # If chunk is a Document object, use chunk.page_content instead
        text = chunk.page_content if hasattr(chunk, "page_content") else chunk
        chunk_id = str(uuid.uuid4())
        chunk_ids.append(chunk_id)

        embedding = get_embeddings(text)
        vectors_to_upsert.append((str(uuid.uuid4()), embedding, {"text": text}))
        db_chunk = DocumentChunk(
            doc_id=doc_id,
            chunk_id=chunk_id,
            filename=file.filename,
            chunk_text_snippet=text[:200]
        )
        session.add(db_chunk)


    await session.commit()
    index.upsert(vectors=vectors_to_upsert)
    return doc_id, chunk_ids

async def file_reader(file: UploadFile):
    file_bytes = await file.read()  # read bytes from UploadFile

    if file.filename.endswith(".txt"):
        content = await load_txt(file_bytes)  # await the async function
    elif file.filename.endswith(".pdf"):
        content = await load_pdf(file_bytes)
    else:
        raise HTTPException(status_code=400, detail="Only .pdf and .txt files are supported")
    return content
    
    
def chunk_text(text: str, strategy: str = "recursive") -> list:
    """
    Split text into chunks using the selected strategy.
    strategy: "recursive" or "semantic"
    """
    if strategy == "recursive":
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.create_documents([text])
        return chunks
    elif strategy == "semantic":
        splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200
        )
        return splitter.split_text(text)
    
    else:
        raise ValueError("Invalid chunking strategy. Choose 'recursive' or 'semantic'.")

