import schedule
import time

# Função para lembrete de pausa
def reminder():
    print("Lembrete: hora de fazer uma pausa!")

# Configuração do agendamento: executa a função de lembrete a cada hora
schedule.every().hour.do(reminder)

# Loop principal para executar tarefas agendadas
while True:
    # Executa todas as tarefas agendadas para o tempo atual
    schedule.run_pending()
    # Pausa de 1 segundo para reduzir a carga no processador
    time.sleep(1)


from plyer import notification

notification.notify(
    title='Lembrete',
    message='Não se esqueça da reunião às 15:00 hoje',
    app_name='Notifier',
    timeout=10
)