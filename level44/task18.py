from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

# Caminho para salvar o PDF
output_file = "report_with_table.pdf"

# Criação do documento
doc = SimpleDocTemplate(output_file, pagesize=A4)

# Estilos para títulos e texto
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'TitleStyle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=24,
    spaceAfter=12
)
subtitle_style = ParagraphStyle(
    'SubtitleStyle',
    parent=styles['Heading2'],
    fontName='Helvetica',
    fontSize=18,
    spaceAfter=12
)

# Título e subtítulo
title = Paragraph("Relatório de Vendas", title_style)
subtitle = Paragraph("Para o Primeiro Trimestre", subtitle_style)
separator = Spacer(1, 0.5 * cm)

# Dados de exemplo para a tabela
data = [
    ["Produto", "Região", "Vendas"],
    ["Produto A", "Norte", "2000"],
    ["Produto B", "Sul", "1500"]
]

# Criação da tabela e aplicação de estilos
table = Table(data, colWidths=[5 * cm, 5 * cm, 4 * cm])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 12),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]))

# Composição do documento com os elementos
elements = [title, subtitle, separator, table]

# Construção do PDF
doc.build(elements)

print(f"Relatório salvo como {output_file}")