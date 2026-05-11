# Entrada da string pelo usuário
s = input("Digite uma string: ")

# Extrai os últimos três caracteres da string
last_three = s[-3:]

# Extrai a string, excluindo o último caractere
excluding_last = s[:-1]

# Inverte a string
reversed_s = s[::-1]

# Imprime todos os três resultados
print(last_three)
print(excluding_last)
print(reversed_s)