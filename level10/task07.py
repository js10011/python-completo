# Recebendo a string do usuário
user_input = input("Digite uma string: ")

# Removendo espaços no início e no fim da string
stripped_string = user_input.strip()
print("String sem espaços no início e no fim:", stripped_string)

# Convertendo todos os caracteres da string para minúsculas
lower_string = stripped_string.lower()
print("String em minúsculas:", lower_string)

# Convertendo todos os caracteres da string para maiúsculas
upper_string = stripped_string.upper()
print("String em maiúsculas:", upper_string)