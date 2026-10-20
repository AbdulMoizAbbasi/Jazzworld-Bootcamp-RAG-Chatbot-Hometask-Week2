
from pathlib import Path

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
VECTOR_DB_DIR = BASE_DIR / "chroma_db"

COLLECTION_NAME = "jazz_b2g_policies"


def get_retriever():
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        output_dimensionality=768,
    )

    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=str(VECTOR_DB_DIR),
    )

    return vector_store.as_retriever(
        search_kwargs={"k": 3}
    )


def retrieve_documents(question):
    retriever = get_retriever()
    results = retriever.invoke(question)

    return results


if __name__ == "__main__":
    question = input("Ask a question about B2G policies: ")

    results = retrieve_documents(question)

    if not results:
        print("No relevant documents found.")
    else:
        for i, document in enumerate(results, start=1):
            print(f"\n--- Result {i} ---")
            print(f"Source: {document.metadata.get('source', 'Unknown')}")
            print(document.page_content)
