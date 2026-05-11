import schedule
import time

# Função que será executada de manhã
def good_morning():
    print("Bom dia")

# Função para verificação do sistema
def system_check():
    print("Verificação do sistema")

# Configuração da agenda de tarefas
schedule.every().day.at("08:00").do(good_morning)  # Executar todas as manhãs às 8:00
schedule.every().monday.at("15:00").do(system_check)  # Executar verificação do sistema às segundas-feiras às 15:00
schedule.every().wednesday.at("15:00").do(system_check)  # Executar verificação do sistema às quartas-feiras às 15:00

# Loop principal para executar as tarefas de acordo com a agenda
while True:
    schedule.run_pending()  # Verifica e executa as tarefas agendadas
    time.sleep(1)  # Pausa de 1 segundo antes da próxima verificação