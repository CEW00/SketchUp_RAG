# config.py

######## Import
from langchain_huggingface import HuggingFaceEmbeddings  # Updated import path
import os
from langchain.vectorstores.faiss import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from transformers import AutoTokenizer
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch


######## SET DIRECTORIES
# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))



# directory for vector store that is created in embedded_vector_store.py
faiss_index_path = os.path.join(current_dir, "knowledge_vector_database.index")
print("Directories are set up.")



######## SET EMBEDDING MODEL 
# Embedding model configuration
embedding_model_name = "thenlper/gte-small"

# Load the embedding model used during the index creation
embedding_model = HuggingFaceEmbeddings(
    model_name=embedding_model_name,
    model_kwargs={"device": "cuda"},
    encode_kwargs={"normalize_embeddings": True},  # Set True for cosine similarity
)
print("Embedding model is set up.")



######## SET GENERATION MODEL 
# Embedding model configuration
# Model Configurations
READER_MODEL_NAME = "HuggingFaceH4/zephyr-7b-beta" # "Qwen/Qwen2.5-72B" #"dfurman/CalmeRys-78B-Orpo-v0.1"  #"tiiuae/falcon-7b" #"HuggingFaceH4/zephyr-7b-beta" "fblgit/TheBeagle-v2beta-32B-MGS"#
embedding_model_name_reader = "sentence-transformers/all-mpnet-base-v2"  # Example, modify as needed
chunk_size_reader = 512
chunk_overlap_reader = 50

# Load the 4-bit quantized causal LLM
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
)
generative_model = AutoModelForCausalLM.from_pretrained(
    READER_MODEL_NAME, quantization_config=bnb_config
)
tokenizer_reader = AutoTokenizer.from_pretrained(READER_MODEL_NAME)
READER_LLM = pipeline(
    model=generative_model,
    tokenizer=tokenizer_reader,
    task="text-generation",
    do_sample=True,
    temperature=0.2,
    repetition_penalty=1.1,
    return_full_text=False,
    max_new_tokens=500,
)



######## DOCUMENT SPLITTING 
tokenizer_name: str = embedding_model_name
tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

chunk_size = 512 #  maximum chunk_size during document splitting
chunk_overlap =int(chunk_size / 10)



