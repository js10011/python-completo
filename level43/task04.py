from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

# Exemplo de dados para a tabela
data = [
    ["Mês", "Vendas"],
    ["Janeiro", "$1000"],
    ["Fevereiro", "$1500"],
    ["Março", "$2000"]
]

# Nome do arquivo PDF para salvar o relatório
file_name = "sales_report.pdf"

# Criação do documento PDF
pdf = SimpleDocTemplate(file_name, pagesize=letter)

# Criação de estilo e cabeçalho
styles = getSampleStyleSheet()
title = Paragraph("Relatório de Vendas", styles['Title'])

# Criação da tabela com dados
table = Table(data)

# Aplicação de estilos à tabela
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),           # Fundo do cabeçalho da tabela
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),      # Cor do texto no cabeçalho
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),                  # Alinhamento do texto ao centro
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),        # Fonte do cabeçalho
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),                 # Espaço inferior para o cabeçalho
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),         # Fundo para as linhas da tabela
    ('GRID', (0, 0), (-1, -1), 1, colors.black)             # Grade para toda a tabela
])
table.setStyle(style)

# Montagem do PDF com os elementos
elements = [title, table]
pdf.build(elements)