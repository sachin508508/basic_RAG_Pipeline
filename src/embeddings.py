from langchain_community.embeddings import HuggingFaceEmbeddings
from config import embedding_model


def embed():
    return HuggingFaceEmbeddings(model_name=embedding_model)
