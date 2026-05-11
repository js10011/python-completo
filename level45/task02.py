from PIL import Image

# Caminho para as imagens de entrada e saída
input_path = 'input.jpg'  # Indique o caminho para sua imagem
output_path = 'output.jpg'  # Indique o caminho para a imagem salva

# Tamanho especificado para redimensionamento
size = (200, 200)

# Abertura do arquivo de imagem
with Image.open(input_path) as img:
    # Redimensionamento da imagem
    resized_img = img.resize(size)
    # Salvando a imagem redimensionada com um novo nome
    resized_img.save(output_path)

    # Verificação do novo tamanho
    if resized_img.size != size:
        raise ValueError(f"A imagem não foi redimensionada corretamente, tamanho atual: {resized_img.size}")

print(f"A imagem foi salva em '{output_path}' com o tamanho {size}.")