"""
Module: pdf_reader

This module provides a utility function to load PDF documents page-wise using PyMuPDF (fitz)
and convert each page into LangChain-compatible `Document` objects.
"""

import os
import logging
import fitz  # PyMuPDF
from typing import List
from langchain.schema import Document

# ----------------------------------------
# Configure Logging
# ----------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[logging.FileHandler("pdf_reader.log"), logging.StreamHandler()]
)


def load_pdf_documents_pagewise(file_path: str) -> List[Document]:
    """
    Loads a PDF document and splits it page by page into LangChain Document objects.

    Args:
        file_path (str): Path to the PDF file to be processed.

    Returns:
        List[Document]: A list of LangChain Document objects, each representing a page.
    """
    docs = []

    try:
        # Extract just the filename for metadata
        filename = os.path.basename(file_path)
        logging.info(f"Opening PDF file: {filename}")

        # Load the document using PyMuPDF
        doc = fitz.open(file_path)

        # Iterate through each page
        for i, page in enumerate(doc):
            text = page.get_text().strip()

            if text:
                # Add page text and metadata as LangChain Document
                docs.append(
                    Document(
                        page_content=text,
                        metadata={"source": filename, "page": i + 1}
                    )
                )
            else:
                logging.warning(f"Page {i + 1} in {filename} is empty or unreadable.")

        logging.info(f"Successfully loaded {len(docs)} pages from {filename}.")

    except Exception as e:
        logging.exception(f"Failed to load PDF {file_path}: {e}")

    return docs
