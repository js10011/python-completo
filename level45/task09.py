from PIL import Image

# Parâmetros para o corte
input_image_path = 'input.jpg'  # Caminho para a imagem original
output_image_path = 'basic_cropped.jpg'  # Caminho para salvar a imagem recortada
crop_width = 200
crop_height = 200

# Abrindo a imagem original
image = Image.open(input_image_path)

# Obtendo as dimensões da imagem original
width, height = image.size

# Calculando as coordenadas para o corte central
left = (width - crop_width) / 2
top = (height - crop_height) / 2
right = (width + crop_width) / 2
bottom = (height + crop_height) / 2

# Realizando o corte
cropped_image = image.crop((left, top, right, bottom))

# Salvando a imagem recortada
cropped_image.save(output_image_path)