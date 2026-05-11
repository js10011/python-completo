from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Nome do arquivo de saída PDF
filename = "formatted_text.pdf"

# Configuração do modelo de documento
doc = SimpleDocTemplate(filename, pagesize=letter)
styles = getSampleStyleSheet()

# Definição dos estilos para título, subtítulo e texto principal
header_style = styles['Heading1']
subheader_style = styles['Italic']
body_style = styles['BodyText']

# Criação de texto formatado usando tags HTML
header = Paragraph("<b>This is the Title</b>", header_style)
subheader = Paragraph("<i>This is the Subtitle</i>", subheader_style)
body = Paragraph("This is the main body of the text. " * 10, body_style)

# Criação do PDF com os elementos especificados
doc.build([header, subheader, body])