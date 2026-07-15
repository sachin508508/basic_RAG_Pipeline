import os
from dotenv import load_dotenv

load_dotenv()

"""All the configurations are mentioned here!"""

CHROMA_DB="./chroma_db/"
file_path="./data/data_file.pdf"
chunk_size=1000
chunk_overlap=200
gemini_model="gemini-3.1-flash-lite"
deepseek_model="deepseek-chat"
embedding_model="all-MiniLM-L6-v2"