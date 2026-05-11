from fpdf import FPDF
from datetime import datetime
import os

# Função para gerar relatórios mensais
def generate_monthly_reports(data):
    # Definindo os meses e anos para nomes dos arquivos de relatório
    months = ["2023_01", "2023_02", "2023_03"]

    # Iterando pelos dados mensais e criando relatórios
    for i, monthly_data in enumerate(data):
        create_pdf_report(monthly_data, months[i])

# Função para criar um relatório PDF para um mês específico
def create_pdf_report(monthly_data, month_year):
    # Criando objeto PDF
    pdf = FPDF()
    pdf.add_page()

    # Definindo título do relatório
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"Relatório de vendas para: {month_year}", ln=True, align="C")

    # Definindo cabeçalhos das colunas
    pdf.set_font("Arial", "B", 12)
    pdf.cell(60, 10, "Produto", 1)
    pdf.cell(60, 10, "Região", 1)
    pdf.cell(60, 10, "Vendas", 1)
    pdf.ln()

    # Adicionando linhas de dados
    pdf.set_font("Arial", "", 12)
    for product, region, sales in monthly_data:
        pdf.cell(60, 10, product, 1)
        pdf.cell(60, 10, region, 1)
        pdf.cell(60, 10, sales, 1)
        pdf.ln()

    # Salvando PDF com nome único para cada mês
    report_filename = f"monthly_report_{month_year}.pdf"
    pdf.output(report_filename)
    print(f"Relatório salvo como {report_filename}")

# Dados de vendas por três meses
sales_data = [
    [("Produto X", "Norte", "2000"), ("Produto Y", "Sul", "2500")],
    [("Produto Z", "Oeste", "1800"), ("Produto W", "Leste", "2200")],
    [("Produto A", "Norte", "2100"), ("Produto B", "Sul", "1700")]
]

# Geração dos relatórios
generate_monthly_reports(sales_data)