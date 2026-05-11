from datetime import datetime, timedelta

# Pegamos a data atual
current_date = datetime.now().date()

# Recebemos a data do usuário no formato "YYYY-MM-DD"
user_input = input("Digite a data no formato YYYY-MM-DD: ")

# Convertendo a string inserida em um objeto de data
target_date = datetime.strptime(user_input, "%Y-%m-%d").date()

# Calculamos a diferença entre a data alvo e a data atual
difference = target_date - current_date

# Exibimos a quantidade de dias restantes
print(f"Quantidade de dias até a data informada: {difference.days}")