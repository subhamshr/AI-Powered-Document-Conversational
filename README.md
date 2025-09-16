# 📚 RAG-Powered Backend System

This project provides a **backend system** to handle document ingestion, text extraction, embedding generation, and conversational retrieval using **RAG (Retrieval-Augmented Generation)**.  

It also includes:
- 🔄 Multi-turn conversational API with **chat memory**
- 🤖 Intelligent query answering with **context-aware retrieval**
- 📅 **Interview booking functionality**
- 🐳 Easy deployment with **Docker**

---

## ✨ Features
- **Document Ingestion**: Upload and process documents for downstream use
- **Text Extraction**: Clean extraction from structured/unstructured inputs
- **Embeddings Generation**: Vector representation of text for semantic search
- **RAG (Retrieval-Augmented Generation)**: Combine LLM power with external knowledge
- **Conversational API**: Multi-turn chat with memory persistence
- **Interview Booking**: Function calling support for scheduling interviews
- **Dockerized Deployment**: One command setup

---

## 🛠️ Tech Stack
- **Backend**: FastAPI (Python)
- **LLM Integration**: OpenAI API 
- **Vector Store**: Pinecone / Redis (for embeddings & retrieval)
- **Database**: PostgreSQL
- **Cache/Memory**: Redis
- **Containerization**: Docker & Docker Compose

---

## Getting Started

1. **Clone the repo**  
   ```bash
   git clone https://github.com/subhamshr/AI-Powered-Document-Conversational.git
   cd AI-Powered-Document-Conversational

2. **🔑 Environment Variables**

Create a `.env` file in the root directory with the following variables:

```env
# OpenAI API Key (for embedding & LLM calls)
OPENAI_API_KEY=your_openai_api_key_here

# Database connection string (PostgreSQL example)
DATABASE_URL=postgresql://user:password@db:5432/app_db

# Redis connection (for chat memory & caching)
REDIS_URL=redis://redis:6379

# Pinecone or other vector store API key (if using)
PINECONE_API_KEY=your_pinecone_api_key_here

# Pinecone environment
PINECONE_ENV=your_pinecone_environment_here


3. **🐳 Build & Run with Docker**

Use Docker Compose to build and start the application:

```bash
docker-compose up --build
