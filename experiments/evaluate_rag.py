import json
from src.rag_pipeline import rag_chain
from langchain_core.output_parsers import StrOutputParser

chain = rag_chain() | StrOutputParser()


with open('./experiments/evaluation_questions.json', 'r') as doc:
    data = json.load(doc)

for query in data:
    print(f"Loading query {query['id']} out of 10.")
    response = chain.invoke(query['question'])
    query['response'] = response

with open('./experiments/response.json', 'w') as doc:
    json.dump(data, doc, indent=4)
    print("All the outputs has been stored for evaluation in 'response.json' file.")