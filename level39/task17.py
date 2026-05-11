import schedule
import time

def start_of_work_day():
    print("Início do dia de trabalho")

def end_of_work_week():
    print("Fim da semana de trabalho")

# Configuração da tarefa diária
schedule.every().day.at("07:30").do(start_of_work_day)

# Configuração da tarefa semanal
schedule.every().friday.at("17:00").do(end_of_work_week)

while True:
    schedule.run_pending()
    time.sleep(1)