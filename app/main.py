from fastapi import FastAPI
from app.routers.ingestion_router import doucment_router
from app.routers.chat_router import chat_router

app = FastAPI()

app.include_router(doucment_router,prefix='/api')
app.include_router(chat_router,prefix='/api')

@app.get("/", tags=['Root'])
def read_root():
    return {"message": "Welcome to the FastAPI application with Redis!"}



