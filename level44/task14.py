from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.enums import TA_LEFT, TA_RIGHT

# Criar documento PDF
doc = SimpleDocTemplate("styled_text.pdf", pagesize=letter)

# Estilos padrão
styles = getSampleStyleSheet()

# Criar estilo para o primeiro parágrafo
style_first_paragraph = ParagraphStyle(
    name="Times-Roman-12",
    parent=styles["Normal"],
    fontName="Times-Roman",
    fontSize=12,
    alignment=TA_LEFT
)

# Criar estilo para o segundo parágrafo
style_second_paragraph = ParagraphStyle(
    name="Times-Italic-14",
    parent=styles["Normal"],
    fontName="Times-Italic",
    fontSize=14,
    alignment=TA_RIGHT
)

# Definir texto para os parágrafos
text1 = "Este é o primeiro parágrafo, alinhado à esquerda, com fonte Times-Roman, tamanho 12."
text2 = "Este é o segundo parágrafo, alinhado à direita, com fonte Times-Italic, tamanho 14."

# Criar objetos Paragraph para cada parágrafo
paragraph1 = Paragraph(text1, style_first_paragraph)
paragraph2 = Paragraph(text2, style_second_paragraph)

# Adicionar parágrafos à lista de elementos do documento
elements = [paragraph1, paragraph2]

# Criar PDF, adicionando a ele os elementos
doc.build(elements)