# Recebemos uma string do usuário
input_string = input("Digite uma string: ")

# Extração da substring do 3º ao 8º caractere (índice) inclusive
substring1 = input_string[3:9]

# Extração da substring do 5º caractere (índice) até o final da string
substring2 = input_string[5:]

# Exibição de ambas as substrings
print("Substring do 3º ao 8º caractere inclusive:", substring1)
print("Substring do 5º caractere até o final da string:", substring2)