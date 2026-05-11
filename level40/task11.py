from datetime import datetime
import pytz

# Criamos o objeto datetime para Los Angeles
la_timezone = pytz.timezone('America/Los_Angeles')
la_time = la_timezone.localize(datetime(2023, 12, 25, 15, 0, 0))

# Lista de fusos horários para conversão
timezones = {
    'Moscou': 'Europe/Moscow',
    'Nova Delhi': 'Asia/Kolkata',
    'Sydney': 'Australia/Sydney',
    'Rio de Janeiro': 'America/Sao_Paulo',
    'Cidade do Cabo': 'Africa/Johannesburg'
}

# Convertemos e exibimos o tempo para cada fuso horário
for city, zone in timezones.items():
    tz = pytz.timezone(zone)
    city_time = la_time.astimezone(tz)
    print(f"Horário do webinar em {city}: {city_time.strftime('%Y-%m-%d %H:%M:%S')}")