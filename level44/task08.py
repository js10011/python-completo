import argparse
import os
import pandas as pd
import pdfplumber

# Função para extrair texto de todas as páginas de um arquivo PDF
def extract_text_from_pdf(pdf_path):
    text = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text.append(page.extract_text())  # Extraímos o texto de cada página
    return '\n'.join(text)  # Unimos o texto de todas as páginas

# Função para limpar texto
def clean_text(text):
    # Exemplo de limpeza de texto: remoção de quebras de linha e espaços desnecessários
    return text.replace('\n', ' ').strip()

# Função para extrair todas as tabelas de um arquivo PDF
def extract_tables_from_pdf(pdf_path):
    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_tables = page.extract_tables()  # Extraímos as tabelas da página
            if page_tables:
                tables.extend(page_tables)  # Adicionamos as tabelas à lista geral
    return tables

# Função para salvar dados em formato CSV ou Excel
def save_data_to_file(data, output_format, output_file):
    if output_format == 'csv':
        data.to_csv(output_file, index=False)  # Salvamos em formato CSV
    elif output_format == 'excel':
        data.to_excel(output_file, index=False, engine='openpyxl')  # Salvamos em formato Excel

# Função para processar lista de arquivos PDF
def process_pdf_files(pdf_files, output_format):
    for pdf_file in pdf_files:
        # Extraímos e limpamos texto do PDF
        text = extract_text_from_pdf(pdf_file)
        text = clean_text(text)

        # Extraímos tabelas do PDF
        tables = extract_tables_from_pdf(pdf_file)

        # Exemplo de combinação de texto e tabelas em uma única tabela
        data = pd.DataFrame({'Extracted Text': [text]})  # Texto como uma única linha de DataFrame

        if tables:
            # Adicionamos cada tabela do PDF ao DataFrame geral
            for i, table in enumerate(tables):
                df_table = pd.DataFrame(table[1:], columns=table[0])  # Conversão da tabela para DataFrame
                data = pd.concat([data, df_table], ignore_index=True)

        # Formamos o nome do arquivo de saída com base no nome original e formato
        output_file = os.path.splitext(pdf_file)[0] + ('.csv' if output_format == 'csv' else '.xlsx')
        save_data_to_file(data, output_format, output_file)  # Salvamento dos dados

# Função principal
def main():
    # Pedimos ao usuário os caminhos para os arquivos PDF através do input do console
    pdf_files = input("Digite os caminhos para os arquivos PDF, separados por espaço: ").split()

    # Solicitamos ao usuário o formato de saída limitado a "csv" ou "excel"
    output_format = ''
    while output_format not in ['csv', 'excel']:
        output_format = input("Digite o formato de saída (csv ou excel): ").strip().lower()

    # Processamento dos arquivos PDF com base nos argumentos
    process_pdf_files(pdf_files, output_format)

# Execução do programa
main()