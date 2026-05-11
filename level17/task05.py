# Conversão de Dados.

# Escreva uma função convert_and_sum que recebe dois argumentos como strings,
# converte-os em inteiros e retorna sua soma.
# Lide com exceções que podem ocorrer ao converter strings para números
# (por exemplo, se valores incorretos forem passados).

# Escreva seu código aqui

def convert_and_sum(str1, str2):
    try:
        num1 = int(str1)
        num2 = int(str2)
        return num1 + num2
    except ValueError:
        return "Valor incorreto"

# Exemplo de uso da função:
print(convert_and_sum("10", "20"))  # Resultado esperado: 30
print(convert_and_sum("a", "20"))  # Resultado esperado: Valor incorreto