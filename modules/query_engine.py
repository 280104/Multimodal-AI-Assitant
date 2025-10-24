import google.generativeai as genai

def answer_query(vectorstore, query):
    # Retrieve top 3 relevant chunks
    docs = vectorstore.similarity_search(query, k=3)
    context = "\n".join([d.page_content for d in docs])

    # Smarter prompt: tell the model to explain clearly, summarize, and reason if needed
    prompt = f"""
You are an expert AI assistant and domain specialist. 
Based on the context provided, give a clear, concise, and accurate answer to the question. 

- Explain concepts as if the user has never heard of them.  
- Summarize information; do not just copy text verbatim.  
- If the context is insufficient, reason carefully and provide a helpful, plausible answer.  
- Keep your response structured, using bullet points or short paragraphs if necessary.  
- Do not mention “contact xyz” or irrelevant lines from the document.  

Context:
{context}

Question:
{query}

Answer:

"""

    # Use a valid model from your list
    model_name = "models/gemini-2.5-flash"
    response = genai.GenerativeModel(model_name).generate_content(prompt)
    return response.text
