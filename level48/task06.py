from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import colorx, blackwhite

# Caminho para os arquivos de vídeo de entrada e saída
input_video_path = "input_video.mp4"  # Indique o caminho para o seu arquivo de vídeo
output_video_path = "high_contrast_bw_video.mp4"

# Fator de aumento de contraste
contrast_factor = 1.5

# Carregamento do vídeo
clip = VideoFileClip(input_video_path)

# Aumento do contraste em 50%
clip_contrast = colorx(clip, contrast_factor)

# Conversão para formato preto e branco
clip_bw = blackwhite(clip_contrast)

# Salvamento do resultado em um novo arquivo
clip_bw.write_videofile(output_video_path, codec='libx264')