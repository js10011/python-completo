from datetime import datetime, timedelta

# Criação de um objeto datetime para a data e hora atuais
current_datetime = datetime.now()

# Criação de timedelta para adicionar 7 dias
one_week = timedelta(days=7)

# Adição de 7 dias à data e hora atuais
next_week_datetime = current_datetime + one_week

# Exibição de ambos os objetos datetime
print("Data e hora atuais:", current_datetime)
print("Data e hora daqui a uma semana:", next_week_datetime)