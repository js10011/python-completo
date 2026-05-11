from PIL import Image, ImageDraw

def add_text_to_image(input_image_path, output_image_path, text):
    # Abre a imagem
    image = Image.open(input_image_path)

    # Cria um objeto de desenho
    draw = ImageDraw.Draw(image)

    # Define a posição para o texto
    position = (0, 0)

    # Cor do texto (branca)
    text_color = (255, 255, 255)

    # Adiciona o texto na imagem
    draw.text(position, text, fill=text_color)

    # Salva a imagem com o texto adicionado
    image.save(output_image_path)

# Parâmetros
input_image_path = 'input_image.jpg'
output_image_path = 'output_image.jpg'
text = 'Hello World!'

# Chama a função para adicionar texto
add_text_to_image(input_image_path, output_image_path, text)