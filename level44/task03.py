import PyPDF2

def merge_pdfs(file1, file2, output):
    # Abrindo o primeiro arquivo PDF
    with open(file1, 'rb') as f1:
        pdf1_reader = PyPDF2.PdfReader(f1)

        # Abrindo o segundo arquivo PDF
        with open(file2, 'rb') as f2:
            pdf2_reader = PyPDF2.PdfReader(f2)

            # Criando um objeto para escrever o PDF combinado
            pdf_writer = PyPDF2.PdfWriter()

            # Adicionando páginas do primeiro PDF no arquivo final
            for page in pdf1_reader.pages:
                pdf_writer.add_page(page)

            # Adicionando páginas do segundo PDF no arquivo final
            for page in pdf2_reader.pages:
                pdf_writer.add_page(page)

            # Escrevendo o PDF combinado no arquivo de saída
            with open(output, 'wb') as out:
                pdf_writer.write(out)

# Especificando nomes dos arquivos de origem e nome do arquivo final
file1 = 'report_part1.pdf'
file2 = 'report_part2.pdf'
output_file = 'full_report.pdf'

# Combinando arquivos PDF
merge_pdfs(file1, file2, output_file)