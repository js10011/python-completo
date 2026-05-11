from PIL import Image

# Abrimos a imagem original
input_image_path = 'input.jpg'
image = Image.open(input_image_path)

# Inverter a imagem horizontalmente
flipped_horizontal = image.transpose(Image.FLIP_LEFT_RIGHT)
# Salvar o resultado
flipped_horizontal.save('flipped_horizontal.jpg')

# Inverter a imagem verticalmente
flipped_vertical = image.transpose(Image.FLIP_TOP_BOTTOM)
# Salvar o resultado
flipped_vertical.save('flipped_vertical.jpg')