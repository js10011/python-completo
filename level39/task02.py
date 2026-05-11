import time

start_time = time.time()  # Lembra o tempo atual
end_time = start_time + 60  # Define o tempo de término para 60 segundos (1 minuto)

while time.time() < end_time:  # O loop vai funcionar até passar um minuto
    print("Pora fazer uma pausa!")
    time.sleep(10)  # Pausa de 10 segundos entre as exibições da mensagem