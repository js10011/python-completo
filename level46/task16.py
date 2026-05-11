import os
from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_folder, output_folder, watermark_text, font_path, font_size):
    # Cria a pasta de saída se ela não existir
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Percorre todos os arquivos na pasta de imagens
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff')):
            # Abre a imagem
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)
            
            # Cria um objeto para desenho
            drawable = ImageDraw.Draw(image)
            width, height = image.size
            
            # Carrega a fonte
            font = ImageFont.truetype(font_path, font_size)
            
            # Tamanho do texto
            text_width, text_height = drawable.textsize(watermark_text, font=font)
            
            # Posição do texto no canto inferior direito
            position = (width - text_width - 10, height - text_height - 10)
            
            # Adiciona a marca d'água
            drawable.text(position, watermark_text, font=font, fill=(255, 255, 255, 128))
            
            # Salva a imagem
            output_path = os.path.join(output_folder, filename)
            image.save(output_path)

# Parâmetros
input_folder = 'images'
output_folder = 'watermarked_images'
watermark_text = 'Sample Watermark'
font_path = 'arial.ttf'  # caminho para o arquivo de fonte Arial
font_size = 30

add_watermark(input_folder, output_folder, watermark_text, font_path, font_size)