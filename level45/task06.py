from PIL import Image

# Caminho para as imagens de entrada e saída
input_image_path = "input.jpg"  # Substitua este nome de arquivo pelo caminho atual da sua imagem
output_image_path = "thumbnail_image.jpg"

# Tamanho máximo do thumbnail
max_size = (400, 400)

# Abrir a imagem
with Image.open(input_image_path) as img:
    # Reduzir a imagem, mantendo as proporções
    img.thumbnail(max_size)
    # Salvar a imagem reduzida
    img.save(output_image_path)

print(f"Thumbnail salvo em '{output_image_path}' com tamanho máximo de {max_size}.")