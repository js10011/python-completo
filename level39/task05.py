from datetime import datetime

# Solicita a entrada da primeira data
date_str1 = input("Digite a primeira data (AAAA-MM-DD): ")
# Solicita a entrada da segunda data
date_str2 = input("Digite a segunda data (AAAA-MM-DD): ")

# Conversão das strings para objetos datetime
date1 = datetime.strptime(date_str1, "%Y-%m-%d")
date2 = datetime.strptime(date_str2, "%Y-%m-%d")

# Cálculo da diferença entre as datas
delta = date2 - date1
# Exibe a quantidade de dias
print("Quantidade de dias entre as datas:", abs(delta.days))

from datetime import datetime

# Obter o tempo atual
current_time = datetime.now()

# Extrair e imprimir ano, mês, dia, hora, minuto e segundo
print(current_time.year)
print(current_time.month)
print(current_time.day)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)