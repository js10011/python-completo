import datetime
import time

while True:
    # Obtém o horário atual
    now = datetime.datetime.now()
    # Define o horário para execução (hoje às 8:00 da manhã)
    next_run_time = now.replace(hour=8, minute=0, second=0, microsecond=0)

    # Se já passou das 8:00 da manhã, planeja a execução para o próximo dia
    if now >= next_run_time:
        next_run_time += datetime.timedelta(days=1)

    # Calcula o tempo de espera até a próxima execução em segundos
    sleep_time = (next_run_time - now).total_seconds()
    print(f"Esperando {sleep_time:.2f} segundos até a próxima execução às 8:00.")

    # Pausa até a próxima execução
    time.sleep(sleep_time)

    # Exibe a mensagem de início de trabalho
    print("Pora levantar e começar a trabalhar!")