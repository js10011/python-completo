import schedule
import time

def job():
    print("Procurou hora")

# Configura a tarefa para execução a cada hora
schedule.every().hour.do(job)

while True:
    # Verifica se há tarefas para execução
    schedule.run_pending()
    # Atraso de 1 minuto para evitar uso excessivo do processador
    time.sleep(60)