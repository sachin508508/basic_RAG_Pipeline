from llm import llm_object
from prompt import get_message
from chunk_retriever import retrieve, format_chunk
from langchain_core.runnables import RunnablePassthrough

def rag_chain():
    return ({"context": retrieve() | format_chunk, "query":RunnablePassthrough()} | get_message() | llm_object())
