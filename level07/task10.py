# Remoção de elemento

# Escreva um programa que crie uma lista de 5 elementos, solicite ao usuário o índice do elemento a ser removido
# e remova o elemento desse índice usando o método pop().
# O programa deve imprimir a lista atualizada e o elemento removido.
# Se o índice não existir, o programa deve exibir uma mensagem sobre isso.

# Escreva seu código aqui
linguagem = ['Python', 'java', 'javacript', 'c#', 'ruby']
print(f"Lista atual:\n{linguagem}")
removL= int(input("Digite um item para eliminar: "))

try:
    ligua_remov = linguagem.pop(removL)
    print(f"Lista atualizada:\n{linguagem}\nItem removido {ligua_remov}")
except:
    print("Índice inválido")