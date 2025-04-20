import os
import logging
from typing import Union, List
from pdf_reader import load_pdf_documents_pagewise
from langchain.schema import Document  # Make sure to install langchain if not already

# ----------------------------------------
# Configure logging
# ----------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[logging.FileHandler("file_handler.log"), logging.StreamHandler()]
)

def save_and_load_pdf_pagewise(
    uploaded_file: Union["UploadedFile", List["UploadedFile"]],
    doc_path: str = "uploaded_docs"
) -> List[Document]:
    """
    Saves uploaded PDF files to disk and loads them page-by-page.

    Args:
        uploaded_file (Union[UploadedFile, List[UploadedFile]]): 
            A single or list of Streamlit uploaded file objects.
        doc_path (str): 
            Directory where the uploaded files will be saved.

    Returns:
        List[Document]: 
            A list of LangChain Document objects representing each page.
    """
    try:
        # Ensure target directory exists
        os.makedirs(doc_path, exist_ok=True)
        logging.info(f"Saving uploaded PDFs to directory: {doc_path}")

        raw_docs = []

        # Handle multiple file uploads
        if isinstance(uploaded_file, list):
            for file in uploaded_file:
                file_path = os.path.join(doc_path, file.name)
                with open(file_path, "wb") as f:
                    f.write(file.getbuffer())
                logging.info(f"Saved file: {file_path}")

                docs = load_pdf_documents_pagewise(file_path)
                raw_docs.extend(docs)
                logging.info(f"Loaded {len(docs)} pages from: {file.name}")

        else:
            # Handle single file upload
            file_path = os.path.join(doc_path, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            logging.info(f"Saved file: {file_path}")

            raw_docs = load_pdf_documents_pagewise(file_path)
            logging.info(f"Loaded {len(raw_docs)} pages from: {uploaded_file.name}")

        return raw_docs

    except Exception as e:
        logging.error(f"Error in save_and_load_pdf_pagewise: {e}")
        raise RuntimeError("Failed to process uploaded PDF file(s).") from e
