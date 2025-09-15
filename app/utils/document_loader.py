from PyPDF2 import PdfReader
import io

async def load_txt(file_bytes: bytes) -> str:
    """
    Load a text file from bytes.
    """
    return file_bytes.decode("utf-8", errors="ignore")

async def load_pdf(file_bytes: bytes) -> str:
    """
    Load a PDF file from bytes and extract text.
    """
    reader = PdfReader(io.BytesIO(file_bytes))
    return " ".join(page.extract_text() for page in reader.pages if page.extract_text())
