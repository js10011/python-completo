from datetime import datetime, timedelta
import pytz

# Definindo o fuso horário para Nova York
ny_tz = pytz.timezone('America/New_York')

# Criando objetos datetime para as datas e horários indicados
dt_march = datetime(2024, 3, 10, 12, 0, 0)
dt_november = datetime(2024, 11, 10, 12, 0, 0)

# Localizando esses objetos para Nova York
dt_march_ny = ny_tz.localize(dt_march, is_dst=None)
dt_november_ny = ny_tz.localize(dt_november, is_dst=None)

# Determinando se o horário está no período de horário de verão
is_dst_march = dt_march_ny.dst() != timedelta(0)
is_dst_november = dt_november_ny.dst() != timedelta(0)

# Imprimindo os resultados
print("Data:", dt_march_ny.strftime('%Y-%m-%d %H:%M:%S'), "| Horário de verão:", is_dst_march)
print("Data:", dt_november_ny.strftime('%Y-%m-%d %H:%M:%S'), "| Horário de verão:", is_dst_november)