from langchain_chroma import Chroma
from config import CHROMA_DB
from embeddings import get_embedding_model

def vector_load():
    return Chroma(
        embedding_function=get_embedding_model(),
        persist_directory=CHROMA_DB
    )