from moviepy.video.io.VideoFileClip import VideoFileClip

# Caminho para o arquivo de vídeo de entrada
video_path = "input_video.mp4"  # Substitua pelo caminho do seu arquivo de vídeo

# Carregamento do arquivo de vídeo usando MoviePy
video = VideoFileClip(video_path)

# Definição da duração de cada segmento
segment_duration = video.duration / 3

# Criação e salvamento de cada um dos três segmentos
for i in range(3):
    start_time = i * segment_duration
    end_time = (i + 1) * segment_duration
    segment = video.subclip(start_time, end_time)
    segment.write_videofile(f"segment{i+1}.mp4", codec="libx264")
    print(f"Segmento {i+1} salvo como segment{i+1}.mp4")

# Fechamento do arquivo de vídeo
video.close()