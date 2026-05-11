from PIL import Image
from PIL.ExifTags import TAGS

# Entrada do caminho da imagem
image_path = input("Digite o caminho da imagem: ")

try:
    # Abrimos a imagem e tentamos obter os dados EXIF
    with Image.open(image_path) as img:
        exif_data = img._getexif()

        if exif_data is not None:
            exif_dict = {}
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                exif_dict[tag_name] = value

            # Extração e exibição de determinados dados EXIF
            date_time = exif_dict.get('DateTime', 'Data e hora não especificadas')
            orientation = exif_dict.get('Orientation', 'Orientação não especificada')
            x_resolution = exif_dict.get('XResolution', 'Resolução X não especificada')
            y_resolution = exif_dict.get('YResolution', 'Resolução Y não especificada')

            print(f"Data e hora da captura: {date_time}")
            print(f"Orientação: {orientation}")
            print(f"Resolução X: {x_resolution}")
            print(f"Resolução Y: {y_resolution}")
        else:
            print("Dados EXIF não encontrados.")

except IOError:
    print("Erro ao abrir a imagem. Verifique o caminho do arquivo.")