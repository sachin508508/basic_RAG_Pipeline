import os
from dotenv import load_dotenv

load_dotenv()

"""All the configurations are mentioned here!"""

CHROMA_DB="./chroma_db/"
FILE_PATH="./data/data_file.pdf"
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
gemini_model="gemini-3.1-flash-lite"
deepseek_model="deepseek-chat"
deepseek_url="https://api.deepseek.com"
deepseek_api_key=os.getenv("DEEPSEEK_API_KEY")
EMBEDDING_MODEL="all-MiniLM-L6-v2"
TEMPERATURE=0.4
TOP_K=3
MAX_TOKENS=1024
