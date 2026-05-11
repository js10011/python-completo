from PIL import Image

# Carregamento da imagem do arquivo
original_image = Image.open("input_image.jpg")

# Redimensionamento da imagem para 800x600 pixels
resized_image = original_image.resize((800, 600))

# Salvamento da imagem redimensionada em um novo arquivo
resized_image.save("resized_image.jpg")