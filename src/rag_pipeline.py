from src.llm import llm_object
from src.prompt import get_message
from src.chunk_retriever import retrieve, format_chunk
from langchain_core.runnables import RunnablePassthrough
from src.config import TOP_K, TEMPERATURE
from langchain_core.output_parsers import StrOutputParser
from src.hybrid_retriever import hybrid


def rag_chain(top_k=TOP_K, temperature=TEMPERATURE):
    search_type = int(input('Enter the search type: press 1 to semantic search. press 2 to hybrid search.'))
    if search_type == 1:
        return ({"context": retrieve(top_k) | format_chunk, "query":RunnablePassthrough()} | get_message() | llm_object(temperature))
    elif search_type == 2:
        return ({"context": hybrid(top_k) | format_chunk, "query":RunnablePassthrough()} | get_message() | llm_object(temperature))    

def rag_chain_with_context(query: str, top_k=TOP_K, temperature=TEMPERATURE):
    context_chain = retrieve(top_k) | format_chunk
    context = context_chain.invoke(query)

    main_chain = get_message() | llm_object(temperature) | StrOutputParser()
    response = main_chain.invoke({'query': query, 'context': context})

    return {'context':context,'response': response}
