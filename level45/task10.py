from PIL import Image

# Abre a imagem original
input_image_path = "input_image.jpg"  # substitua pelo caminho para a sua imagem
image = Image.open(input_image_path)

# Rotaciona a imagem em 90 graus no sentido anti-horário
rotated_90 = image.rotate(90, expand=False)
rotated_90.save("rotated_90.jpg")

# Rotaciona a imagem em 45 graus com o parâmetro expand=True
rotated_expanded_45 = image.rotate(45, expand=True)
rotated_expanded_45.save("rotated_expanded_45.jpg")