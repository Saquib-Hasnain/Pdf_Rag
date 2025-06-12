# 🧠 RAG PDF Chatbot using LangChain, OpenAI & Qdrant

This project is a working example of **Retrieval-Augmented Generation (RAG)** that lets you chat with any PDF 📄 using OpenAI's LLMs.

Instead of fine-tuning a model, we **store your PDF data in a vector database** and retrieve relevant chunks on-the-fly when a user asks a question.

---

## 📌 Features

✅ Chunk and index any PDF  
✅ Store vector embeddings in **Qdrant**  
✅ Ask natural language questions  
✅ Get contextual answers with page references  
✅ All in one Python script (`main.py`)

---

## ⚙️ How It Works

### Step-by-Step:

1. **Extract PDF content** and split into chunks  
2. **Generate embeddings** using `OpenAIEmbeddings`  
3. **Store** the vectors in `Qdrant` DB  
4. **User enters a query**
5. Query is embedded → relevant chunks fetched via semantic search  
6. LLM is prompted with those chunks as context  
7. Answer is generated 🔥

---

## 📂 Project Structure

├── main.py # All-in-one PDF index + chat script

├── nodejs.pdf # Your PDF file (rename or replace as needed)

├── .env # API key and environment configs

├── requirements.txt # All required Python dependencies

└── docker-compose.yml # Qdrant setup




---

## 🚀 Getting Started

###  Clone the Repo

```bash
git clone https://github.com/yourusername/rag-pdf-chatbot.git
cd rag-pdf-chatbot


