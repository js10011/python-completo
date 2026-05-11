from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_audioclips

# Abrimos o arquivo de vídeo
video = VideoFileClip("example_video.mp4")

# Abrimos o arquivo de áudio
audio = AudioFileClip("looped_music.mp3")

# Criamos loop do áudio até a duração do vídeo
audio_duration = audio.duration
video_duration = video.duration
repeats_needed = int(video_duration // audio_duration) + 1
looped_audio = concatenate_audioclips([audio] * repeats_needed).subclip(0, video_duration)

# Ajustamos o volume do áudio
looped_audio = looped_audio.volumex(0.7)

# Adicionamos o áudio ao vídeo
final_video = video.set_audio(looped_audio)

# Exportamos o vídeo final
final_video.write_videofile("looped_audio_video.mp4", codec='libx264', audio_codec='aac')