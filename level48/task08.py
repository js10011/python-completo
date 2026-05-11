from moviepy.editor import VideoFileClip
import numpy as np

# Caminho para os arquivos de vídeo de entrada e saída
input_video = "input_video.mp4"  # Indique o caminho para o seu arquivo de vídeo
output_video = "enhanced_red_video.mp4"

# Função para aumentar o canal vermelho e reduzir os canais verde e azul
def enhance_red_frame(frame):
    # Aumentar o canal vermelho
    frame[:, :, 0] *= 1.5
    frame[:, :, 0] = frame[:, :, 0].clip(0, 255)  # Limitar valores no intervalo [0, 255]

    # Reduzir os canais verde e azul
    frame[:, :, 1] *= 0.5
    frame[:, :, 2] *= 0.5

    return frame.astype(np.uint8)

# Carregar o vídeo original
clip = VideoFileClip(input_video)

# Aplicar o filtro a cada quadro
modified_clip = clip.fl_image(enhance_red_frame)

# Salvar o vídeo modificado em um arquivo
modified_clip.write_videofile(output_video, codec='libx264')