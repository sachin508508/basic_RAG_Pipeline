from langchain_openai import ChatOpenAI
from config import deepseek_url, deepseek_model, deepseek_api_key, temperature, max_tokens


def llm_object():
    return ChatOpenAI(model=deepseek_model, api_key=deepseek_api_key, base_url=deepseek_url, max_tokens=max_tokens, temperature=temperature)