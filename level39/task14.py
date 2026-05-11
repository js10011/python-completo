import schedule
import time

def task():
    print("Executando tarefa")

# Configuração da execução da tarefa a cada minuto
schedule.every(1).minute.do(task)

# Loop infinito para operação contínua do programa
while True:
    schedule.run_pending()  # Verifica e executa as tarefas
    time.sleep(1)  # Pausa para reduzir a carga da CPU