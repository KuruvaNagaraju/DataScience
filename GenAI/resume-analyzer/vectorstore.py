import os
import shutil
import logging
from typing import List, Optional
from dotenv import load_dotenv

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma  # ✅ Updated import from langchain-chroma
from langchain_huggingface import HuggingFaceEmbeddings  # ✅ No change

# Load environment variables from .env
load_dotenv()

# Persistent directory for storing the vector database
PERSIST_DIR = "chroma_db"

# Read the embedding model name from the environment
EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME", "all-MiniLM-L6-v2")

# ----------------------------------------
# Configure logging
# ----------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] - %(message)s",
    handlers=[logging.FileHandler("vectorstore.log"), logging.StreamHandler()]
)


def create_vector_db(raw_docs: List) -> None:
    """
    Creates and persists a vector database from the provided raw document chunks.

    Args:
        raw_docs (List): List of raw documents extracted from the uploaded PDF files.
    """
    logging.info(f"Loaded {len(raw_docs)} pages from uploaded PDF")

    splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=50)
    texts = splitter.split_documents(raw_docs)
    logging.info(f"Generated {len(texts)} chunks from page-wise content")

    if not texts:
        logging.warning("No text chunks to embed. Exiting.")
        return

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    try:
        test_emb = embeddings.embed_documents([texts[0].page_content])
        logging.info(f"Sample embedding vector length: {len(test_emb[0])}")
    except Exception as e:
        logging.error(f"Embedding failed! {e}")
        return

    if os.path.exists(PERSIST_DIR):
        try:
            shutil.rmtree(PERSIST_DIR)
            logging.info(f"Deleted existing vector DB at {PERSIST_DIR}")
        except Exception as e:
            logging.error(f"Failed to delete existing vector DB at {PERSIST_DIR}. Error: {e}")
            return

    try:
        os.makedirs(PERSIST_DIR, exist_ok=True)
        logging.info(f"Created vector DB directory at {PERSIST_DIR}")
    except Exception as e:
        logging.error(f"Failed to create vector DB directory at {PERSIST_DIR}. Error: {e}")
        return

    # ✅ Updated creation method (no separate .persist() needed)
    try:
        vectordb = Chroma.from_documents(
            documents=texts,
            embedding=embeddings,
            persist_directory=PERSIST_DIR
        )
        logging.info("Vector DB created and persisted successfully.")
    except Exception as e:
        logging.error(f"Failed to create vector DB: {e}")



def load_vector_db() -> Optional[Chroma]:
    """
    Loads the vector database from the persistent directory.

    Returns:
        Optional[Chroma]: A Chroma vector store object loaded with the embeddings or None if failed.
    """
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    try:
        vectordb = Chroma(persist_directory=PERSIST_DIR, embedding_function=embeddings)
        logging.info(f"Loaded vector DB from {PERSIST_DIR}")
        return vectordb
    except ImportError as e:
        logging.error("Failed to import Chroma or chromadb. Did you install chromadb and langchain-chroma?")
        logging.exception(e)
    except Exception as e:
        logging.error("Failed to load vector DB.")
        logging.exception(e)

    return None
