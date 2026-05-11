from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Parâmetros da página
width, height = A4

# Criação do documento PDF
c = canvas.Canvas("my_first_pdf.pdf", pagesize=A4)

# Configuração do texto
text = "Este é meu primeiro documento PDF"
font_name = "Times-Roman"
font_size = 14

# Cálculo da posição para o texto (quarto superior da página)
x_position = 50  # margem esquerda
y_position = height - height / 4  # quarto superior da página

# Configuração da fonte e inserção do texto
c.setFont(font_name, font_size)
c.drawString(x_position, y_position, text)

# Salvando o documento PDF
c.save()