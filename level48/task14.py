from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip

# Criamos um videoclipe. Aqui estamos criando um videoclipe preto vazio com duração de 10 segundos.
video_clip = VideoFileClip("your_video.mp4").subclip(0, 10)  # Substitua "your_video.mp4" pelo seu arquivo de vídeo

# Importamos a trilha de áudio
audio_clip = AudioFileClip("background_music.mp3").subclip(0, video_clip.duration)

# Adicionamos texto ao vídeo
text = TextClip("Welcome to the Show", fontsize=70, color='white', size=video_clip.size)
text = text.set_position('center').set_duration(3)

# Criamos um novo videoclipe com texto
video = CompositeVideoClip([video_clip, text])

# Adicionamos a trilha de áudio ao videoclipe
final_clip = video.set_audio(audio_clip)

# Salvamos o vídeo final
final_clip.write_videofile("video_with_music.mp4", codec='libx264', audio_codec='aac')