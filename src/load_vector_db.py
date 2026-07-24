from langchain_chroma import Chroma
from src.config import CHROMA_DB
from src.embeddings import get_embedding_model

def vector_load():
    return Chroma(
        embedding_function=get_embedding_model(),
        persist_directory=CHROMA_DB
    )