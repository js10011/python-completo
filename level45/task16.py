from PIL import Image

# Função para criar colagem com imagem de fundo e quatro imagens incorporadas
def create_collage(background_path, images_paths, output_path='collage.jpg'):
    # Carrega a imagem de fundo
    background = Image.open(background_path)
    bg_width, bg_height = background.size  # Determina a largura e altura do fundo

    # Carrega as imagens a serem inseridas e redimensiona para metade do tamanho da imagem de fundo
    images = [Image.open(img_path).resize((bg_width // 2, bg_height // 2)) for img_path in images_paths]

    # Insere as imagens nos quatro cantos da imagem de fundo
    background.paste(images[0], (0, 0))  # Inserção no canto superior esquerdo
    background.paste(images[1], (bg_width // 2, 0))  # Inserção no canto superior direito
    background.paste(images[2], (0, bg_height // 2))  # Inserção no canto inferior esquerdo
    background.paste(images[3], (bg_width // 2, bg_height // 2))  # Inserção no canto inferior direito

    # Salva o colagem final
    background.save(output_path)

# Exemplo de uso
create_collage('background.jpg', ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg'])