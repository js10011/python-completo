from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Nome do arquivo de saída PDF
filename = "custom_report.pdf"

# Criação do documento PDF
doc = SimpleDocTemplate(filename, pagesize=A4)
elements = []

# Carregamento e configuração de estilos
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'TitleStyle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=36,
    textColor=colors.HexColor("#003366"),
    spaceAfter=20
)

header_style = ParagraphStyle(
    'HeaderStyle',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=24,
    textColor=colors.HexColor("#336699"),
    spaceAfter=10
)

subheader_style = ParagraphStyle(
    'SubHeaderStyle',
    parent=styles['Heading3'],
    fontName='Helvetica-Bold',
    fontSize=18,
    textColor=colors.HexColor("#6699FF"),
    spaceAfter=10
)

text_style = ParagraphStyle(
    'TextStyle',
    parent=styles['BodyText'],
    fontName='Helvetica',
    fontSize=12,
    spaceAfter=10
)

# Adicionando a página de título
elements.append(Spacer(1, 200))
elements.append(Paragraph("Relatório da Empresa", title_style))
elements.append(Spacer(1, 50))

# Adicionando o logotipo da empresa
logo_path = "company_logo.png"  # Especifique o caminho para o logotipo da empresa
elements.append(Image(logo_path, width=200, height=100))
elements.append(Spacer(1, 200))

# Adicionando seções de análise de dados
for section in range(1, 4):
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(f"Seção {section}: Análise de Dados", header_style))
    elements.append(Paragraph(f"Subseção {section}.1: Visão Detalhada", subheader_style))
    elements.append(Paragraph("Esta subseção fornece uma visão detalhada da análise de dados realizada. "
                              "A análise revela principais insights sobre as tendências e padrões observados ao longo do período.", text_style))
    elements.append(Paragraph(f"Subseção {section}.2: Insights Estatísticos", subheader_style))
    elements.append(Paragraph("Esta subseção explora os insights e métricas estatísticas derivadas dos dados. "
                              "Os resultados destacam descobertas e interpretações significativas.", text_style))

# Criação do PDF
doc.build(elements)