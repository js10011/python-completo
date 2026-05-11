from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Dados para o relatório
data = [
    ["Mês", "Quantidade de Vendas", "Valor Total de Vendas"],
    ["Janeiro", "100", "$5000"],
    ["Fevereiro", "150", "$7500"],
    ["Março", "130", "$6800"]
]

# Criação do documento PDF
pdf_file = "quarterly_sales_report.pdf"
document = SimpleDocTemplate(pdf_file, pagesize=A4)

# Criação da tabela com os dados
table = Table(data)

# Adição de estilos à tabela
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
])
table.setStyle(style)

# Título do documento
title = "Vendas do Trimestre"

# Geração do PDF com título e tabela
elements = []

# Adição do título
styles = getSampleStyleSheet()
title_style = styles["Title"]

elements.append(Paragraph(title, title_style))

# Adição da tabela após o título
elements.append(table)

# Construção do PDF
document.build(elements)