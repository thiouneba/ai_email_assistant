from pathlib import Path
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from app.embeddings import build_embeddings

base = Path("data/knowledge_base")
texts = []
for p in base.glob("*.txt"):
    texts.append(Document(page_content=p.read_text(encoding="utf-8"), metadata={"source": p.name}))

if texts:
    store = FAISS.from_documents(texts, build_embeddings())
    out = Path("output/index")
    out.mkdir(parents=True, exist_ok=True)
    store.save_local(str(out))
