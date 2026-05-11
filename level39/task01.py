from datetime import datetime

# Extração da data atual
current_date = datetime.now()

# Formatação da data em string "AAAA-MM-DD"
formatted_date = current_date.strftime("%Y-%m-%d")

# Exibição na tela
print(formatted_date)


from datetime import datetime

# Criamos um objeto datetime para a data e hora atuais
current_datetime = datetime.now()

# Especificamos a data de nascimento
birthday = datetime(year=1990, month=1, day=1)  # Substitua pela data de nascimento real

# Calculamos a diferença entre a data atual e a data de aniversário
difference = current_datetime - birthday

# Exibimos o número de dias entre as datas
print(f"Quantidade de dias entre a data atual e a data de aniversário: {difference.days}")