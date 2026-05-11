from moviepy.editor import VideoFileClip, concatenate_videoclips

# Carrega os arquivos de vídeo do diretório de trabalho atual
video1 = VideoFileClip("video1.mp4")
video2 = VideoFileClip("video2.mp4")

# Define a duração da transição
crossfade_duration = 1  # 1 segundo

# Configura a transição suave para o segundo clipe
video2 = video2.crossfadein(crossfade_duration)

# Une os vídeos com a transição suave
final_video = concatenate_videoclips([video1, video2.set_start(video1.duration - crossfade_duration)], method="compose")

# Salva o vídeo resultante
final_video.write_videofile("simple_crossfade.mp4", codec="libx264", audio_codec="aac")