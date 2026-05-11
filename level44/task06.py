import pdfplumber
import csv

# Definindo caminhos para o arquivo PDF e o arquivo CSV para salvar o resultado
pdf_path = 'example.pdf'  # Indique o caminho para o seu arquivo PDF
csv_path = 'output.csv'   # Indique o caminho para salvar o arquivo CSV

# Extração de texto do PDF por páginas
text_by_page = []
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        text_by_page.append(text)

# Salvamento de texto por páginas no arquivo CSV
with open(csv_path, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    for page_text in text_by_page:
        csv_writer.writerow([page_text])