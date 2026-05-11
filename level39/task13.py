from datetime import datetime
import pytz
from tzlocal import get_localzone


# Solicitando entrada de dados do usuário
event_datetime_str = input("Insira a data e hora do evento (YYYY-MM-DD HH:MM): ")
event_timezone_str = input("Insira o fuso horário do evento (por exemplo, Europe/London): ")

# Determinando o fuso horário local do usuário
local_timezone = get_localzone()

# Criando um objeto datetime para o evento, considerando o fuso horário especificado
event_timezone = pytz.timezone(event_timezone_str)
event_datetime = event_timezone.localize(datetime.strptime(event_datetime_str, '%Y-%m-%d %H:%M'))

# Obtendo o tempo atual no fuso horário local do usuário
current_datetime = datetime.now(local_timezone)

# Convertendo a data e hora do evento para o fuso horário local do usuário
event_in_local_tz = event_datetime.astimezone(local_timezone)

# Calculando a diferença entre o tempo atual e o tempo do evento
delta = event_in_local_tz - current_datetime

# Obtendo a quantidade de dias, horas e minutos
days = delta.days
seconds = delta.seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60

# Exibindo o resultado
print(f"Faltam {days} dias, {hours} horas e {minutes} minutos para o evento.")