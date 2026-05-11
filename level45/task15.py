from PIL import Image

def composite_images(image1_path, image2_path, mask_path, output_path):
    # Carregamento de imagens e máscara
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)
    mask = Image.open(mask_path)

    # Verificação se os tamanhos das imagens e da máscara coincidem
    if image1.size != image2.size or image1.size != mask.size:
        raise ValueError("Os tamanhos das imagens e da máscara devem coincidir.")

    # Criação da composição
    composited_image = Image.composite(image1, image2, mask)

    # Salvamento da imagem composta
    composited_image.save(output_path, "JPEG")

# Exemplo de uso da função
image1_path = 'image1.jpg'  # caminho para a primeira imagem
image2_path = 'image2.jpg'  # caminho para a segunda imagem
mask_path = 'mask.png'      # caminho para a imagem de máscara
output_path = 'composited_image.jpg'  # caminho para salvar o resultado

composite_images(image1_path, image2_path, mask_path, output_path)