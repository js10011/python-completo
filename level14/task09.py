from datetime import date

# Solicitamos ao usuário o ano, mês e dia de nascimento
year = int(input("Digite o ano do seu nascimento: "))
month = int(input("Digite o mês do seu nascimento: "))
day = int(input("Digite o dia do seu nascimento: "))

# Criamos um objeto de data de nascimento
birth_date = date(year, month, day)

# Obtemos a data atual
current_date = date.today()

# Calculamos a diferença entre a data atual e a data de nascimento
days_difference = (current_date - birth_date).days

# Exibimos a quantidade de dias que passaram desde a data de nascimento
print(f"Quantidade de dias que passaram desde o seu nascimento: {days_difference}")