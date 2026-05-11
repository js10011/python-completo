def calculate_and_report(input_file, output_file):
    # Abre o arquivo de entrada para leitura
    with open(input_file, 'r') as file:
        # Lê cada linha do arquivo, remove espaços desnecessários e verifica se a linha é um número
        # Se a linha for um número, converte-a para int e adiciona à lista numbers
        numbers = [int(line.strip()) for line in file if line.strip().isdigit()]

    # Calcula a soma dos números na lista numbers
    total_sum = sum(numbers)
    # Calcula a média; se a lista estiver vazia, define a média como 0
    average = total_sum / len(numbers) if numbers else 0

    # Abre o arquivo de saída para escrever o relatório
    with open(output_file, 'w') as report:
        # Escreve no arquivo a linha com a soma e a média
        report.write(f"Soma: {total_sum}, Média: {average}")

# Executa a função com os nomes especificados do arquivo de entrada e saída
calculate_and_report('data.txt', 'report.txt')