from langchain_text_splitters import RecursiveCharacterTextSplitter
from document_loader import load_the_pdf
from config import chunk_size, chunk_overlap

def text_split():
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    document = load_the_pdf()
    return splitter.split_documents(document)