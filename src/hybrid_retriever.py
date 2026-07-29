from src.chunk_retriever import retrieve
from src.keyword_retriever import keyword_search
from src.config import TOP_K

def hybrid(query, top_k=TOP_K):
    keyword_chunk = keyword_search(query=query)
    vector_chunk = retrieve(top_k=top_k).invoke(query)
    vector_chunks = list(chunk.page_content for chunk in vector_chunk)
    hybrid_chunk = list(set(vector_chunks).union(set(keyword_chunk)))
    final_chunk: str = "\n\n".join(hybrid_chunk)
    return final_chunk
