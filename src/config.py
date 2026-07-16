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
deepseek_url="https://api.deepseek.com"
deepseek_api_key=os.getenv("DEEPSEEK_API_KEY")
embedding_model="all-MiniLM-L6-v2"
temperature=0.4
max_tokens=1024