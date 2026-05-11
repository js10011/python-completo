import PyPDF2

def merge_pdfs_with_bookmarks(pdf_files, output_file):
    # Criar um PdfMerger para mesclar os PDFs
    pdf_merger = PyPDF2.PdfMerger()
    current_page = 0  # Inicializar o contador de páginas atuais

    for file in pdf_files:
        # Abrir o arquivo PDF atual
        with open(file, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            num_pages = len(pdf_reader.pages)

            # Adicionar o arquivo PDF atual ao PdfMerger
            pdf_merger.append(pdf_reader, import_bookmarks=False)

            # Adicionar um marcador no início deste arquivo PDF com o nome do arquivo
            pdf_merger.add_bookmark(title=file, pagenum=current_page)

            # Atualizar o número da página atual para o próximo arquivo
            current_page += num_pages

    # Escrever o resultado no arquivo de saída
    with open(output_file, 'wb') as f_out:
        pdf_merger.write(f_out)

# Definir os nomes dos arquivos de entrada e saída
input_files = ["part1.pdf", "part2.pdf", "part3.pdf"]
output_file = "merged_with_bookmarks.pdf"

# Executar a função para mesclar os PDFs com marcadores
merge_pdfs_with_bookmarks(input_files, output_file)