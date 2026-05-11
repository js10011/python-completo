import os
from PyPDF2 import PdfReader, PdfWriter

# Especifica o diretório contendo os arquivos PDF
input_folder = 'pdf_folder'  # Substitua pelo caminho da sua pasta

# Itera sobre todos os arquivos na pasta especificada
for filename in os.listdir(input_folder):
    # Processa apenas arquivos com extensão .pdf
    if filename.endswith('.pdf'):
        # Cria o caminho completo para o arquivo PDF de entrada
        input_path = os.path.join(input_folder, filename)

        # Leitura do arquivo PDF
        with open(input_path, 'rb') as infile:
            reader = PdfReader(infile)

            # Percorre cada página do arquivo PDF
            for page_number in range(len(reader.pages)):
                writer = PdfWriter()
                writer.add_page(reader.pages[page_number])

                # Cria um nome para o novo arquivo contendo uma página
                base_name = os.path.splitext(filename)[0]
                output_filename = f"{base_name}_page_{page_number + 1}.pdf"
                output_path = os.path.join(input_folder, output_filename)

                # Escreve uma página em um novo arquivo PDF
                with open(output_path, 'wb') as outfile:
                    writer.write(outfile)