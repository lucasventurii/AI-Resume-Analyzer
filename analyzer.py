
from pypdf import PdfReader
from io import BytesIO


def extract_resume_text(pdf_file):
    """
    Extrai o texto de um currículo em PDF.
    """

    pdf = PdfReader(BytesIO(pdf_file.getvalue()))

    text = ""

    for page in pdf.pages:
        text += page.extract_text() or ""

    return text
