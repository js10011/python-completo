import os
from PIL import Image

# Recupera a lista de todos os arquivos no diretório atual
files = os.listdir('.')

# Filtra os arquivos para manter apenas os com extensão .png
png_files = [file for file in files if file.endswith('.png')]

# Inicializa o contador de arquivos processados com sucesso
successful_conversions = 0

for png_file in png_files:
    try:
        # Abre a imagem
        with Image.open(png_file) as img:
            # Define o novo nome do arquivo com extensão .webp
            webp_file = os.path.splitext(png_file)[0] + '.webp'

            # Converte e salva a imagem no formato WebP com qualidade 75
            img.save(webp_file, 'WEBP', quality=75)

            # Incrementa o contador de conversões bem-sucedidas
            successful_conversions += 1
    except Exception as e:
        print(f"Não foi possível processar o arquivo {png_file}: {e}")

# Exibe a quantidade de arquivos processados com sucesso
print(f"Quantidade de arquivos processados com sucesso: {successful_conversions}")