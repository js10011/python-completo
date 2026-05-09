elements = []
for _ in range(7):
    element = input("Digite um elemento: ")
    elements.append(element)

tuple_elements = tuple(elements)

print("Terceiro elemento a partir do final:", tuple_elements[-3])
print("Penúltimo elemento:", tuple_elements[-2])