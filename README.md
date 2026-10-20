# B2G Policy Assistant using RAG

## Prerequisites
- Python 3.10 or newer
- Google Gemini API key

## 1. Extract the Project
Extract the project folder and open a terminal in the `code` directory.

## 2. Create a Virtual Environment
```bash
python -m venv .venv
```

Activate it on Windows:
```powershell
.venv\Scripts\activate
```

## 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 4. Configure the API Key
Create a `.env` file in the project root and add:

```text
GOOGLE_API_KEY=your_google_api_key
```

Replace the placeholder with your own API key.

## 5. Prepare the Knowledge Base
Ensure the six DOCX policy documents are inside the `knowledge_base` folder. Run:

```bash
python ingest.py
```

This loads the documents, splits them into chunks, generates embeddings, and stores them in ChromaDB.

## 6. Launch the Chatbot
Run:

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## Project Files
- `ingest.py` — Document ingestion, chunking, embedding, and vector storage.
- `retrieve.py` — Retrieves relevant document chunks.
- `main.py` — Generates answers using Gemini and retrieved context.
- `app.py` — Streamlit chatbot interface.
- `requirements.txt` — Python dependencies.
- `knowledge_base/` — Source policy documents.
- `chroma_db/` — Persistent vector database.

## Notes
- Run `python ingest.py` again when the source documents change.
- Keep the `.env` file and API key private.
- Internet access is required for Gemini API calls.
