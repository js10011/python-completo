# Leitura da imagem input_image.jpg em modo binário
with open('input_image.jpg', 'rb') as input_file:
    image_data = input_file.read()

# Gravação dos dados em um novo arquivo output_image.jpg
with open('output_image.jpg', 'wb') as output_file:
    output_file.write(image_data)