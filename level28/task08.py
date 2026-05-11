import pandas as pd
import os
from glob import glob

# Caminho para o diretório com arquivos Excel
directory_path = 'path_to_directory' # Substitua pelo seu caminho

# Padrão para localização de arquivos
file_pattern = os.path.join(directory_path, 'sales_data_*.xlsx')

# Encontramos todos os arquivos que correspondem ao padrão
excel_files = glob(file_pattern)

# Lista para armazenar dados de todos os arquivos
dataframes = []

# Processamos cada arquivo encontrado
for file_path in excel_files:
    # Lemos dados do arquivo Excel atual
    df = pd.read_excel(file_path)
    # Adicionamos a coluna com o nome do arquivo
    df['Source File'] = os.path.basename(file_path)
    # Adicionamos o DataFrame na lista
    dataframes.append(df)

# Unificamos todos os DataFrames em um só
combined_df = pd.concat(dataframes, ignore_index=True)

# Exibimos o resultado
print(combined_df)