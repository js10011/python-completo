from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Nome do arquivo para salvar o documento PDF
filename = "basic_report.pdf"

# Criar um novo documento PDF
c = canvas.Canvas(filename, pagesize=letter)

# Definir a largura e a altura da página
width, height = letter

# Adicionar o título
c.setFont("Helvetica-Bold", 20)
c.drawString(100, height - 100, "Relatório de Vendas")

# Adicionar separador
c.line(100, height - 110, width - 100, height - 110)

# Adicionar o subtítulo
c.setFont("Helvetica", 16)
c.drawString(100, height - 130, "Para o Primeiro Trimestre")

# Salvar o documento PDF
c.save()