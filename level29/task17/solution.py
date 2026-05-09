import PyPDF2

# Definimos os nomes dos arquivos de entrada e saída
input_pdf = "sample.pdf"
output_pdf = "page_1.pdf"

# Abertura do documento PDF para leitura
with open(input_pdf, "rb") as file:
    reader = PyPDF2.PdfReader(file)

    # Extração da primeira página
    first_page = reader.pages[0]

    # Criação de um novo objeto PDF para escrita
    writer = PyPDF2.PdfWriter()
    writer.add_page(first_page)

    # Salvamento da primeira página em um novo arquivo PDF
    with open(output_pdf, "wb") as new_file:
        writer.write(new_file)