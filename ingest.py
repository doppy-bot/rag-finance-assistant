"""
ingest.py — Loads .md, .txt, .pdf files from data/, chunks them, builds FAISS index
Run once: python ingest.py
"""

from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

DATA_DIR = Path("data")
INDEX_PATH = Path("faiss_index")

def load_documents():
    docs = []
    # Load .txt and .md files
    for f in list(DATA_DIR.glob("*.txt")) + list(DATA_DIR.glob("*.md")):
        loader = TextLoader(str(f), encoding="utf-8")
        loaded = loader.load()
        for doc in loaded:
            doc.metadata["source"] = f.name
        docs.extend(loaded)
        print(f"  Loaded: {f.name} ({len(loaded[0].page_content)} chars)")
    # Load .pdf files
    try:
        from langchain_community.document_loaders import PyMuPDFLoader
        for f in DATA_DIR.glob("*.pdf"):
            loader = PyMuPDFLoader(str(f))
            loaded = loader.load()
            for doc in loaded:
                doc.metadata["source"] = f.name
            docs.extend(loaded)
            print(f"  Loaded PDF: {f.name} ({len(loaded)} pages)")
    except Exception as e:
        print(f"  PDF loading skipped: {e}")
    return docs

def build_index():
    print("Loading documents...")
    docs = load_documents()

    if not docs:
        print("ERROR: No documents found in data/ folder!")
        return

    print("Splitting into chunks...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    print(f"  {len(chunks)} chunks created")

    print("Building embeddings via Ollama (may take ~1 min)...")
    embeddings = OllamaEmbeddings(model="llama3.2")

    print("Building FAISS index...")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(str(INDEX_PATH))
    print(f"Index saved to {INDEX_PATH}/")

if __name__ == "__main__":
    build_index()
    print("\nDone! Now run: streamlit run app.py")
