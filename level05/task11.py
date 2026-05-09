# Você diz uma palavra, ele te dá um link

# Escreva um programa que crie duas listas, atribua uma
# delas a outra variável
# e verifique se ambas as variáveis apontam para
# o mesmo objeto.
# Use o operador is para verificar as referências.

# Escreva seu código aqui
l1= ["A", "B", "C", "D"]
l2 = l1    #["a", "b", "c", "d"]
if l1 is l2 :
    print("Objeto iguais")
else:
    print("Objeto diferentes")