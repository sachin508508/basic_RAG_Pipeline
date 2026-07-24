from langchain_chroma import Chroma
from src.config import CHROMA_DB
from src.embeddings import get_embedding_model
from src.document_splitter import text_split

def vector_store() -> Chroma:
    return Chroma().from_documents(documents=text_split(),
                                 embedding=get_embedding_model(),
                                 persist_directory=CHROMA_DB)
