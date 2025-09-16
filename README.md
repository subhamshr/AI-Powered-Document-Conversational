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
# PostgreSQL database configuration
POSTGRES_USER=your_postgres_username
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_DB=your_database_name
POSTGRES_PORT=your_database_port
POSTGRES_HOST=your_database_host

# OpenAI API Key (for embeddings & LLM calls)
OPENAI_API_KEY=your_openai_api_key_here

# Redis configuration
REDIS_HOST=your_redis_host
REDIS_PORT=your_redis_port

# Pinecone API Key and environment
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_ENV=your_pinecone_environment_here


```
 
3. **🐳 Build & Run with Docker**

Use Docker Compose to build and start the application:

```bash
docker-compose up --build
