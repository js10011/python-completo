from PIL import Image, ImageOps

# Caminho para as imagens original e de resultado
input_image_path = 'input.jpg'  # Indique o caminho atual para a sua imagem
output_image_path = 'fitted_image.jpg'

# Tamanho especificado para redimensionamento e recorte
size = (300, 300)

# Abrindo a imagem
with Image.open(input_image_path) as image:
    # Redimensionamento e recorte usando ImageOps.fit
    fitted_image = ImageOps.fit(image, size, method=Image.LANCZOS)
    # Salvando o resultado no caminho especificado
    fitted_image.save(output_image_path, 'JPEG')

print(f"Imagem salva em '{output_image_path}' com tamanho {size}.")