import schedule
import time

# Função para lembrar da necessidade de preparar o relatório
def remind():
    print("É hora de preparar o relatório!")

# Configuração da agenda da tarefa para cada dia útil às 8:30 da manhã
schedule.every().monday.at("08:30").do(remind)    # Segunda-feira
schedule.every().tuesday.at("08:30").do(remind)   # Terça-feira
schedule.every().wednesday.at("08:30").do(remind) # Quarta-feira
schedule.every().thursday.at("08:30").do(remind)  # Quinta-feira
schedule.every().friday.at("08:30").do(remind)    # Sexta-feira

# Loop principal para executar as tarefas de acordo com a agenda
while True:
    schedule.run_pending()  # Executa as tarefas agendadas
    time.sleep(1)  # Pausa de 1 segundo antes da próxima verificação