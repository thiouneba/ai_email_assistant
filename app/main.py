from fastapi import FastAPI
from .schemas import EmailInput
from .pipeline import classify_email

app = FastAPI(title="Email Assistant RAG")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/classify")
def classify(email: EmailInput):
    decision = classify_email(f"{email.subject}
{email.body}")
    return decision.model_dump()
