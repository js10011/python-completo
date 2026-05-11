file = None 
try:
    file = open('example.txt', 'a')
    file.write("Nova linha.")
except FileNotFoundError:
    print("Arquivo não encontrado.")
finally:
    if file:
        file.close()