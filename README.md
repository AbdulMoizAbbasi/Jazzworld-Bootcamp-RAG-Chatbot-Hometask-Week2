# B2G Policy Assistant Using RAG

A document-based chatbot that retrieves relevant information from six policy and guidance documents and generates answers using Google Gemini.

## Prerequisites
- Python 3.10 or newer
- A Google Gemini API key
- Internet connection

## 1. Clone the Repository

```bash
git clone https://github.com/AbdulMoizAbbasi/Jazzworld-Bootcamp-RAG-Chatbot-Hometask-Week2.git
cd YOUR_REPOSITORY_NAME
```

Run these commands from the directory containing `app.py`.

## 2. Create and Activate a Virtual Environment

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Environment Variables

Create a copy of `.env.example` named `.env` in the project root.

Add your own Google Gemini API key:

```text
GOOGLE_API_KEY=your_google_api_key_here
```

Replace the placeholder with a valid API key. Never share or commit your actual `.env` file.

## 5. Ingest the Knowledge Base

Ensure the six DOCX policy documents are present in the `knowledge_base` folder. Run:

```bash
python ingest.py
```

This loads the documents, splits them into chunks, generates embeddings, and stores them in ChromaDB.

Run ingestion again whenever the source documents need to be re-indexed.

## 6. Launch the Chatbot

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

`http://localhost:8501`

## Project Files

- `ingest.py` — Document loading, chunking, embedding, and vector storage.
- `retrieve.py` — Retrieves relevant document chunks.
- `main.py` — Generates answers using retrieved context and Gemini.
- `app.py` — Streamlit chatbot interface.
- `requirements.txt` — Python dependencies.
- `.env.example` — Template for required environment variables.
- `knowledge_base/` — Source policy documents.
- `chroma_db/` — Generated persistent vector database.

## Notes

- The evaluator must provide their own valid Gemini API key.
- Internet access is required for Gemini API calls.
- Keep API keys and credentials private.
- The chatbot answers based on the indexed documents and does not access live organizational systems.
