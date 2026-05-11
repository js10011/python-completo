import pdfplumber

# Caminho para o documento PDF
pdf_path = 'test_document.pdf'

# Extraímos e exibimos o texto da primeira página
with pdfplumber.open(pdf_path) as pdf:
    # Extraímos a primeira página
    first_page = pdf.pages[0]
    # Extraímos o texto da primeira página
    text = first_page.extract_text()

print(text)