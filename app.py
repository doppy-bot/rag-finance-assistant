"""
app.py — Streamlit chat UI for the RAG assistant
Run: streamlit run app.py
"""

import streamlit as st
from pathlib import Path

# Page config
st.set_page_config(
    page_title="Tarun's Project Assistant",
    page_icon="🧠",
    layout="centered"
)

# Check index exists
if not Path("faiss_index").exists():
    st.error("Index not found. Run `python ingest.py` first.")
    st.stop()

# Lazy load pipeline
@st.cache_resource
def load_pipeline():
    from rag_pipeline import answer_question
    return answer_question

answer_question = load_pipeline()

# UI
st.title("🧠 Tarun's Project Assistant")
st.caption("Ask anything about Tarun's data science projects — Credit Risk, Fairness & Bias, Premier League Forecast, or his CV.")

# Suggested questions
st.markdown("**Try asking:**")
cols = st.columns(2)
suggestions = [
    "What was the key finding in the credit risk project?",
    "How was fairness measured in the income prediction model?",
    "What ML model was used for Premier League predictions?",
    "What technical skills does Tarun have?",
    "How did Tarun handle imbalanced classes?",
    "What is Tarun's highest academic qualification?"
]
for i, s in enumerate(suggestions):
    if cols[i % 2].button(s, key=f"sug_{i}"):
        st.session_state.setdefault("messages", [])
        st.session_state.messages.append({"role": "user", "content": s})

st.divider()

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("sources"):
            st.caption(f"📂 Sources: {', '.join(msg['sources'])}")

# Input
if prompt := st.chat_input("Ask about Tarun's projects..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = answer_question(prompt)
        st.markdown(result["answer"])
        st.caption(f"📂 Sources: {', '.join(result['sources'])}")
        st.session_state.messages.append({
            "role": "assistant",
            "content": result["answer"],
            "sources": result["sources"]
        })
