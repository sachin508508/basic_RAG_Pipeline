from langchain_openai import ChatOpenAI
from config import deepseek_url, deepseek_model, deepseek_api_key, TEMPERATURE, MAX_TOKENS
from exceptions import MissingAPIKeyException

def llm_object(temperature=TEMPERATURE):
    if not deepseek_api_key:
        raise MissingAPIKeyException("API key not found! Please include the api key in '.env' file.")
    else:
        return ChatOpenAI(model=deepseek_model, api_key=deepseek_api_key, base_url=deepseek_url, max_tokens=MAX_TOKENS, temperature=temperature)