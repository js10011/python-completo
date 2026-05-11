from PIL import Image

# Criamos uma nova imagem de 300x300 pixels no formato RGBA
# A cor de fundo (0, 0, 0, 0) significa completamente transparente
image = Image.new("RGBA", (300, 300), (0, 0, 0, 0))

# Salvamos a imagem com o nome "transparent_image.png"
image.save("transparent_image.png")