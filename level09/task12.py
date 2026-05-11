fruits = {"maçã", "banana", "laranja", "pêra"}

for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

index = int(input("Digite o número da fruta para substituição: ")) - 1
new_fruit = input("Digite o novo nome da fruta: ")

fruits_list = list(fruits)
fruits_list[index] = new_fruit
fruits = set(fruits_list)

print("Conjunto de frutas atualizado:", fruits)