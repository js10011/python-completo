from PIL import Image, ImageEnhance

# Carregamento da imagem
input_image = "input.jpg"
image = Image.open(input_image)

# Alteração de brilho
enhancer = ImageEnhance.Brightness(image)
bright_image = enhancer.enhance(1.5)  # Aumento de brilho em 50%
bright_image.save("output_brightness.jpg")

# Alteração de contraste
enhancer = ImageEnhance.Contrast(bright_image)
contrast_image = enhancer.enhance(1.5)  # Aumento de contraste em 50%
contrast_image.save("output_contrast.jpg")

# Alteração de saturação
enhancer = ImageEnhance.Color(contrast_image)
saturation_image = enhancer.enhance(0.5)  # Diminuição de saturação em 50%
saturation_image.save("output_saturation.jpg")