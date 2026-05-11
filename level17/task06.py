def process_input(input_string):
    try:
        if input_string == "":
            raise IndexError("String vazia")
        number = int(input_string)
        return number ** 2
    except ValueError:
        print("Erro: a string fornecida não é um número.")
    except IndexError:
        print("Erro: string vazia fornecida.")

# Exemplos de chamada da função
print(process_input("5"))         # Saída: 25
print(process_input("abc"))       # Saída: Erro: a string fornecida não é um número.
print(process_input(""))          # Saída: Erro: string vazia fornecida.