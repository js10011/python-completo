from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Carregar vídeo
video = VideoFileClip("sample_video.mp4")

# Criar clipe de texto
text = "Important Announcement"
text_clip = TextClip(text, font="Arial", fontsize=50, color="yellow")

# Definir posição do texto na parte superior do vídeo
text_clip = text_clip.set_position(("center", "top")).set_duration(video.duration)

# Sobrepor clipe de texto no vídeo
video_with_text = CompositeVideoClip([video, text_clip])

# Salvar resultado
video_with_text.write_videofile("video_with_styled_text.mp4", codec="libx264")