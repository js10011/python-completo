from datetime import datetime, timedelta, timezone

# Obter a hora atual no fuso horário UTC
current_utc_time = datetime.now(timezone.utc)

# Solicitar ao usuário o deslocamento em horas em relação ao UTC
offset_hours = int(input("Digite o deslocamento em relação ao UTC em horas: "))

# Criar um objeto de fuso horário com o deslocamento especificado
user_timezone = timezone(timedelta(hours=offset_hours))

# Converter a hora atual para o fuso horário especificado
current_user_time = current_utc_time.astimezone(user_timezone)

# Exibir a hora atual no UTC e no fuso horário especificado pelo usuário
print("Hora atual no UTC:", current_utc_time)
print(f"Hora atual no fuso horário com deslocamento de {offset_hours} hora(s):", current_user_time)