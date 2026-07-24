import json
from src.rag_pipeline import rag_chain_with_context
from langchain_core.output_parsers import StrOutputParser

with open('./experiments/evaluation_questions.json', 'r') as doc:
    data: dict = json.load(doc)

for query in data:
    print(f"Evaluating question {query['id']} out of {len(data)}.")
    result = rag_chain_with_context(query['question'])
    query['context'] = result['context']
    query['response'] = result['response']

with open('./experiments/evaluation_results.json', 'w') as doc:
    json.dump(data, doc, indent=4)
    print("All the outputs has been stored for evaluation in 'response.json' file.")