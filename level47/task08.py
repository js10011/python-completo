from moviepy.editor import VideoFileClip
from PIL import Image

# Abre o arquivo de vídeo
video = VideoFileClip("input_video.mp4")

# Extrai o quadro no quinto segundo
frame = video.get_frame(5)

# Converte o quadro em imagem PIL
image = Image.fromarray(frame)

# Salva a imagem no formato PNG
image.save("extracted_frame.png")