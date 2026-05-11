from PIL import Image

# Caminho para as imagens de entrada e saída
input_image_path = 'input_image.jpg'  # Indique o caminho para a sua imagem original
output_image_path = 'combined_processed_image.jpg'  # Caminho para salvar a imagem processada

# Abrindo a imagem
with Image.open(input_image_path) as img:
    # Obtendo as dimensões da imagem
    width, height = img.size

    # Calculando as dimensões e coordenadas para o recorte da parte central
    new_width = width // 2
    new_height = height // 2
    left = (width - new_width) // 2
    upper = (height - new_height) // 2
    right = left + new_width
    lower = upper + new_height

    # Recorte da imagem
    cropped_img = img.crop((left, upper, right, lower))

    # Giro da imagem em 30 graus
    rotated_img = cropped_img.rotate(30, expand=True)

    # Reflexão da imagem horizontalmente
    final_img = rotated_img.transpose(Image.FLIP_LEFT_RIGHT)

    # Salvando a imagem resultante
    final_img.save(output_image_path)