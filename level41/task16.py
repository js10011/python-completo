import pandas as pd
import matplotlib.pyplot as plt

# Carregamento de dados dos arquivos CSV
def load_temperature_data(file_path):
    # Usar pandas para carregar o arquivo CSV
    data = pd.read_csv(file_path)
    # Supõe-se que os dados de temperatura estão na coluna 'temperature'
    return data['temperature']

# Construção do histograma
def plot_histogram(data1, data2, month1, month2):
    plt.figure(figsize=(12, 6))

    # Primeiro histograma
    plt.subplot(1, 2, 1)
    plt.hist(data1, bins=10, range=(data1.min(), data1.max()), alpha=0.7, label=month1)
    plt.title(f'Histograma de Temperaturas: {month1}')
    plt.xlabel('Temperatura')
    plt.ylabel('Número de dias')
    plt.grid(True)

    # Segundo histograma
    plt.subplot(1, 2, 2)
    plt.hist(data2, bins=10, range=(data2.min(), data2.max()), alpha=0.7, label=month2)
    plt.title(f'Histograma de Temperaturas: {month2}')
    plt.xlabel('Temperatura')
    plt.grid(True)

    # Exibição dos gráficos
    plt.tight_layout()
    plt.show()

# Caminho dos arquivos CSV para cada mês
january_file_path = 'january_temperatures.csv'
february_file_path = 'february_temperatures.csv'

# Carregamento de dados
january_data = load_temperature_data(january_file_path)
february_data = load_temperature_data(february_file_path)

# Construção e exibição do histograma
plot_histogram(january_data, february_data, 'Janeiro', 'Fevereiro')