from datetime import datetime

def log_event(event_description, log_file):
    # Obtemos a hora atual e a formatamos
    current_time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    # Formamos a string de log
    log_entry = f"{current_time} {event_description}\n"

    # Abrimos o arquivo de logs no modo de adição e registramos o evento
    with open(log_file, "a") as file:
        file.write(log_entry)


log_file = "events.log"
# Exemplo de registro de vários eventos
events = ["Evento 1", "Evento 2", "Evento 3"]

for event in events:
    log_event(event, log_file)