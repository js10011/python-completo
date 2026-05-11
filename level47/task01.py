from moviepy.editor import VideoFileClip

# Carregamento do clipe de vídeo
video = VideoFileClip("sample_video.mp4")

# Obtenção de informações sobre o vídeo
duration = video.duration  # duração
width, height = video.size  # dimensões
fps = video.fps  # taxa de quadros

# Exibição das características do vídeo
print(f"Duração do vídeo: {duration} segundos")
print(f"Dimensões do vídeo: {width}x{height} pixels")
print(f"Taxa de quadros do vídeo: {fps} fps")

# Liberação de recursos
video.close()