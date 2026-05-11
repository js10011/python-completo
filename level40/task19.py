import csv
from datetime import datetime, timedelta

# Função para arredondar o tempo para o intervalo de 10 minutos mais próximo
def round_time_to_nearest_10_minutes(time):
    """Arredonda o objeto de tempo passado para o intervalo de 10 minutos mais próximo."""
    discard = timedelta(minutes=time.minute % 10, seconds=time.second,
                        microseconds=time.microsecond)
    time -= discard  # Remove minutos e segundos desnecessários
    if discard >= timedelta(minutes=5):  # Verifica se arredonda para cima ou para baixo
        time += timedelta(minutes=10)
    return time

# Função para calcular o tempo total de trabalho com base nos intervalos arredondados
def calculate_work_time(time_pairs):
    """Calcula o tempo total de trabalho com base nos pares de tempo arredondados."""
    total_time = timedelta()  # Valor inicial para somar o tempo
    rounded_time_pairs = []  # Lista para armazenar intervalos arredondados
    for start_time, end_time in time_pairs:
        rounded_start = round_time_to_nearest_10_minutes(start_time)
        rounded_end = round_time_to_nearest_10_minutes(end_time)
        work_duration = rounded_end - rounded_start  # Calcula o tempo de trabalho
        total_time += work_duration  # Adiciona o tempo de trabalho ao tempo total
        rounded_time_pairs.append((rounded_start, rounded_end))  # Armazena os intervalos arredondados
    return total_time, rounded_time_pairs

# Função para gerar um relatório em formato CSV com dados de horas de trabalho dos funcionários
def generate_report(employee_data, output_csv_file):
    """Cria um relatório CSV de horas de trabalho dos funcionários."""
    with open(output_csv_file, mode='w', newline='') as csvfile:
        fieldnames = ['Nome', 'Marcações de tempo arredondadas', 'Tempo total de trabalho']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()  # Escreve os cabeçalhos das colunas
        for employee, time_pairs in employee_data.items():
            total_time, rounded_time_pairs = calculate_work_time(time_pairs)
            # Converte os intervalos arredondados em strings
            rounded_time_str = '; '.join(
                [f"{start.strftime('%H:%M')} - {end.strftime('%H:%M')}" for start, end in rounded_time_pairs]
            )
            total_time_str = str(total_time)  # Tempo total de trabalho em formato de string
            writer.writerow({
                'Nome': employee,
                'Marcações de tempo arredondadas': rounded_time_str,
                'Tempo total de trabalho': total_time_str
            })

# Função principal para teste
def main():
    # Exemplo de dados de entrada
    employee_data = {
        "Alice": [
            (datetime(2023, 10, 4, 9, 12), datetime(2023, 10, 4, 17, 45)),
            (datetime(2023, 10, 5, 9, 5), datetime(2023, 10, 5, 17, 50))
        ],
        "Bob": [
            (datetime(2023, 10, 4, 8, 31), datetime(2023, 10, 4, 16, 55)),
            (datetime(2023, 10, 5, 8, 40), datetime(2023, 10, 5, 17, 15))
        ]
    }

    output_csv_file = 'work_report.csv'  # Nome do arquivo para o relatório
    generate_report(employee_data, output_csv_file)  # Geração do relatório
    print(f"Relatório criado com sucesso: {output_csv_file}")

# Executa o programa
main()