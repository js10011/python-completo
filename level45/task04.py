import os
from PIL import Image, ImageEnhance

# Indicação dos diretórios para imagens de entrada e saída
input_dir = "path_to_input_directory"  # Indique o caminho para seu diretório com imagens
output_dir = "path_to_output_directory"  # Indique o caminho para salvar as imagens processadas

# Criação do diretório de saída, se ele não existir
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Processamento de todos os arquivos no diretório de entrada
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
        # Caminho completo para o arquivo de entrada e saída
        input_file_path = os.path.join(input_dir, filename)
        output_file_path = os.path.join(output_dir, filename)

        # Abertura do arquivo de imagem
        with Image.open(input_file_path) as img:
            # Redimensionamento da imagem para 300x300
            img = img.resize((300, 300), Image.ANTIALIAS)

            # Rotação da imagem em 45 graus
            img = img.rotate(45, expand=True)

            # Aumento do brilho em 1,5
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(1.5)

            # Salvamento da imagem modificada no diretório de saída
            img.save(output_file_path)

print("Processamento de imagens concluído.")