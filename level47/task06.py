from moviepy.editor import VideoFileClip, AudioFileClip

# Abertura do arquivo de vídeo e arquivo de áudio
video = VideoFileClip("example_video.mp4")
audio = AudioFileClip("background_music.mp3")

# Corte da trilha sonora para a duração do vídeo
audio = audio.subclip(0, video.duration)

# Adição da trilha sonora ao vídeo
video_with_audio = video.set_audio(audio)

# Salvamento do vídeo resultante
video_with_audio.write_videofile("video_with_music.mp4", codec="libx264", audio_codec="aac")