from langchain_huggingface import HuggingFaceEmbeddings
from config import embedding_model


def get_embedding_model():
    return HuggingFaceEmbeddings(model_name=embedding_model)
