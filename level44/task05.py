import PyPDF2

# Solicita ao usuário o caminho para o arquivo PDF
file_path = input("Digite o caminho para o arquivo PDF: ")

# Abre o arquivo PDF em modo binário para leitura
with open(file_path, 'rb') as file:
    # Cria um objeto PDF reader
    pdf_reader = PyPDF2.PdfReader(file)
    # Inicializa a variável para armazenar o texto extraído
    text = ""

    # Percorre todas as páginas no arquivo PDF
    for page_num in range(len(pdf_reader.pages)):
        # Obtém a página
        page = pdf_reader.pages[page_num]
        # Extrai o texto da página
        text += page.extract_text()

# Imprime o texto extraído na tela
print(text)