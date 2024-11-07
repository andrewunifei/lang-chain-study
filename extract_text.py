import fitz

def extract_text_from_pdf(path):
    pdf_document = fitz.open(path)
    text_content = []

    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]
        text = page.get_text()
        text_content.append(text)

    pdf_document.close()
    return text_content
