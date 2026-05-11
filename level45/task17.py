from PIL import Image

# Carregamento de imagem
image = Image.open("input.jpg")

# Conversão para modo preto e branco (L)
gray_image = image.convert("L")
gray_image.save("output_gray.jpg")

# Conversão para modo CMYK
cmyk_image = image.convert("CMYK")
cmyk_image.save("output_cmyk.jpg")

# Conversão para modo RGBA
rgba_image = image.convert("RGBA")
rgba_image.save("output_rgba.png")