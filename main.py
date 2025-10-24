from modules.text_processor import extract_text, split_text
from modules.vector_store import create_vector_store
from modules.query_engine import answer_query

def main():
    file_path = input("Enter file path: ").strip().strip('"').strip("'")
    query = input("Enter your question: ")

    # Extract text from file
    text = extract_text(file_path)
    print("✅ Text extracted.")

    # Split text into chunks for embeddings
    chunks = split_text(text)
    print(f"✅ Text split into {len(chunks)} chunks.")

    # Create vector store from chunks
    vectorstore = create_vector_store(chunks)
    print("✅ Knowledge base created by Charan.")

    # Answer query using retrieved chunks
    answer = answer_query(vectorstore, query)
    print("\n🤖 Answer:\n", answer)

if __name__ == "__main__":
    main()
