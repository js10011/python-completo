from PIL import Image
import os

# Caminho para a pasta com as imagens
frames_folder = 'frames'

# Leitura de todas as imagens da pasta especificada
images = []
for filename in sorted(os.listdir(frames_folder)):
    if filename.endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
        img_path = os.path.join(frames_folder, filename)
        img = Image.open(img_path)
        images.append(img)

# Conversão das imagens para GIF
if images:
    # Definição da duração do frame e do loop infinito
    images[0].save(
        'animation.gif',
        save_all=True,
        append_images=images[1:],
        duration=150,
        loop=0
    )