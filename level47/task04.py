from moviepy.editor import VideoFileClip

# Abertura do arquivo de vídeo
video_clip = VideoFileClip("example_video.mp4")

# Extração da duração do vídeo
duration = video_clip.duration

# Extração dos tamanhos do vídeo (largura e altura)
width, height = video_clip.size

# Exibição das informações
print(f"Duração do vídeo: {duration} segundos")
print(f"Tamanhos do vídeo: {width}x{height} pixels")

# Fechamento do arquivo de vídeo
video_clip.close()