# Reagrupamento.

# Escreva um programa que receba uma string de várias palavras separadas por vírgulas do usuário.
# O programa deve:
# Dividir a string em uma lista de palavras usando o método split().
# Unir esta lista de palavras em uma única string usando o método join(), separando as palavras com espaços.
# Exibir os resultados de cada operação.

# Escreva o seu código aqui

input_str = input("Digite uma string de várias palavras separadas por vírgulas: ")

# Divisão da string em uma lista de palavras
words_list = input_str.split(',')

# Exibição da lista de palavras
print("Lista de palavras:", words_list)

# União da lista de palavras em uma única string com espaços
joined_str = ' '.join(words_list)

# Exibição da string unida
print("String unida:", joined_str)