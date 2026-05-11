initial_set = set()

for _ in range(5):
    number = int(input("Digite um número: "))
    number_set = {number}
    initial_set.update(number_set)

print(initial_set)