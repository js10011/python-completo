from datetime import datetime, timedelta

def round_time_to_nearest_half_hour(time_str):
    # Converte a string em um objeto de tempo
    time_obj = datetime.strptime(time_str, "%H:%M")
    
    # Obtém o número de minutos e arredonda para os 30 minutos mais próximos
    minutes = time_obj.minute
    if minutes < 15:
        minutes = 0
    elif minutes < 45:
        minutes = 30
    else:
        minutes = 0
        time_obj += timedelta(hours=1)
    
    # Define os minutos arredondados
    rounded_time = time_obj.replace(minute=minutes, second=0, microsecond=0)
    return rounded_time.strftime("%H:%M")

def process_time_stamps(time_stamps):
    rounded_times = []
    for time_str in time_stamps:
        rounded_times.append(round_time_to_nearest_half_hour(time_str))
    return rounded_times

# Exemplo de uso:
time_stamps = ["14:07", "15:29", "16:45", "22:59", "23:15"]
rounded_times = process_time_stamps(time_stamps)
print(rounded_times)