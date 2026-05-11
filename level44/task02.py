from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

# Nome do arquivo PDF para criação
filename = "sectioned_report.pdf"

# Criação do arquivo PDF e definição do tamanho da página
c = canvas.Canvas(filename, pagesize=A4)

# Definição das coordenadas iniciais
width, height = A4
c.translate(cm, height - cm)

# Adicionando o título
c.setFont("Helvetica-Bold", 16)
c.drawString(0, -1 * cm, "Relatório Semanal")

# Adicionando os subtítulos
c.setFont("Helvetica", 14)
c.drawString(0, -3 * cm, "1. Informações Gerais")
c.drawString(0, -5 * cm, "2. Resultados da Análise")
c.drawString(0, -7 * cm, "3. Previsões")

# Salvando o arquivo PDF
c.save()