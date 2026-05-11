import os
from PIL import Image

# Pasta para salvar as miniaturas
output_folder = "thumbnails"

# Lista fixa de caminhos para as imagens
image_paths = [
    "path/to/image1.jpg",  # Substitua pelos caminhos reais das suas imagens
    "path/to/image2.jpg",
    "path/to/image3.jpg"
]

# Verifica e cria a pasta, se não existir
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Processamento de cada imagem da lista
for image_path in image_paths:
    try:
        # Abre a imagem
        with Image.open(image_path) as img:
            # Cria a miniatura com tamanho máximo de 200x200 pixels
            img.thumbnail((200, 200))

            # Define o novo nome do arquivo para a miniatura
            base_name = os.path.basename(image_path)
            new_name = f"thumb_{base_name}"
            output_path = os.path.join(output_folder, new_name)

            # Salva a miniatura na pasta especificada
            img.save(output_path)
            print(f"Miniatura salva como {output_path}")
    except IOError:
        print(f"Não é possível abrir o arquivo de imagem: {image_path}")
    except Exception as e:
        print(f"Erro ao processar {image_path}: {e}")