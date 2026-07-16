from rag_pipeline import rag_chain

chain = rag_chain()
query = "Which two organisations' AI-as-a-Service offerings increase the accessibility of AI technologies for the smaller businesses and non-technical users?"
# query = "who is the father of east india company?"
response = chain.invoke(query)
print(response.text)