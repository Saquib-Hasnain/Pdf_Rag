from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI

load_dotenv()

client = OpenAI()

# Load embedding model
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

# Load existing Qdrant collection
vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_vectors",
    embedding=embedding_model
)

# Start chat loop
message_history = []

print("🤖: Ask your questions from the document (type 'exit' to quit)\n")

while True:
    user_input = input("> ").strip()
    if user_input.lower() in ["exit", "quit"]:
        print("🤖: Goodbye!")
        break

    # Get relevant context from vector DB
    search_results = vector_db.similarity_search(query=user_input)

    context = "\n\n\n".join([
        f"Page Content: {r.page_content}\nPage Number: {r.metadata['page_label']}\nFile Location: {r.metadata['source']}"
        for r in search_results
    ])

    system_prompt = f"""
You are a helpful AI assistant that answers user queries based only on the context below,
which is retrieved from a PDF file. Always guide the user by suggesting the relevant page number.

Context:
{context}
    """

    # Full message list (system + chat history + new user query)
    messages = [{"role": "system", "content": system_prompt}] + message_history + [
        {"role": "user", "content": user_input}
    ]

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=messages
    )

    reply = response.choices[0].message.content.strip()

    # Display answer
    print(f"\n🤖: {reply}\n")

    # Update chat history
    message_history.append({"role": "user", "content": user_input})
    message_history.append({"role": "assistant", "content": reply})
