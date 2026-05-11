from datetime import datetime

# Obtém a data e hora atuais
now = datetime.now()

# Formata a data e hora de acordo com o formato especificado
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")

# Exibe a data e hora formatada na tela
print(formatted_now)