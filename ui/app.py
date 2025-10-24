import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print("🔍 Current sys.path:", sys.path[:3])  # Just to verify
import streamlit as st
from modules.text_processor import extract_text, split_text
from modules.vector_store import create_vector_store
from modules.query_engine import answer_query

st.set_page_config(
    page_title="Multimodal AI System",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Sidebar ---
# --- Sidebar ---
with st.sidebar:
    st.title("ℹ️ Instructions")
    st.markdown("""
    1. Upload a file (PDF, DOCX, PPTX, TXT, MD, MP3, MP4)  
    2. Enter a question in natural language  
    3. Get instant answers powered by Gemini AI  
    """)
    st.markdown("---")

# --- Hero Section ---
st.markdown("<h1 style='text-align:center; color:#4B6CB7;'>🤖 Multimodal AI Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#6C757D;'>Upload documents or audio files and ask questions instantly!</p>", unsafe_allow_html=True)

# --- File Upload & Query Input ---
uploaded_file = st.file_uploader("📂 Upload your file", type=["pdf", "txt", "docx", "pptx", "md", "mp3", "mp4"])
query = st.text_input("💬 Ask a question", placeholder="Type your question here...")

# --- Main Processing ---
if uploaded_file and query:  # Removed youtube_link check
    try:
        with st.spinner("Extracting text..."):
            text = extract_text(uploaded_file)  # Simplified
        st.success("✅ Text extracted!")

        # ... rest of the code stays the same
        with st.spinner("Splitting text into chunks..."):
            chunks = split_text(text)
        st.info(f"📦 Text split into {len(chunks)} chunks.")

        with st.spinner("Creating knowledge base..."):
            vectorstore = create_vector_store(chunks)
        st.success("🗄 Knowledge base ready!")

        with st.spinner("Generating answer..."):
            answer = answer_query(vectorstore, query)

        # --- Answer Section ---
        st.markdown("### 🤖 Answer")
        st.markdown(
            """
            <style>
            .answer-box {
                background-color: #f8fafc;
                color: #1e293b;
                padding: 20px;
                border-radius: 12px;
                font-size: 16px;
                line-height: 1.6;
                border: 1px solid #e2e8f0;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                max-height: 400px;
                overflow-y: auto;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown(f'<div class="answer-box">{answer.replace("<", "&lt;").replace(">", "&gt;")}</div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Error: {e}")
        import traceback
        with st.expander("Show detailed error"):
            st.code(traceback.format_exc())

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#6C757D;'>Powered by Gemini AI + LangChain | Streamlit UI</p>", unsafe_allow_html=True)