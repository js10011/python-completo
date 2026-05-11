def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

# Criação de contadores independentes
counter1 = make_counter()
counter2 = make_counter()

# Chamadas aos contadores e exibição do resultado na tela
print(counter1())  # 1
print(counter1())  # 2
print(counter2())  # 1
print(counter1())  # 3
print(counter2())  # 2