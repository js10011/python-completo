import schedule
import time
import logging

# Configurando o log para gravação no console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def reminder():
    # Tarefa que exibe o lembrete
    logging.info("É hora de fazer o plano semanal!")

# Configuração do agendamento para todos os domingos às 18:00
schedule.every().sunday.at("18:00").do(reminder)

print("Programa iniciado. Aguardando execução de tarefas.")

while True:
    # Verificação do agendamento
    schedule.run_pending()
    # Atraso de 1 minuto para evitar sobrecarga excessiva do processador
    time.sleep(60)