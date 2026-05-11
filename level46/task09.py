from PIL import Image

# Abrimos a imagem com o nome 'input_image.jpg'
input_image_path = 'input_image.jpg'
output_image_path = 'output_image.png'

# Usamos a biblioteca Pillow para abrir a imagem
with Image.open(input_image_path) as img:
    # Convertendo a imagem para o formato PNG
    img.save(output_image_path, 'PNG')

print(f"Imagem salva como {output_image_path}")