import pdfplumber
import pandas as pd

# Caminho para os arquivos PDF e Excel
pdf_path = "example.pdf"  # Especifique o caminho para o arquivo PDF
excel_path = "output.xlsx"  # Especifique o caminho para salvar o arquivo Excel

# Extração de tabela do PDF
with pdfplumber.open(pdf_path) as pdf:
    page_number = 0  # Defina o número da página, se for necessário outra página
    page = pdf.pages[page_number]
    table = page.extract_table()

# Verificação da presença da tabela e salvamento em Excel
if table:
    # Conversão da tabela em DataFrame
    df = pd.DataFrame(table[1:], columns=table[0])

    # Salvamento do DataFrame em arquivo Excel
    df.to_excel(excel_path, index=False)
    print(f"Tabela salva com sucesso em {excel_path}")
else:
    print("Tabela não encontrada na página especificada do PDF.")