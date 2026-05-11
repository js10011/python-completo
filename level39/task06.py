from datetime import datetime
import pytz

# Obtemos o horário atual
local_time = datetime.now()

# Definimos o horário local para UTC
utc_time = local_time.astimezone(pytz.utc)

# Definimos os fusos horários
timezones = {
    "US/Pacific": pytz.timezone("US/Pacific"),
    "Europe/London": pytz.timezone("Europe/London"),
    "Asia/Tokyo": pytz.timezone("Asia/Tokyo")
}

# Convertendo o tempo de UTC para cada um dos fusos horários especificados e exibindo o resultado
for tz_name, tz in timezones.items():
    converted_time = utc_time.astimezone(tz)
    print(converted_time.strftime(f"%Y-%m-%d %H:%M:%S {tz.zone}"))


import datetime

# Obtenção da data e hora atuais
current_datetime = datetime.datetime.now()

# Formatação da data e hora
formatted_datetime = current_datetime.strftime("%d.%m.%Y %H:%M:%S")

# Exibição do resultado na tela
print(formatted_datetime)