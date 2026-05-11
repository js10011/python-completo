from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Nome do arquivo de saída
filename = "report.pdf"

# Criação do documento PDF e configuração do tamanho da página
c = canvas.Canvas(filename, pagesize=A4)
width, height = A4

# Primeira página com o título "Relatório 2023"
c.setFont("Helvetica-Bold", 36)
c.drawCentredString(width / 2, height / 2, "Relatório 2023")
c.showPage()

# Segunda página com o texto "Índice"
c.setFont("Times-Roman", 24)
c.drawCentredString(width / 2, height / 2, "Índice")
c.showPage()

# Terceira página com o texto "Fim do Relatório"
c.setFont("Courier", 18)
c.drawCentredString(width / 2, height / 2, "Fim do Relatório")
c.showPage()

# Salvando o documento
c.save()