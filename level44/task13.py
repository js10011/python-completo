from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

# Nome do arquivo de saída
filename = "output.pdf"

# Definição dos tamanhos da página A4
width, height = A4
# Título e texto
title = "Título"
text = "Este é um exemplo de texto que será centralizado na página."

# Criação do arquivo PDF
c = canvas.Canvas(filename, pagesize=A4)

# Fonte e tamanho do texto para o título
c.setFont("Helvetica-Bold", 24)
# Cálculo das posições para centralizar o título
title_width = c.stringWidth(title, "Helvetica-Bold", 24)
title_x = (width - title_width) / 2
title_y = height / 2 + 2 * cm  # Move o título um pouco para cima

# Desenho do título
c.drawString(title_x, title_y, title)

# Fonte e tamanho do texto para o parágrafo
c.setFont("Helvetica", 14)
# Cálculo das posições para centralizar o texto
text_width = c.stringWidth(text, "Helvetica", 14)
text_x = (width - text_width) / 2
text_y = height / 2 - cm  # Move o texto um pouco para baixo

# Desenho do texto
c.drawString(text_x, text_y, text)

# Finalização e salvamento do PDF
c.save()