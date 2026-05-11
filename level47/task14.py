from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Carregar o vídeo original
video = VideoFileClip("sample_video.mp4")

# Criar texto
text = TextClip("Hello, World!", fontsize=70, color='white', bg_color='black')
text = text.set_position('center').set_duration(video.duration)

# Posicionar texto no vídeo
video_with_text = CompositeVideoClip([video, text])

# Salvar o vídeo modificado
video_with_text.write_videofile("output_with_text.mp4", codec="libx264")