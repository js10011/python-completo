from PIL import Image
import os

# Definimos os caminhos para as imagens de entrada e saída
input_path = 'input.jpg'  # Informe o caminho para a sua imagem
output_path = 'output.png'  # Informe o caminho para salvar a nova imagem

# Abrimos a imagem
with Image.open(input_path) as img:
    # Obtemos os dados EXIF
    exif_data = img.info.get('exif')

    # Conversão para outro formato e salvamento com otimização e dados EXIF
    img.save(output_path, format='PNG', optimize=True, exif=exif_data)

print(f"A imagem foi convertida e salva com sucesso em {output_path}.")