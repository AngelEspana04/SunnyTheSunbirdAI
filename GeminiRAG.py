import google.generativeai as genai
import chromadb

# -------------------------------
# 1. Configure Gemini API Key
# -------------------------------
genai.configure(api_key="YOUR OWN API KEY")

# Initialize the Gemini model
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# -------------------------------
# 2. Connect to ChromaDB
# -------------------------------
client = chromadb.PersistentClient(path="/Users/elmer/Desktop/VectorDB/chroma_db")
collection = client.get_collection(name="university")

# -------------------------------
# 3. User Input Loop
# -------------------------------
while True:
    query = input("\nAsk a question about the university (or type 'exit' to quit): ").strip()
    
    if query.lower() == 'exit':
        print("Goodbye!")
        break

    # Perform semantic search
    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    # Handle case where no documents were found
    if not results['documents'] or not results['documents'][0]:
        print("No relevant documents found in the database.")
        continue

    # Flatten and format documents
    retrieved_docs = [doc for sublist in results['documents'] for doc in sublist]
    context = "\n---\n".join(retrieved_docs)

    # Build the prompt
    prompt = f"""
                You are a helpful, friendly university assistant named FPUBot. Respond conversationally and informatively.

                Here’s some information you can use:
                {context}

                Now, a user asked you this:
                "{query}"

                Respond like you're chatting with them. Be warm, clear, and friendly.
            """

    # Generate and display response
    try:
        response = model.generate_content(prompt)
        print("\nGemini Response:\n", response.text)
    except Exception as e:
        print("Error generating response:", e)
