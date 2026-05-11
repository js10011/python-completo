import PyPDF2

# Caminho para o arquivo PDF e o arquivo de texto de saída
pdf_file = 'example.pdf'
output_file = 'extracted_text.txt'

# Leitura e extração de texto do arquivo PDF
with open(pdf_file, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()

# Salvamento do texto extraído em um arquivo de texto
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(text)