from datetime import datetime, timedelta

# Função para arredondar o tempo para o intervalo de 15 minutos mais próximo
def round_time_to_nearest_minute(dt):
    # Calcula o número de minutos passados desde o último intervalo de 15 minutos
    minutes = dt.minute % 15
    # Determina se deve arredondar para baixo ou para cima
    if minutes < 7.5:
        delta = -minutes  # Arredondar para baixo
    else:
        delta = 15 - minutes  # Arredondar para cima
    # Arredonda segundos e microsegundos para zero
    dt_rounded = dt + timedelta(minutes=delta, seconds=-dt.second, microseconds=-dt.microsecond)
    return dt_rounded

# Testa a função com o tempo atual
current_time = datetime.now()
rounded_time = round_time_to_nearest_minute(current_time)
print("Tempo atual:", current_time)
print("Tempo arredondado:", rounded_time)