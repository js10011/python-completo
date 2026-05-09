N = int(input("Digite o número N: "))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(i * j, end='\t')
    print()