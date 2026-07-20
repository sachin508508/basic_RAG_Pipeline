from load_vector_db import vector_load
from build_vector_db import vector_store
from config import CHROMA_DB
from pathlib import Path

def retrieve(top_k):
    db_path = Path(CHROMA_DB)
    if not db_path.exists() or not any(db_path.iterdir()):
        vector_store()
    db = vector_load()
    retrieved_chunks = db.as_retriever(search_kwargs={"k":top_k})
    return retrieved_chunks

def format_chunk(chunks):
    return "\n\n".join(chunk.page_content for chunk in chunks)