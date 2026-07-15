from langchain_chroma import Chroma
from config import CHROMA_DB
from embeddings import embed

def vector_load():
    return Chroma(
        embedding_function=embed(),
        persist_directory=CHROMA_DB
    )