from langchain_openai import OpenAIEmbeddings
import os

from app.core.config import settings
os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY
emb_model = OpenAIEmbeddings(model="text-embedding-3-small")

def get_embeddings(text: str):
    return emb_model.embed_query(text)
