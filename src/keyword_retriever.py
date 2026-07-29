from src.document_splitter import text_split
from langchain_chroma import Chroma
from src.config import CHROMA_DB, TOP_K


def keyword_search(query, top_k=TOP_K):
    db = Chroma(persist_directory=CHROMA_DB)
    chunks = db._collection.get()["documents"]
    query_words = set(query.lower().split())
    ranked_chunks = []

    for chunk in chunks:
        score = 0
        chunk_words = set(chunk.lower().split())

        matched_words = list(query_words.intersection(chunk_words))

        for word in matched_words:
            score += chunk.lower().count(word)
        ranked_chunks.append({"score": score, "chunk": chunk})

    ranked_chunks = sorted(ranked_chunks, key=lambda x:x['score'], reverse=True)
    selected_chunks = ranked_chunks[:top_k] 
    selected_chunk = list(chunk['chunk'] for chunk in selected_chunks)
    return selected_chunk