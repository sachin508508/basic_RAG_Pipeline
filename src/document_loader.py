from config import file_path
from langchain_community.document_loaders import PyPDFLoader

def load_the_pdf():
    get_pdf = PyPDFLoader(file_path=file_path)
    return get_pdf.load()
