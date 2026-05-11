from datetime import datetime
import pytz

# Definimos os fusos horários
time_zones = {
    'New York': 'America/New_York',
    'London': 'Europe/London',
    'Tokyo': 'Asia/Tokyo'
}

# Obtemos e exibimos a hora atual para cada fuso horário
for city, tz_name in time_zones.items():
    tz = pytz.timezone(tz_name)
    current_time = datetime.now(tz)
    print(f"O horário atual em {city} ({tz_name}) é: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")