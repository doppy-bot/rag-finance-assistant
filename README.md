# 🧠 RAG Finance Assistant

A locally-running Retrieval-Augmented Generation (RAG) chatbot that answers questions about my data science projects using **Ollama (LLaMA 3.2)** and **FAISS** — with zero cloud dependency and zero API costs.

Built as a practical demonstration of GenAI application development applied to financial analytics, responsible AI, and predictive modelling.

---

## 💡 What It Does

Instead of asking an LLM to recall facts from training data, this system:

1. **Retrieves** the most relevant chunks from my project documents using semantic search (FAISS vector store)
2. **Augments** the prompt with that context
3. **Generates** a grounded, specific answer using a local LLM (LLaMA 3.2 via Ollama)

This means every answer is traceable back to a real source — no hallucination, no vague generalisations.

---

## 📂 Knowledge Base

The assistant is grounded in 4 real project documents:

| Document | Content |
|---|---|
| `Credit-Risk-Segmentation.md` | KMeans clustering on 51,336 customer records — High Risk cohort with 3x missed payment rate |
| `Fairness-Bias-Income-Prediction.md` | Logistic Regression + fairness metrics — 30% selection gap across demographic subgroups |
| `Premier League Prediction.md` | Random Forest + 5,000 Monte Carlo simulations using football-data.org API |
| `cv_tarun.pdf` | Full CV — skills, education, achievements |

---

## 🏗️ Architecture

```
User Question
      │
      ▼
 FAISS Vector Store  ◄──── Embedded project documents (OllamaEmbeddings)
      │
  Top-k Chunks
      │
      ▼
  Prompt Builder  ──► [Context + Question]
      │
      ▼
  LLaMA 3.2 (Ollama)
      │
      ▼
  Grounded Answer + Source Citations
```

---

## 🛠️ Tech Stack

| Component | Tool |
|---|---|
| LLM | LLaMA 3.2 via Ollama (fully local) |
| Embeddings | OllamaEmbeddings (llama3.2) |
| Vector Store | FAISS (Facebook AI Similarity Search) |
| Orchestration | LangChain |
| UI | Streamlit |
| Document Loaders | LangChain TextLoader + PyMuPDF |

---

## 🚀 How to Run

### Prerequisites
- [Ollama](https://ollama.com) installed and running
- Python 3.9+

### Setup

```bash
# 1. Clone the repo
git clone https://github.com/doppy-bot/rag-finance-assistant.git
cd rag-finance-assistant

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Pull the LLM model
ollama pull llama3.2

# 5. Build the FAISS index (run once)
python ingest.py

# 6. Launch the app
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## 💬 Example Questions

- *"What was the key finding in the credit risk project?"*
- *"How was fairness measured in the income prediction model?"*
- *"What ML model was used for Premier League predictions?"*
- *"How did Tarun handle imbalanced classes?"*
- *"What technical skills does Tarun have?"*

---

## 🔗 Why This Is Relevant to Financial Services AI

American Express and similar firms are actively building:
- **Conversational analytics** — querying internal reports and model outputs via natural language
- **Automated insights** — surfacing findings from analytical pipelines without manual reporting
- **Next-best-action decisioning** — grounding LLM recommendations in real data

This project demonstrates exactly that pattern — a RAG pipeline grounded in credit risk, fairness evaluation, and predictive modelling outputs.

---

## 👤 Author

**Tarun Jena**
MSc Business Analytics & Decision Science — University of Leeds
[LinkedIn](https://linkedin.com/in/tarun-jena07) | [GitHub](https://github.com/doppy-bot)
