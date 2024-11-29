import os
from typing import Optional, List, Tuple
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from langchain.docstore.document import Document as LangchainDocument
from langchain.vectorstores.faiss import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores.utils import DistanceStrategy

from config_models import embedding_model, current_dir, faiss_index_path
from config_models import tokenizer_reader, READER_LLM
from config_prompts import prompt_in_chat_format4

# Load the knowledge vector database
knowledge_vector_database = FAISS.load_local(faiss_index_path, embedding_model, allow_dangerous_deserialization=True)
print("FAISS knowledge vector database loaded successfully.")

# Define a reusable prompt template
RAG_PROMPT_TEMPLATE = tokenizer_reader.apply_chat_template(
    prompt_in_chat_format4, tokenize=False, add_generation_prompt=True
)

def refine_query_with_llm(
    question: str, 
    llm: pipeline, 
    conversation_history: Optional[List[str]] = None
) -> str:
    """
    Use the LLM to refine or decompose the user query into a more useful form,
    considering the prior conversation context if provided.
    """
    # Combine the conversation history into a single string
    context = ""
    if conversation_history:
        context = "Conversation History:\n"
        context += "\n".join([f"User: {entry}" for entry in conversation_history])
        context += "\n\n"

    # Prepare the refinement prompt
    refinement_prompt = (
        f"{context} A user that is learning to use the CAD program SketchUp is talking to you. The user might need advice or wants you to help them breaking down the steps required to model something from scratch. Please break down their query into the needed steps and functions that the user would need to look up. Be as precise as possible.   :\n\n"
        f"Query: {question}\n\n"
        f"Refined Query:"
    )

    # Generate the refined query
    refined_query = llm(refinement_prompt)[0]["generated_text"]
    return refined_query.strip()


def answer_with_rag(
    question: str,
    llm: pipeline,
    knowledge_index: FAISS,
    num_retrieved_docs: int = 30,
    num_docs_final: int = 5,
) -> Tuple[str, List[LangchainDocument]]:
    # Step 1: Refine the query
    refined_question = refine_query_with_llm(question, llm)

    # Step 2: Retrieve documents with FAISS
    relevant_docs = knowledge_index.similarity_search(query=refined_question, k=num_retrieved_docs)
    relevant_docs_text = [doc.page_content for doc in relevant_docs]

    # Step 3: Prepare context for the final prompt
    context = "\nExtracted documents:\n"
    context += "".join([f"Document {str(i)}:::\n" + doc for i, doc in enumerate(relevant_docs_text[:num_docs_final])])

    final_prompt = RAG_PROMPT_TEMPLATE.format(
        question=question, context=context
    )

    # Step 4: Generate the final answer with the Reader LLM
    answer = llm(final_prompt)[0]["generated_text"]
    return answer, relevant_docs[:num_docs_final]

# Chat loop for interacting with the model in the console
def chat_with_model():
    print("Welcome to the Refined RAG Chat!")
    print("Type 'exit' to end the conversation.")
    
    while True:
        # Ask user for input (question)
        question = input("You: ")

        # Allow user to exit the chat
        if question.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break

        # Get the answer using the modified RAG-based model
        answer, docs_used = answer_with_rag(question, READER_LLM, knowledge_vector_database)

        # Display the answer
        print("Model:", answer)

# Run the chat
chat_with_model()

