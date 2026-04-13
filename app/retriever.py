from pathlib import Path
from langchain_community.vectorstores import FAISS
from .embeddings import build_embeddings
from .config import settings


def load_vectorstore():
    path = Path(settings.faiss_index_path)
    if not path.exists():
        return None
    return FAISS.load_local(str(path), build_embeddings(), allow_dangerous_deserialization=True)


def get_retriever(k: int = 4):
    store = load_vectorstore()
    if store is None:
        return None
    return store.as_retriever(search_kwargs={"k": k})
