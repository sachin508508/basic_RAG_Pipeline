from config import FILE_PATH
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from exceptions import MissingPDFFileException

def load_the_pdf():
    file_path = Path(FILE_PATH)
    if not file_path.exists():
        raise MissingPDFFileException("No PDF files found! Please attach the PDF inside /data folder with the name 'data_file.py'.")
    try:
        get_pdf = PyPDFLoader(file_path=FILE_PATH)
        return get_pdf.load()
    except Exception as e:
        raise RuntimeError(
            "Unable to read the PDF! Please ensure the PDF is valid and not corrupted."
        ) from e