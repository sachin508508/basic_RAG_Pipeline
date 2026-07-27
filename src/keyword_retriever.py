from document_splitter import text_split

chunks = text_split()
query = "contributor density ratio"

query_words = set(query.lower().split())
ranked_chunks = []

for chunk in chunks:
    score = 0
    chunk_words = set(chunk.page_content.lower().split())

    matched_words = list(query_words.intersection(chunk_words))

    for word in matched_words:
        score += chunk.page_content.lower().count(word)
    ranked_chunks.append({"score": score, "chunk": chunk.page_content})

ranked_chunks = sorted(ranked_chunks, key=lambda x:x['score'], reverse=True)

print(ranked_chunks[:3])

    


