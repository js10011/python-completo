import os
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS


# Função para extrair dados EXIF de uma imagem
def get_exif_data(image):
    exif_data = image._getexif()
    if not exif_data:
        return None

    exif = {}
    # Itera sobre as tags e valores EXIF
    for tag_id, value in exif_data.items():
        tag = TAGS.get(tag_id, tag_id)
        exif[tag] = value

    return exif


# Função para obter a data de criação dos dados EXIF
def get_image_date(exif):
    if 'DateTimeOriginal' in exif:
        return exif['DateTimeOriginal']
    elif 'DateTime' in exif:
        return exif['DateTime']
    else:
        return None


# Função para classificar imagens por data extraída dos dados EXIF
def sort_images_by_date(source_folder):
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(('jpg', 'jpeg', 'png')):
            filepath = os.path.join(source_folder, filename)
            with Image.open(filepath) as img:
                exif = get_exif_data(img)  # Extrai os dados EXIF
                date_taken = None

                if exif:
                    date_taken = get_image_date(exif)  # Obtém a data dos dados EXIF

                if date_taken is None:
                    # Se os dados EXIF não existirem, usa a data atual
                    date_taken = datetime.now().strftime('%Y:%m:%d %H:%M:%S')

                # Forma o nome da pasta com base na data
                date_folder_name = datetime.strptime(date_taken, '%Y:%m:%d %H:%M:%S').strftime('%Y-%m-%d')
                target_folder = os.path.join(source_folder, date_folder_name)

                # Cria a pasta se ela não existir
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                # Move o arquivo para a pasta, preservando os metadados
                target_path = os.path.join(target_folder, filename)
                img.save(target_path)


# Especifique o caminho para a pasta com as imagens de origem
source_folder_path = "/path/to/source/folder"
sort_images_by_date(source_folder_path)