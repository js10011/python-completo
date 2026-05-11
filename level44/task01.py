from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet

# Nome do arquivo para salvar o PDF
file_name = "simple_report.pdf"

# Criamos o documento PDF
c = canvas.Canvas(file_name, pagesize=letter)

# Definimos estilos para o texto
styles = getSampleStyleSheet()
title_style = styles['Title']
subtitle_style = styles['Heading2']

# Adicionamos o título
c.setFont("Helvetica-Bold", 24)
c.drawCentredString(300, 750, "Relatório Diário")

# Adicionamos o subtítulo
c.setFont("Helvetica", 18)
c.drawCentredString(300, 720, "Situação Atual")

# Salvamos o documento PDF
c.save()