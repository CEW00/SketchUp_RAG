

# Define RAG Prompt Template
prompt_in_chat_format = [
    {
        "role": "system",
        "content": """Use the information contained in the context,
give a comprehensive answer to the question.
Respond only to the question asked, response should be concise and relevant to the question.
If the answer cannot be deduced from the context, do not give an answer. If the user does not refer to the context engage in a conversation.""",
    },
    {
        "role": "user",
        "content": """Context:
{context}
---
Now here is the question you need to answer.

Question: {question}""",
    },
]

# Define RAG Prompt Template
prompt_in_chat_format2 = [
   {
    "role": "system",
    "content": """Answer the question using only the provided context. Follow these guidelines:
1. Provide a clear, concise, and relevant answer strictly based on the context.
2. Break the question down into simpler steps if applicable.
3. Avoid repeating or re-explaining details already stated in the context.
4. If the context does not provide enough information to answer, state that the answer cannot be deduced.
5. If the user asks something unrelated to the context, engage in a broader conversation instead.""",
},
{
    "role": "user",
    "content": """Context:
{context}
---
Question: {question}""",
}
]

# Define RAG Prompt Template
prompt_in_chat_format3 = [
   {
    "role": "system",
    "content": """Answer the question using only the provided context. Follow these guidelines:
1. Provide a clear, concise, and relevant answer strictly based on the context.
2. Break the question down into simpler steps if applicable.
3. Please explain every function needed that was not explained in the context.
4. If the context does not provide enough information to answer, state that the answer cannot be deduced.
5. If the user asks something unrelated to the context, engage in a broader conversation instead.""",
},
{
    "role": "user",
    "content": """Context:
{context}
---
Question: {question}""",
}
]

# Define RAG Prompt Template
prompt_in_chat_format4 = [
   {
    "role": "system",
    "content": """Answer the question using only the provided context. Follow these guidelines:
1. Provide a clear, concise, and relevant answer strictly based on the context.
2. Break the question down into simpler steps if applicable.
3. Please explain every function and the location where you can find it.
4. Please consider that the user is not able to import any existing models.
4. If the context does not provide enough information to answer, state that the answer cannot be deduced.
5. If the user asks something unrelated to the context, engage in a broader conversation instead.""",
},
{
    "role": "user",
    "content": """Context:
{context}
---
Question: {question}""",
}
]