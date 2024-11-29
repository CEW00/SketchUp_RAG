# Load the content of each file into RAW_KNOWLEDGE_BASE
import pdfplumber
from langchain.docstore.document import Document as LangchainDocument  
from langchain.docstore.document import Document as LangchainDocument
from langchain.text_splitter import RecursiveCharacterTextSplitter
from transformers import AutoTokenizer
import os
from typing import Optional, List
from config_models import embedding_model_name, embedding_model, current_dir, faiss_index_path, chunk_size, tokenizer, chunk_overlap
from config_scraping_URLs import file_paths
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores.faiss import FAISS  # Updated import for FAISS
from langchain_community.vectorstores.utils import DistanceStrategy
import json
# Initialize an empty list for the raw knowledge base
RAW_KNOWLEDGE_BASE = []

# Load the content of each file into RAW_KNOWLEDGE_BASE
for file_path in file_paths:
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist. Please check the path.")

    # Load content depending on file type
    if file_path.endswith('.json'):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            # Directly iterate over the list
            for item in data:
                # Ensure the item is a dictionary and contains 'content'
                if isinstance(item, dict):
                    content = item.get("content", [])

                    # Only process if 'content' exists
                    if content:
                        for content_item in content:
                            # Extract header and paragraphs safely
                            header = content_item.get("header", "")
                            paragraphs = content_item.get("paragraphs", [])

                            # Process the content if both header and paragraphs are available
                            if header and paragraphs:
                                document = LangchainDocument(page_content=" ".join(paragraphs))
                                RAW_KNOWLEDGE_BASE.append(document)

    elif file_path.endswith('.pdf'):
        # For PDF files using pdfplumber
        content = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                content += page.extract_text()  # Extract text from each page
        
        document = LangchainDocument(page_content=content)
        RAW_KNOWLEDGE_BASE.append(document)

    else:
        raise ValueError(f"Unsupported file format: {file_path}")


# Define the document splitting function
def split_documents(
    chunk_size: int,
    knowledge_base: List[LangchainDocument],
    tokenizer_name: str = embedding_model_name,
) -> List[LangchainDocument]:
    """
    Split documents into chunks of maximum size `chunk_size` tokens and return a list of documents.
    """
    text_splitter = RecursiveCharacterTextSplitter.from_huggingface_tokenizer(
        tokenizer,
        chunk_size=chunk_size,
        chunk_overlap = chunk_overlap,
        add_start_index=True,
        strip_whitespace=True
    )

    docs_processed = []
    for doc in knowledge_base:
        docs_processed += text_splitter.split_documents([doc])

    # Remove duplicates
    unique_texts = {}
    docs_processed_unique = []
    for doc in docs_processed:
        if doc.page_content not in unique_texts:  # Correct usage of 'page_content'
            unique_texts[doc.page_content] = True
            docs_processed_unique.append(doc)

    return docs_processed_unique

# Split documents into chunks
docs_processed = split_documents(
    chunk_size,  # We choose a chunk size adapted to our model
    RAW_KNOWLEDGE_BASE,
    tokenizer_name=embedding_model_name,
)

# Create the FAISS Knowledge Vector Database
KNOWLEDGE_VECTOR_DATABASE = FAISS.from_documents(
    docs_processed, embedding_model, distance_strategy=DistanceStrategy.COSINE
)

# Save the FAISS Knowledge Vector Database to a file
KNOWLEDGE_VECTOR_DATABASE.save_local(faiss_index_path)

print(f"FAISS knowledge vector database saved at: {faiss_index_path}")
