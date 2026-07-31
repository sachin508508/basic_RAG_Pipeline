from src.chunk_retriever import retrieve
from src.keyword_retriever import keyword_search
from src.config import TOP_K
from langchain_core.runnables import RunnableLambda

def hybrid(top_k=TOP_K):
    def hybrid_search(query):
        keyword_chunk = keyword_search(query=query)
        vector_chunk = retrieve(top_k=top_k).invoke(query)
        vector_chunks = list(chunk.page_content for chunk in vector_chunk)
        hybrid_chunk = list(set(vector_chunks).union(set(keyword_chunk)))
        final_chunk: str = "\n\n".join(hybrid_chunk)
        print(f"{'--'*50}\n\nContext: \n\t{final_chunk}\n\n{'--'*50}")
        return final_chunk
    return RunnableLambda(hybrid_search)