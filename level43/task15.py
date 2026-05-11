from PyPDF2 import PdfReader, PdfWriter

# Função para dividir o arquivo PDF com base no intervalo de páginas especificado
def split_pdf(input_pdf, start_page, end_page, output_pdf):
    # Abrimos o arquivo PDF de entrada para leitura
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Calculamos os índices zero-base para a página inicial e final
    # Como end_page é incluída, usamos ela como fim do intervalo (exclusivo)
    start_index = start_page - 1
    end_index = end_page

    # Adicionamos as páginas do intervalo especificado no objeto writer
    for page_number in range(start_index, end_index):
        writer.add_page(reader.pages[page_number])

    # Gravamos o novo arquivo PDF com as páginas escolhidas
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)

# Exemplo de uso
split_pdf('sample.pdf', 1, 3, 'section_1.pdf')  # Extração de páginas 1–3
split_pdf('sample.pdf', 5, 7, 'section_2.pdf')  # Extração de páginas 5–7