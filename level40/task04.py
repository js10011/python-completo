'''import schedule
import time
import requests
import json
import os
from datetime import datetime
from fpdf import FPDF

# Constantes
API_KEY = "your_openweather_api_key"
CITY_ID = "your_city_id"
WEATHER_FILE = "weather_data.json"
REPORT_FILE = "weekly_report.pdf"

# Função para obter dados climáticos
def fetch_weather_data():
    url = (f"http://api.openweathermap.org/data/2.5/weather?id={CITY_ID}&appid={API_KEY}&units=metric")
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        save_weather_data(data)
    else:
        print("Erro ao obter dados:", response.status_code)

# Função para salvar dados climáticos
def save_weather_data(data):
    if os.path.exists(WEATHER_FILE):
        with open(WEATHER_FILE, "r") as file:
            weather_data = json.load(file)
    else:
        weather_data = []

    weather_data.append({
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "weather": data
    })

    with open(WEATHER_FILE, "w") as file:
        json.dump(weather_data, file, ensure_ascii=False, indent=4)
    print("Dados climáticos salvos.")

# Função para criar relatório semanal
def create_weekly_report():
    if not os.path.exists(WEATHER_FILE):
        print("Nenhum dado climático disponível para o relatório.")
        return

    with open(WEATHER_FILE, "r") as file:
        weather_data = json.load(file)

    today = datetime.now()
    last_week = today - timedelta(days=7)
    last_week_data = [entry for entry in weather_data if datetime.fromisoformat(entry["date"]) > last_week]

    if not last_week_data:
        print("Nenhum dado para gerar relatório da última semana.")
        return

    # Criação do relatório PDF usando FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Relatório Climático da Última Semana", ln=True, align='C')

    for entry in last_week_data:
        date = entry["date"]
        weather_desc = entry["weather"]["weather"][0]["description"]
        temp = entry["weather"]["main"]["temp"]
        pdf.cell(200, 10, txt=f"{date} - {weather_desc}, Temperatura: {temp}C", ln=True)

    pdf.output(REPORT_FILE)
    print("Relatório semanal salvo em formato PDF.")

# Agendador de tarefas
schedule.every().day.at("09:00").do(fetch_weather_data)
schedule.every().monday.at("10:00").do(create_weekly_report)

# Loop principal
while True:
    schedule.run_pending()
    time.sleep(60)'''  # Aguarda 60 segundos antes de verificar novamente as tarefas
 
import requests
import schedule
import time
import json
import os
from datetime import datetime, timedelta
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# -------------------------
# CONFIGURAÇÕES
# -------------------------
API_KEY = "SUA_API_KEY"
CIDADE = "Sao Paulo"
ARQUIVO = "dados_clima.json"

# -------------------------
# COLETA DE DADOS
# -------------------------
def coletar_clima():
    print(f"[{datetime.now()}] Coletando dados do clima...")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        registro = {
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "temperatura": dados["main"]["temp"],
            "umidade": dados["main"]["humidity"],
            "descricao": dados["weather"][0]["description"]
        }

        # Carregar dados existentes
        if os.path.exists(ARQUIVO):
            with open(ARQUIVO, "r") as f:
                historico = json.load(f)
        else:
            historico = []

        historico.append(registro)

        # Salvar
        with open(ARQUIVO, "w") as f:
            json.dump(historico, f, indent=4)

        print("Dados salvos com sucesso.")

    except Exception as e:
        print("Erro ao coletar dados:", e)


# -------------------------
# GERAR RELATÓRIO PDF
# -------------------------
def gerar_relatorio():
    print(f"[{datetime.now()}] Gerando relatório semanal...")

    if not os.path.exists(ARQUIVO):
        print("Arquivo de dados não encontrado.")
        return

    try:
        with open(ARQUIVO, "r") as f:
            historico = json.load(f)

        data_limite = datetime.now() - timedelta(days=7)

        dados_semana = [
            d for d in historico
            if datetime.strptime(d["data"], "%Y-%m-%d %H:%M:%S") >= data_limite
        ]

        if not dados_semana:
            print("Sem dados suficientes para gerar relatório.")
            return

        temp_media = sum(d["temperatura"] for d in dados_semana) / len(dados_semana)
        umidade_media = sum(d["umidade"] for d in dados_semana) / len(dados_semana)

        nome_pdf = f"relatorio_{datetime.now().strftime('%Y%m%d')}.pdf"

        c = canvas.Canvas(nome_pdf, pagesize=letter)

        # Título
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, 750, "Relatório Semanal de Clima")

        c.setFont("Helvetica", 12)
        c.drawString(100, 720, "Período: últimos 7 dias")
        c.drawString(100, 700, f"Temperatura média: {temp_media:.2f} °C")
        c.drawString(100, 680, f"Umidade média: {umidade_media:.2f} %")

        # Listagem
        y = 650
        for d in dados_semana:
            linha = f"{d['data']} | {d['temperatura']}°C | {d['umidade']}% | {d['descricao']}"
            c.drawString(50, y, linha)
            y -= 20

            if y < 50:
                c.showPage()
                c.setFont("Helvetica", 12)
                y = 750

        c.save()

        print(f"Relatório gerado: {nome_pdf}")

    except Exception as e:
        print("Erro ao gerar relatório:", e)


# -------------------------
# AGENDAMENTO
# -------------------------
schedule.every().day.at("09:00").do(coletar_clima)
schedule.every().monday.at("10:00").do(gerar_relatorio)

print("Scheduler em execução...")

# Loop principal
while True:
    schedule.run_pending()
    time.sleep(30)