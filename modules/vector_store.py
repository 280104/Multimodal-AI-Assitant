from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def create_vector_store(docs, persist_directory="db"):
    """
    Creates a Chroma vector store from a list of text chunks.
    """
    model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_texts(docs, embedding=model, persist_directory=persist_directory)
    return vectorstore
