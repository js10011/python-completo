from PIL import Image, ImageDraw

# Carregamento da imagem
input_image_path = "input_image.jpg"
output_image_path = "graphics_image.jpg"
image = Image.open(input_image_path)
draw = ImageDraw.Draw(image)

# Desenho da linha vermelha
draw.line((0, 0, image.width, image.height), fill="red", width=3)

# Desenho do retângulo azul
draw.rectangle((100, 100, 200, 200), outline="blue", width=3)

# Desenho do círculo verde
draw.ellipse((100, 100, 200, 200), outline="green", width=3)

# Salvar a imagem modificada
image.save(output_image_path)