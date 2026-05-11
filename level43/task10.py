import PyPDF2

# Caminho para os arquivos PDF de origem e o arquivo resultante
file1 = 'documentA.pdf'
file2 = 'documentB.pdf'
output = 'even_pages_merged.pdf'

# Criamos um objeto PdfWriter para as páginas unidas
pdf_writer = PyPDF2.PdfWriter()

# Processamento do primeiro arquivo
with open(file1, 'rb') as f1:
    pdf_reader1 = PyPDF2.PdfReader(f1)
    for page_num in range(len(pdf_reader1.pages)):
        if (page_num + 1) % 2 == 0:  # Páginas pares (começando com 1)
            pdf_writer.add_page(pdf_reader1.pages[page_num])

# Processamento do segundo arquivo
with open(file2, 'rb') as f2:
    pdf_reader2 = PyPDF2.PdfReader(f2)
    for page_num in range(len(pdf_reader2.pages)):
        if (page_num + 1) % 2 == 0:  # Páginas pares (começando com 1)
            pdf_writer.add_page(pdf_reader2.pages[page_num])

# Gravação do PDF combinado no arquivo de saída
with open(output, 'wb') as output_file:
    pdf_writer.write(output_file)