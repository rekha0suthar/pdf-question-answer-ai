import fitz  # PyMuPDF

# This function extracts text from a PDF file given its file path
def extract_text_from_pdf(file_path: str) -> str:
    document = fitz.open(file_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text