import os
from PIL import Image


# Função para redimensionar imagens
def resize_images(input_folder, output_folder, size=(320, 320)):
    # Cria a pasta para salvar as imagens redimensionadas, se ela não existir
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Percorre os arquivos na pasta
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            # Redimensiona a imagem usando suavização
            img = img.resize(size, Image.ANTIALIAS)
            # Salva a imagem redimensionada na pasta de destino
            img.save(os.path.join(output_folder, filename))


# Função para criar animação GIF a partir de imagens
def create_gif_from_images(image_folder, output_gif, duration=100):
    images = []
    # Carrega as imagens e as ordena pelo nome do arquivo
    for filename in sorted(os.listdir(image_folder)):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            img_path = os.path.join(image_folder, filename)
            images.append(Image.open(img_path))

    # Se as imagens foram carregadas, cria o GIF
    if images:
        images[0].save(
            output_gif,
            save_all=True,
            append_images=images[1:],  # Adiciona as outras imagens à primeira
            duration=duration,  # Duração da exibição de cada quadro (em milissegundos)
            loop=0  # Loop infinito
        )


# Função principal
def main():
    input_folder = 'input_images'  # Pasta com as imagens originais
    temp_folder = 'temp_resized_images'  # Pasta temporária para as imagens redimensionadas
    output_gif = 'resized_animation.gif'  # Nome do arquivo GIF de saída

    # Redimensiona as imagens e as salva na pasta temporária
    resize_images(input_folder, temp_folder)

    # Cria o GIF a partir das imagens redimensionadas
    create_gif_from_images(temp_folder, output_gif)

    # Limpeza dos arquivos temporários
    for filename in os.listdir(temp_folder):
        file_path = os.path.join(temp_folder, filename)
        os.remove(file_path)  # Remove as imagens temporárias
    os.rmdir(temp_folder)  # Remove a pasta temporária


# Executa o programa
main()