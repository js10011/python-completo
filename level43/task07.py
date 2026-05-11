import PyPDF2

# Abertura do documento PDF
with open('example.pdf', 'rb') as file:
    # Criação do objeto PDF Reader
    reader = PyPDF2.PdfReader(file)

    # Inicialização da lista de páginas para extração
    pages_to_extract = [1, 3]  # Índices para páginas 2 e 4

    # Extração de texto e exibição na tela
    for page_num in pages_to_extract:
        page = reader.pages[page_num]
        text = page.extract_text()
        print(f"Texto da página {page_num + 1}:\n{text}\n")