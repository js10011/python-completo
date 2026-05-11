from moviepy.editor import VideoFileClip
import numpy as np

# Caminho para os arquivos de vídeo de entrada e saída
input_video_path = "input_video.mp4"  # Indique o caminho para o seu arquivo de vídeo
output_video_path = "brightened_video.mp4"

# Função para aumentar o brilho da imagem
def increase_brightness(image):
    # Aumentar o brilho em 20%
    return (image * 1.2).clip(0, 255).astype('uint8')

# Carregar vídeo
clip = VideoFileClip(input_video_path)

# Aplicar alteração de brilho a todos os frames do vídeo
brightened_clip = clip.fl_image(increase_brightness)

# Salvar o resultado em um novo arquivo
brightened_clip.write_videofile(output_video_path, codec='libx264')