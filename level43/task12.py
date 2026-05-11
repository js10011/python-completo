import PyPDF2

# Função para combinar arquivos PDF e adicionar metadados
def merge_pdfs(input_files, output_file, metadata):
    pdf_writer = PyPDF2.PdfWriter()  # Criamos um objeto para escrever PDF

    # Percorremos cada arquivo da lista input_files e adicionamos suas páginas ao pdf_writer
    for file_name in input_files:
        with open(file_name, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)  # Lemos o arquivo PDF
            # Adicionamos cada página do PDF atual ao pdf_writer
            for page in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page])

    # Adicionamos metadados ao arquivo PDF final
    pdf_writer.add_metadata(metadata)

    # Gravamos o PDF combinado no arquivo de saída
    with open(output_file, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

# Lista de nomes de arquivos PDF de entrada para combinar
input_files = ['report1.pdf', 'report2.pdf', 'report3.pdf']

# Nome do arquivo PDF de saída
output_file = 'final_report.pdf'

# Metadados para o PDF final
metadata = {
    '/Title': 'Relatório Final',       # Título
    '/Author': 'Empresa X',            # Autor
    '/Subject': 'Revisão do Ano'       # Assunto
}

# Combinação de arquivos PDF com adição de metadados
merge_pdfs(input_files, output_file, metadata)