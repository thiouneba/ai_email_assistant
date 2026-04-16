# 📧 Email Assistant — Intelligent RAG Routing System

> A production-ready **email understanding and routing agent** built with **LangChain + Mistral AI + FAISS** that classifies, enriches, and assigns emails to the right team using structured reasoning and retrieval.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/LangChain-0.3-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white"/>
  <img src="https://img.shields.io/badge/Mistral-AI-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/FAISS-Vector_Store-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/FastAPI-API-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
</p>

---

## 🧠 What is this?

I built this project as a real-world example of how **AI systems can automate business workflows**, specifically around one of the most common pain points: **email triage and routing**.

This assistant can:
- Automatically **classify email intent** (request, complaint, escalation, etc.)
- Extract **topic and subtopic** with structured outputs
- Use **RAG (Retrieval-Augmented Generation)** to enrich decisions with internal knowledge
- **Assign emails** to the most relevant team or expert
- Provide **explanations** for decisions (auditability)
- Trigger **human review fallback** when confidence is low

The system is designed to be **organization-agnostic** — plug in your own knowledge base, experts, and rules.

---

## 🏗️ Architecture

```
email-assistant/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── schemas.py
│   ├── prompts.py
│   ├── embeddings.py
│   ├── retriever.py
│   ├── router.py
│   └── pipeline.py
│
├── scripts/
│   ├── build_index.py
│   └── evaluate.py
│
├── data/
├── knowledge_base/
│
└── pyproject.toml
```

---

## 🛠️ Capabilities

| Capability | Description |
|------------|-------------|
| 🧠 intent_classification | Detects request, complaint, escalation |
| 🏷️ topic_extraction | Identifies topic and subtopic |
| 📚 rag_retrieval | Fetches internal knowledge |
| 🧭 routing_engine | Assigns team and expert |
| 📊 confidence_scoring | Measures decision confidence |
| ⚠️ human_fallback | Flags uncertain cases |

---

## 🚀 Quick Start

```bash
pip install -e .
cp .env.example .env
python scripts/build_index.py
uvicorn app.main:app --reload
```

---

## 🔌 API Example

### Request

```json
{
  "subject": "Access issue for finance dashboard",
  "body": "Hi team, I need access to the finance dashboard for monthly reporting."
}
```

### Response

```json
{
  "intent": "request",
  "topic": "IT access",
  "subtopic": "finance dashboard permissions",
  "confidence": 0.92,
  "assigned_team": "IT Support",
  "assigned_expert": "Bassirou T.",
  "reasons": ["Mentions access", "Mentions finance dashboard"],
  "requires_human_review": false
}
```

---

## 🔄 Processing Flow

1. Ingest email  
2. Classify intent  
3. Retrieve knowledge  
4. Route to team  
5. Score confidence  
6. Fallback if needed  

---

## 👤 Author

Bassirou — AI Engineer

---

## 📄 License

MIT
