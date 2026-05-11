import os
from PIL import Image

# Diretórios de entrada e saída
input_dir = 'input_images'
output_dir = 'output_images'

# Cria o diretório de saída se não existir
os.makedirs(output_dir, exist_ok=True)

# Tamanho desejado
desired_size = (640, 640)

# Itera sobre cada arquivo na pasta input_images
for filename in os.listdir(input_dir):
    # Verifica as extensões de interesse
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        # Abre a imagem
        with Image.open(os.path.join(input_dir, filename)) as img:
            # Redimensiona a imagem mantendo a proporção
            img.thumbnail(desired_size, Image.LANCZOS)  # Define o tamanho máximo de 640x640
            # Caminho para salvar a imagem processada
            output_path = os.path.join(output_dir, filename)
            # Salva a imagem
            img.save(output_path)