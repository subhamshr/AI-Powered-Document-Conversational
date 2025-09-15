import os
from pinecone import Pinecone,ServerlessSpec
from app.core.config import settings

pc = Pinecone(api_key=settings.PINECONE_API_KEY)

if "rag-project-512" not in pc.list_indexes().names():
    pc.create_index(
        name="rag-project-512",
        dimension=1536,  
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index("rag-project-512")



