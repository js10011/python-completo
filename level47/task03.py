from moviepy.editor import VideoFileClip, vfx

# Caminho para os arquivos de vídeo de entrada e saída
input_file = 'sample_video.mp4'
output_file = 'final_video.mp4'

# Carregamento do vídeo
clip = VideoFileClip(input_file)

# Redimensionamento do vídeo para largura de 480 pixels, mantendo as proporções
clip_resized = clip.resize(width=480)

# Recorte do vídeo para o segmento de 15 a 45 segundos
clip_trimmed = clip_resized.subclip(15, 45)

# Aceleração do vídeo em 1,5 vezes
clip_sped_up = clip_trimmed.fx(vfx.speedx, 1.5)

# Exportação do vídeo final
clip_sped_up.write_videofile(output_file, codec='libx264', audio_codec='aac')