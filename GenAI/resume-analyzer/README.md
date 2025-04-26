# Candidate Resume Analyzer with Q&A

This application allows you to upload candidate resumes in PDF format and interact with them using a Retrieval-Augmented Generation (RAG) approach. It creates a vector database from the resumes, summarizes the content, and enables question-answering about the candidate. The app now also supports **re-ranking** of search results using a Cross-Encoder model for enhanced answer accuracy.

---

## 🚀 Features

- ✅ Upload and process multiple PDF resumes.
- ✅ Generate a semantic vector store using HuggingFace embeddings.
- ✅ Structured resume summarization.
- ✅ Ask freeform questions about candidates and retrieve relevant context.
- ✅ **Re-ranking of retrieved chunks using `cross-encoder/ms-marco-MiniLM-L12-v2`.**
- ✅ View reference text chunks used to generate answers.
- ✅ Chat history tracking.

---

## 🛠️ Tech Stack

| Component           | Technology |
|--------------------|------------|
| Web UI             | Streamlit  |
| Embeddings         | HuggingFace |
| Re-ranking         | Cross-Encoder (`sentence-transformers`) |
| Vector DB          | Chroma (`langchain-chroma`) |
| PDF Reading        | PyMuPDF |
| LLM Inference      | vLLM / Ollama |
| Framework          | LangChain |

---

## 🧪 Setup & Installation

### 1. Clone the repository

```bash
https://github.com/KuruvaNagaraju/DataScience.git
cd GenAI/resume-analyzer
```

### 2. Create and activate a virtual environment (recommended)

```bash
python -m venv resume_venv
source resume_venv/bin/activate  # Windows: resume_venv\Scripts\activate
```

### 3. Install required dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file at the root of your project:

```env
# API endpoints
VLLM_API_URL=http://localhost:8000/v1/chat/completions
OLLAMA_API_URL=http://localhost:11434/api/generate

# Model configurations
VLLM_API_KEY=<your_vllm_api_key>
VLLM_MODEL_NAME=ibm-granite/granite-3.2-8b-instruct
EMBEDDING_MODEL_NAME=all-MiniLM-L6-v2
RE_RANKER_MODEL=cross-encoder/ms-marco-MiniLM-L12-v2
OLLAMA_LLM_MODEL_NAME=granite3.3:8b
```

> 🔐 **Note:** Replace `<your_vllm_api_key>` with your actual VLLM API key.

### 5. Run the application

```bash
streamlit run app.py
```

---

## 🔁 Application Flow

1. **Resume Upload**  
   Upload one or more PDF resumes.

2. **Text Chunking & Embedding**  
   Resumes are split and embedded using `HuggingFaceEmbeddings`.

3. **Vector DB Creation**  
   Stored in Chroma using `langchain-chroma`.

4. **Re-ranking (Optional)**  
   Retrieved documents are re-ranked using a **cross-encoder** model for improved semantic matching.

5. **Question Answering**  
   Ask natural language questions. Responses are powered by RAG + LLM (vLLM/Ollama).

6. **Chat History**  
   Past Q&A is saved for reference and reuse.

---

## 📁 File Structure

```
.
├── app.py                  # Streamlit UI
├── file_handler.py         # Upload logic
├── llm_config.py           # LLM API setup
├── pdf_reader.py           # PDF extraction
├── rag_chain.py            # RAG logic with re-ranking
├── summary_chain.py        # Resume summarization
├── vectorstore.py          # Embedding & vector DB logic
├── requirements.txt        # Python dependencies
├── .env                    # Env variables
├── vllm_setup.md           # Guide for vLLM setup
├── ollama_setup.md         # Guide for Ollama setup
├── uploaded_docs/          # Uploaded files
└── chroma_db/              # Chroma vector DB
```

---

## 📌 Notes

- Add `.env` and `uploaded_docs/` to your `.gitignore`.
- Re-ranking improves result relevance, especially with longer documents.
- If you're only using text and not images, avoid using vision models in Ollama.
- Ensure `langchain-chroma` and `chromadb` are installed and updated for compatibility.

---

## 📚 Setup References

- For VLLM setup please refer: [vllm_setup.md](https://github.com/KuruvaNagaraju/DataScience/blob/master/GenAI/resume-analyzer/vllm_setup.md)
- For OLLAMA setup please refer: [ollama_setup.md](https://github.com/KuruvaNagaraju/DataScience/blob/master/GenAI/resume-analyzer/ollama_setup.md)

---

## 🙌 Acknowledgments

- [Hugging Face](https://huggingface.co) — Embedding & re-ranking models
- [Streamlit](https://streamlit.io) — UI development
- [LangChain](https://www.langchain.com) — Chaining LLMs and document loaders
- [ChromaDB](https://www.trychroma.com) — Lightweight vector storage
- [Ollama](https://ollama.com) / [vLLM](https://github.com/vllm-project/vllm) — Local LLM inference
