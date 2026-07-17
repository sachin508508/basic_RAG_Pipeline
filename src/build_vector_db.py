from langchain_chroma import Chroma
from config import CHROMA_DB
from embeddings import get_embedding_model
from document_splitter import text_split

def vector_store():
    return Chroma().from_documents(documents=text_split(),
                                 embedding=get_embedding_model(),
                                 persist_directory=CHROMA_DB)
