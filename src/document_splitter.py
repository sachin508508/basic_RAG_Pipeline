from langchain_text_splitters import RecursiveCharacterTextSplitter
from document_loader import load_the_pdf
from config import CHUNK_SIZE, CHUNK_OVERLAP

def text_split():
    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    document = load_the_pdf()
    return splitter.split_documents(document)