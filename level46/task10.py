from PIL import Image
import os

# Caminho para as imagens original e comprimida
input_image_path = 'input_image.jpg'
output_image_path = 'compressed_image.jpg'

# Abertura da imagem usando Pillow
with Image.open(input_image_path) as img:
    # Salvando a imagem com qualidade 50 para compressão
    img.save(output_image_path, 'JPEG', quality=50)

# Obtendo o tamanho dos arquivos
input_size = os.path.getsize(input_image_path)
output_size = os.path.getsize(output_image_path)

# Exibindo os tamanhos dos arquivos
print(f"Tamanho do arquivo '{input_image_path}': {input_size} bytes")
print(f"Tamanho do arquivo '{output_image_path}': {output_size} bytes")