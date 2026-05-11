from datetime import datetime

# Solicita a data e hora do evento do usuário
user_input = input("Digite a data e hora do evento no formato AAAA-MM-DD HH:MM: ")

try:
    # Converte a string inserida em um objeto datetime
    event_time = datetime.strptime(user_input, "%Y-%m-%d %H:%M")
    current_time = datetime.now()

    # Compara o horário do evento com o horário atual
    if event_time == current_time.replace(second=0, microsecond=0):
        print("O evento começou!")
    elif event_time > current_time:
        print("O evento ainda não começou.")
    else:
        print("O evento já ocorreu.")

except ValueError:
    # Manipula o erro se a data inserida não corresponder ao formato
    print("Formato de data e hora incorreto. Por favor, use o formato AAAA-MM-DD HH:MM.")