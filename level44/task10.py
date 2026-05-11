from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

# Nome do arquivo PDF
pdf_file = "formatted_text.pdf"

# Criação do documento PDF
doc = SimpleDocTemplate(pdf_file, pagesize=A4)

# Uso dos estilos padrão do ReportLab
styles = getSampleStyleSheet()

# Título
title_style = ParagraphStyle(name='TitleStyle', parent=styles['Heading1'],
                             fontName='Helvetica-Bold', fontSize=18,
                             textColor=colors.red, spaceAfter=inch/4)

# Estilo para os parágrafos
paragraph_style = ParagraphStyle(name='ParagraphStyle', parent=styles['BodyText'],
                                 fontName='Helvetica', fontSize=12,
                                 textColor=colors.black, spaceAfter=inch/4)

# Título e texto
title = "This is the Title"
first_paragraph = "This is the first paragraph of the document. It provides an introduction and overview of the topic being discussed."
second_paragraph = "This is the second paragraph of the document. It continues the discussion and provides additional insights and information."

# Criação de elementos para o documento
elements = []

# Adição do título
elements.append(Paragraph(title, title_style))
elements.append(Spacer(1, 12))

# Adição do primeiro parágrafo
elements.append(Paragraph(first_paragraph, paragraph_style))
elements.append(Spacer(1, 12))

# Adição do segundo parágrafo
elements.append(Paragraph(second_paragraph, paragraph_style))
elements.append(Spacer(1, 12))

# Construção do PDF
doc.build(elements)