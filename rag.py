from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM

# Load PDF
loader = PyPDFLoader("sample.pdf")
documents = loader.load()

# Split documents into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

# Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create vector database
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings
)

# Create retriever
retriever = vectorstore.as_retriever()

# Load Ollama model
llm = OllamaLLM(model="llama3")

print("\nRAG Chatbot Ready!")
print("Type 'exit' to quit.\n")

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    # Retrieve relevant chunks
    retrieved_docs = retriever.invoke(query)

    # Combine retrieved text
    context = "\n".join([doc.page_content for doc in retrieved_docs])

    # Prompt
    prompt = f"""
    Answer the question using the context below.

    Context:
    {context}

    Question:
    {query}
    """

    # Generate response
    response = llm.invoke(prompt)

    print("\nBot:", response, "\n")