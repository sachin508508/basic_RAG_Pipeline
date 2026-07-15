from langchain_chroma import Chroma
from config import CHROMA_DB
from embeddings import embed
from document_splitter import text_split

def vector_store():
    return Chroma().from_documents(documents=text_split(),
                                 embedding=embed(),
                                 persist_directory=CHROMA_DB)

if __name__ == "__main__":
    vector_store()
