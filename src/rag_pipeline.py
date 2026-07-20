from llm import llm_object
from prompt import get_message
from chunk_retriever import retrieve, format_chunk
from langchain_core.runnables import RunnablePassthrough
from config import TOP_K, TEMPERATURE

def rag_chain(top_k=TOP_K, temperature=TEMPERATURE):
    return ({"context": retrieve(top_k) | format_chunk, "query":RunnablePassthrough()} | get_message() | llm_object(temperature))
