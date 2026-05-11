from PIL import Image

# Carregamento de duas imagens
image1 = Image.open('image1.jpg')
image2 = Image.open('image2.jpg')

# Verificação se as imagens são do mesmo tamanho
if image1.size != image2.size:
    raise ValueError("As imagens devem ter o mesmo tamanho!")

# Sobreposição de uma imagem sobre a outra
image1.paste(image2, (0, 0), image2)

# Salvamento da imagem final
image1.save('combined_image.jpg', 'JPEG')