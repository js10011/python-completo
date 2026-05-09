# Esperando "pare"

# Escreva um programa que cria uma lista vazia usando colchetes [] e adiciona nela elementos solicitados ao usuário.
# A entrada de elementos deve continuar até que o usuário insira a palavra "pare". Em seguida, o programa deve exibir a lista final.

# Escreva seu código aqui
lista=[]
pergunta = input("Adicione algo ou pare: ").lower()
while pergunta != "pare" :
    lista.append(pergunta)
    
    pergunta = input("Adicione algo ou pare: ").lower()
    
print(lista)