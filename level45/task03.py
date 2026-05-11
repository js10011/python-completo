from PIL import Image, ImageEnhance

# Abertura da imagem
image_path = 'input_image.jpg'  # Substitua pelo caminho para sua imagem
image = Image.open(image_path)

# Rotação da imagem 90 graus no sentido anti-horário
rotated_image = image.rotate(90, expand=True)

# Modificação do brilho da imagem (redução pela metade)
enhancer = ImageEnhance.Brightness(rotated_image)
darker_image = enhancer.enhance(0.5)

# Salvar imagem processada
output_image_path = 'output_image.jpg'
darker_image.save(output_image_path)

# Exibição da imagem processada na tela
darker_image.show()