def parse_time_string(time_str):
    """Parsa a string de tempo e retorna horas e minutos como inteiros."""
    try:
        hours, minutes = map(int, time_str.split(':'))
        if not (0 <= hours < 24) or not (0 <= minutes < 60):
            raise ValueError("Tempo incorreto")
        return hours, minutes
    except ValueError:
        raise ValueError("Formato de tempo incorreto. Por favor, insira o tempo no formato HH:MM.")

def round_minutes_to_nearest_five(minutes):
    """Arredonda um dado número de minutos para o múltiplo de 5 mais próximo."""
    remainder = minutes % 5
    if remainder < 2.5:
        return minutes - remainder  # Arredondamento para baixo
    else:
        return minutes + (5 - remainder)  # Arredondamento para cima

def round_time_to_nearest_five_minutes(time_str):
    """Arredonda o tempo fornecido para os 5 minutos mais próximos."""
    hours, minutes = parse_time_string(time_str)  # Parso da string de tempo
    rounded_minutes = round_minutes_to_nearest_five(minutes)  # Arredondamento dos minutos

    # Se os minutos arredondados forem 60, adicionamos 1 hora e zeramos os minutos
    if rounded_minutes == 60:
        rounded_minutes = 0
        hours = (hours + 1) % 24  # Passa para a próxima hora considerando o formato de 24 horas

    # Retorna o tempo arredondado no formato de string
    return f"{hours:02}:{rounded_minutes:02}"

def get_time_input(prompt):
    """Solicita e arredonda a entrada de tempo do usuário."""
    while True:
        try:
            time_str = input(prompt)  # Solicita o tempo do usuário
            return round_time_to_nearest_five_minutes(time_str)  # Arredonda o tempo
        except ValueError as e:
            print(e)  # Exibe a mensagem de erro se o formato do tempo estiver incorreto

def main():
    print("Programa para arredondamento de tempo do horário de trabalho")
    start_time = get_time_input("Insira o horário de início (HH:MM): ")
    end_time = get_time_input("Insira o horário de término (HH:MM): ")

    print("Tempo arredondado:")
    print(f"Horário de início: {start_time}")
    print(f"Horário de término: {end_time}")

# Inicia o programa principal
main()