from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
import io

# Função para criar a página de título
def create_title_page():
    buffer = io.BytesIO()  # Buffer para armazenar a página do PDF
    c = canvas.Canvas(buffer, pagesize=A4)
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(297.5, 750, "Relatório Anual de 2023")  # Texto centralizado na página
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# Função para criar a página do índice
def create_content_page():
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    c.setFont("Helvetica", 18)
    c.drawString(50, 800, "Índice")  # Título "Índice"

    # Adiciona seções com subtítulos
    c.setFont("Helvetica", 14)
    c.drawString(50, 760, "1. Introdução")
    c.setFont("Helvetica", 12)
    c.drawString(60, 740, "Esta seção apresenta uma breve introdução ao tema do relatório.")

    c.setFont("Helvetica", 14)
    c.drawString(50, 700, "2. Dados e Análise")
    c.setFont("Helvetica", 12)
    c.drawString(60, 680, "Aqui é apresentada a análise dos dados usados no relatório.")

    c.setFont("Helvetica", 14)
    c.drawString(50, 640, "3. Conclusões e Recomendações")
    c.setFont("Helvetica", 12)
    c.drawString(60, 620, "Esta seção contém conclusões e recomendações para ações futuras.")

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# Função para criar a página principal com o conteúdo
def create_main_content_page():
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    c.setFont("Helvetica", 14)
    c.drawString(50, 800, "Conteúdo principal do relatório")  # Título do conteúdo principal
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# Função para unir as páginas PDF em um único PDF
def combine_pdfs(title_page, content_page, main_content_page, output_filename):
    pdf_writer = PdfWriter()  # Cria um objeto para escrever o PDF combinado

    # Adiciona páginas dos buffers ao PDF final
    for pdf_buffer in [title_page, content_page, main_content_page]:
        pdf_reader = PdfReader(pdf_buffer)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

    # Salva o PDF combinado em um arquivo
    with open(output_filename, 'wb') as out_pdf:
        pdf_writer.write(out_pdf)

# Função principal
def main():
    title_page = create_title_page()         # Cria a página de título
    content_page = create_content_page()     # Cria o índice
    main_content_page = create_main_content_page()  # Cria o conteúdo principal

    output_filename = "structured_final_report.pdf"  # Nome do arquivo PDF de saída
    combine_pdfs(title_page, content_page, main_content_page, output_filename)
    print(f"Arquivo {output_filename} criado com sucesso.")

# Executa o programa principal
main()