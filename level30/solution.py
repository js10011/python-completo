from PIL import Image

# Abertura da imagem
image_path = "path/to/your/image.jpg"  # Substitua pelo caminho da sua imagem
image = Image.open(image_path)

# Extração das dimensões da imagem
width, height = image.size

# Exibição das dimensões no console
print(f"Tamanho da imagem: largura = {width} pixels, altura = {height} pixels")

# Exibição da imagem
image.show()