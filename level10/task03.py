# Busca de substring.

# Escreva um programa que recebe uma string e uma substring do usuário.
# O programa deve verificar se a substring está contida na string usando o operador in,
# encontrar a primeira ocorrência da substring usando o método find() e
# contar o número de ocorrências da substring usando o método count().
# O programa deve exibir todos os resultados.

# Escreva o seu código aqui
# Entrada de string e substring do usuário
string = input("Digite uma string: ")
substring = input("Digite uma substring: ")

# Verificação da presença da substring na string usando o operador in
is_in = substring in string

# Encontrando a primeira ocorrência da substring usando o método find()
first_occurrence = string.find(substring)

# Contando o número de ocorrências da substring usando o método count()
count_occurrences = string.count(substring)

# Exibição dos resultados
print(f"A substring está contida na string: {is_in}")
print(f"Primeira ocorrência da substring na string: {first_occurrence}")
print(f"Número de ocorrências da substring na string: {count_occurrences}")