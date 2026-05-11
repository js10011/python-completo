import schedule
import time

def reminder():
    print("Pora verificar o e-mail!")

# Configurar a tarefa para execução diária às 10:00
schedule.every().day.at("10:00").do(reminder)

# Loop infinito para funcionamento contínuo do programa
while True:
    schedule.run_pending()  # Verificação do agendamento das tarefas
    time.sleep(60)  # Pausa para reduzir a carga no processador