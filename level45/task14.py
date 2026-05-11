from PIL import Image

def blend_images(image_path1, image_path2, output_path, alpha=0.5):
    # Carregamento de imagens
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)

    # Verificação de mesmo tamanho de imagens
    if image1.size != image2.size:
        raise ValueError("As imagens devem ter o mesmo tamanho")

    # Mistura de imagens usando o método blend()
    blended_image = Image.blend(image1, image2, alpha)

    # Salvando o resultado
    blended_image.save(output_path)

# Caminho para as duas primeiras imagens
image_path1 = 'image1.jpg'  # especifique o caminho para a primeira imagem
image_path2 = 'image2.jpg'  # especifique o caminho para a segunda imagem

# Caminho para salvar a imagem misturada
output_path = 'blended_image.jpg'

# Mistura das imagens
blend_images(image_path1, image_path2, output_path)