from dotenv import load_dotenv
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()

pdf_path=Path(__file__).parent / "nodejs.pdf"

loader = PyPDFLoader(file_path=pdf_path)
docs=loader.load() #Reads the PDF file and returns a list of documents

# Chunking
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
)

split_docs  = text_splitter.split_documents(documents=docs)  # Splits the documents into smaller chunks

# Vector Embedding
embedding_model= OpenAIEmbeddings(
    model="text-embedding-3-large",
   )

# Using [embedding_model] create embeddings of [split_docs] and store in DB

vector_store = QdrantVectorStore.from_documents(
    documents=split_docs,
    embedding=embedding_model,
    collection_name="learning_vectors",
    url="http://localhost:6333",  # Adjust the URL to your Qdrant instance
)

print("Indexing of Documments Done...")