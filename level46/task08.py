from PIL import Image

# Abertura da imagem
with Image.open('input_image.jpg') as img:
    # Determinação do formato da imagem
    image_format = img.format

# Exibição do formato da imagem
print(image_format)