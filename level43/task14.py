import PyPDF2

# Função para extrair um intervalo especificado de páginas de um arquivo PDF
def extract_pages(input_pdf, output_pdf, start_page, end_page):
    # Abre o arquivo PDF original para leitura
    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfReader(file)  # Cria um objeto para ler o PDF

        writer = PyPDF2.PdfWriter()  # Cria um objeto para escrever o PDF

        # Percorre as páginas no intervalo especificado
        for page_num in range(start_page - 1, end_page):  # Considera que a numeração começa de 0
            writer.add_page(reader.pages[page_num])  # Adiciona a página ao PDF final

        # Salva as páginas extraídas em um novo arquivo PDF
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)

# Caminhos para os arquivos
input_pdf_path = "sample.pdf"          # Arquivo PDF original
output_pdf_path = "range_2_to_4.pdf"   # Arquivo PDF de saída com as páginas selecionadas

# Chamada da função para extrair as páginas 2-4
extract_pages(input_pdf_path, output_pdf_path, 2, 4)