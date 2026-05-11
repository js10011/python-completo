from datetime import datetime
import pytz

# Solicitar ao usuário o horário original e o fuso horário
original_time_str = input("Digite o horário no formato 'YYYY-MM-DD HH:MM:SS': ")
original_zone_str = input("Digite o fuso horário original (por exemplo, Europe/Moscow): ")
target_zone_str = input("Digite o fuso horário de destino (por exemplo, Europe/Paris): ")

# Analisar o horário inserido
original_time = datetime.strptime(original_time_str, '%Y-%m-%d %H:%M:%S')

# Obter o fuso horário usando pytz
original_zone = pytz.timezone(original_zone_str)

target_zone = pytz.timezone(target_zone_str)

# Vincular o horário ao fuso horário
original_time = original_zone.localize(original_time)

# Converter o horário para UTC
utc_time = original_time.astimezone(pytz.utc)
print("Hora em UTC:", utc_time.strftime('%Y-%m-%d %H:%M:%S'))

# Converter o horário para o fuso horário de destino
target_time = utc_time.astimezone(target_zone)
print(f"Hora em {target_zone_str}:", target_time.strftime('%Y-%m-%d %H:%M:%S'))