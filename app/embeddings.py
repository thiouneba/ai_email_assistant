from langchain_mistralai import MistralAIEmbeddings
from .config import settings

def build_embeddings():
    return MistralAIEmbeddings(
        mistral_api_key=settings.mistral_api_key,
        model=settings.mistral_embedding_model,
    )
