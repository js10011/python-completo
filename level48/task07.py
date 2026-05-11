from moviepy.editor import VideoFileClip
import numpy as np

# Caminho para os arquivos de vídeo de entrada e saída
input_video = "input_video.mp4"  # Indique o caminho para o seu arquivo de vídeo
output_video = "sepia_video.mp4"

# Função para aplicar o filtro sépia a um frame de imagem
def apply_sepia(image):
    sepia_filter = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])
    sepia_image = image.dot(sepia_filter)
    sepia_image[sepia_image > 255] = 255  # Limite de valores de pixels
    return sepia_image.astype(np.uint8)

# Carregamento do vídeo original
video_clip = VideoFileClip(input_video)

# Aplicação do filtro sépia a todos os frames do vídeo
sepia_clip = video_clip.fl_image(apply_sepia)

# Salvamento do vídeo editado em um arquivo
sepia_clip.write_videofile(output_video, codec='libx264')