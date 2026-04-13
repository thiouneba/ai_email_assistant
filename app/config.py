from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    mistral_api_key: str | None = os.getenv("MISTRAL_API_KEY")
    mistral_model: str = os.getenv("MISTRAL_MODEL", "mistral-large-latest")
    mistral_embedding_model: str = os.getenv("MISTRAL_EMBEDDING_MODEL", "mistral-embed")
    faiss_index_path: str = os.getenv("FAISS_INDEX_PATH", "output/index")

settings = Settings()
