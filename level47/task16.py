from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Carregando o vídeo original
video = VideoFileClip("sample_video.mp4")

# Criando o primeiro clipe de texto "Welcome to the show!"
text_clip1 = (TextClip("Welcome to the show!", fontsize=70, color='white')
              .set_position(('center', 'bottom'))
              .set_duration(3)
              .set_start(0))

# Criando o segundo clipe de texto "Enjoy watching!"
text_clip2 = (TextClip("Enjoy watching!", fontsize=70, color='white')
              .set_position(('center', 'bottom'))
              .set_duration(3)
              .set_start(5))

# Combinando vídeo e clipes de texto
final_video = CompositeVideoClip([video, text_clip1, text_clip2])

# Salvando o vídeo final com legendas
final_video.write_videofile("output_with_subtitles.mp4", codec="libx264")