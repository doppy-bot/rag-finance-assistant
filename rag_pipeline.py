"""
rag_pipeline.py — RAG logic: retrieve relevant chunks, build prompt, call Ollama
"""

from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_community.vectorstores import FAISS

INDEX_PATH = "faiss_index"
MODEL_NAME = "llama3.2"

embeddings = OllamaEmbeddings(model=MODEL_NAME)
vectorstore = FAISS.load_local(INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
llm = OllamaLLM(model=MODEL_NAME)

def answer_question(question: str, k: int = 4) -> dict:
    docs = vectorstore.similarity_search(question, k=k)
    context = "\n\n".join([
        f"[Source: {d.metadata.get('source', 'unknown')}]\n{d.page_content}"
        for d in docs
    ])

    prompt = f"""You are an intelligent assistant with deep knowledge of Tarun Jena's data science projects.
Answer the question using ONLY the context provided below. Be specific, concise, and reference actual numbers or methods where available.
If the answer is not in the context, say "I don't have enough information about that."

CONTEXT:
{context}

QUESTION: {question}

ANSWER:"""

    response = llm.invoke(prompt)
    sources = list(set(d.metadata.get("source", "unknown") for d in docs))
    return {"answer": response, "sources": sources}
