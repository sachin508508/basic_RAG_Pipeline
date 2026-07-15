from chunk_retriever import retrieve

retriver = retrieve() 
query = "content generation"
chunks = retriver.invoke(query)

print ("\n\n".join(chunk.page_content for chunk in chunks))