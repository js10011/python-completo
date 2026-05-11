import datetime

# Solicita ao usuário para inserir os números para divisão
x = float(input("Digite o dividendo: "))
y = float(input("Digite o divisor: "))

# Tenta realizar a divisão e trata o erro de divisão por zero
try:
    result = x / y
    print(f"Resultado da divisão: {result}")

# Faz o log do erro em um arquivo se ocorreu divisão por zero
except ZeroDivisionError as e:
    # Abre o arquivo para gravar o erro
    with open("error_log.txt", "a") as log_file:
        # Obtém o horário atual e o formata
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Grava o erro no arquivo de log
        log_file.write(f"{current_time} - Error: {e}\n")
    print("Erro: Divisão por zero não é possível. Detalhes foram gravados em error_log.txt.")