from PIL import Image, ImageDraw, ImageFont

# Função para adicionar a marca d'água à imagem
def add_watermark(input_image_path, output_image_path, watermark_text):
    # Abrimos a imagem original e a convertimos para o modo RGBA para transparência
    image = Image.open(input_image_path).convert("RGBA")

    # Criamos uma nova camada com transparência para o texto
    txt = Image.new('RGBA', image.size, (255, 255, 255, 0))

    # Escolhemos a fonte e o tamanho (por padrão usamos a fonte do sistema)
    font = ImageFont.load_default()

    # Inicializamos o objeto para desenhar na camada de texto
    draw = ImageDraw.Draw(txt)

    # Calculamos o tamanho do texto e sua posição para colocá-lo no canto inferior direito
    text_size = draw.textsize(watermark_text, font=font)
    text_position = (image.size[0] - text_size[0] - 10, image.size[1] - text_size[1] - 10)

    # Adicionamos o texto com transparência
    draw.text(text_position, watermark_text, fill=(255, 255, 255, 128), font=font)

    # Combinamos a imagem original com a camada de texto
    watermarked = Image.alpha_composite(image, txt)

    # Convertimos a imagem de volta para o modo RGB e salvamos como JPEG
    watermarked.convert("RGB").save(output_image_path, "JPEG")

# Exemplo de uso
add_watermark("input_image.jpg", "watermarked_image.jpg", "© 2023 Student Name")