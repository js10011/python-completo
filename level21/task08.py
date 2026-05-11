try:
    with open('example.txt', 'a', encoding='utf-8') as file:
        file.write('Nova linha.')
except FileNotFoundError:
    print("Arquivo não encontrado.")