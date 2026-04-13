# Email Assistant RAG

A generic email understanding and routing assistant built with LangChain, Mistral AI, and FAISS.

## What it does
- Detects whether an email is a request, suggestion, claim, question, complaint, escalation, or other.
- Extracts the main topic and subtopic.
- Retrieves internal context from a knowledge base.
- Routes the email to the right expert or team.
- Falls back to human review when confidence is low.

## Why this structure
The project is designed to be reused by different organizations while staying focused on email understanding and assignment.

## Core flow
1. Ingest email content.
2. Classify intent and topic with structured output.
3. Retrieve relevant internal documents with FAISS.
4. Decide the best assignee.
5. Store the result for audit and improvement.

## Project structure
```text
app/
  config.py
  schemas.py
  prompts.py
  embeddings.py
  retriever.py
  router.py
  pipeline.py
  main.py
scripts/
  build_index.py
  evaluate.py
```

## Setup
```bash
pip install -e .
cp .env.example .env
```

## Run
```bash
uvicorn app.main:app --reload
```

## Input example
```json
{
  "subject": "Access issue for finance dashboard",
  "body": "Hi team, I need access to the finance dashboard for monthly reporting."
}
```

## Output example
```json
{
  "intent": "request",
  "topic": "IT access",
  "subtopic": "finance dashboard permissions",
  "confidence": 0.92,
  "assigned_team": "IT Support",
  "assigned_expert": "Alex Martin",
  "reasons": ["Mentions access", "Mentions finance dashboard"],
  "requires_human_review": false
}
```

## Customization
Replace the sample knowledge base with your organization rules, experts, and labeled examples.
