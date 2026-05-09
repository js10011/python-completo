# Uso de variável global

# Escreva um programa que tenha uma variável global counter, igual a 0.
# Escreva uma função increment_counter(), que aumenta o valor dessa variável em 1 toda vez que é chamada.
# Em seguida, chame essa função várias vezes e exiba o valor da variável global counter.

# Escreva seu código aqui
counter = 0

def increment_counter():
    
    global counter
    counter += 1
    print(counter)
    
increment_counter()
increment_counter()
increment_counter()

  