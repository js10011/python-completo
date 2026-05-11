import pdfplumber
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

# Função para extrair a primeira tabela de um arquivo PDF
def extract_table_from_pdf(input_pdf_path):
    # Abre o arquivo PDF usando pdfplumber
    with pdfplumber.open(input_pdf_path) as pdf:
        for page in pdf.pages:
            # Verifica se há tabelas na página
            if page.extract_tables():
                # Retorna a primeira tabela encontrada na página
                return page.extract_tables()[0]
    return None

# Função para criar um novo PDF com a tabela
def create_pdf_with_table(output_pdf_path, table_data):
    # Cria o documento PDF
    doc = SimpleDocTemplate(output_pdf_path, pagesize=A4)
    elements = []

    # Configurações de estilos
    styles = getSampleStyleSheet()

    # Cria o estilo do título com tamanho de fonte aumentado
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Title'],
        fontSize=18,  # Tamanho de fonte aumentado para o título
        spaceAfter=12  # Espaço após o título
    )

    # Configurações de estilo da tabela
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),         # Cor de fundo do cabeçalho da tabela
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),    # Cor do texto do cabeçalho
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),                # Alinhamento do texto ao centro
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),      # Fonte do cabeçalho
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),               # Espaço inferior para o cabeçalho
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),       # Cor de fundo para as linhas da tabela
        ('GRID', (0, 0), (-1, -1), 1, colors.black),          # Grade para a tabela
    ])

    # Criação do título
    title = Paragraph('Relatório de dados', title_style)
    elements.append(title)

    # Criação e adição da tabela com os dados
    table = Table(table_data)
    table.setStyle(table_style)
    elements.append(table)

    # Construção do PDF
    doc.build(elements)

# Função principal
def main():
    input_pdf_path = 'input.pdf'  # Caminho para o arquivo PDF de entrada
    output_pdf_path = 'output.pdf'  # Caminho para salvar o arquivo PDF de saída

    # Extração da tabela do PDF
    table_data = extract_table_from_pdf(input_pdf_path)

    # Verificação se a tabela foi extraída
    if table_data:
        create_pdf_with_table(output_pdf_path, table_data)
        print("PDF foi criado com sucesso.")
    else:
        print("Nenhuma tabela encontrada no PDF.")

# Execução do programa
main()