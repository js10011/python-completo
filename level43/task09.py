import PyPDF2

# Caminho para os arquivos PDF de origem e o arquivo resultante
file1 = 'file1.pdf'
file2 = 'file2.pdf'
output = 'merged_document.pdf'

# Abrimos os arquivos PDF
pdf1_file = open(file1, 'rb')
pdf2_file = open(file2, 'rb')

# Criamos um objeto PdfReader para cada arquivo
pdf1_reader = PyPDF2.PdfReader(pdf1_file)
pdf2_reader = PyPDF2.PdfReader(pdf2_file)

# Criamos um objeto PdfWriter, que irá conter as páginas combinadas
pdf_writer = PyPDF2.PdfWriter()

# Extraímos todas as páginas do primeiro PDF e as adicionamos ao PdfWriter
for page_num in range(len(pdf1_reader.pages)):
    page = pdf1_reader.pages[page_num]
    pdf_writer.add_page(page)

# Extraímos todas as páginas do segundo PDF e as adicionamos ao PdfWriter
for page_num in range(len(pdf2_reader.pages)):
    page = pdf2_reader.pages[page_num]
    pdf_writer.add_page(page)

# Salvamos o novo arquivo PDF
with open(output, 'wb') as output_pdf:
    pdf_writer.write(output_pdf)

# Fechamos todos os arquivos abertos
pdf1_file.close()
pdf2_file.close()