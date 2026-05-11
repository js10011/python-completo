from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip

# Carregamento dos fragmentos de vídeo
video1 = VideoFileClip("video1.mp4")
video2 = VideoFileClip("video2.mp4")
video3 = VideoFileClip("video3.mp4")

# Junção dos fragmentos de vídeo
final_video = concatenate_videoclips([video1, video2, video3])

# Carregamento do arquivo de áudio
audio = AudioFileClip("audio.mp3")

# Junção do vídeo com a trilha sonora
final_video_with_audio = final_video.set_audio(audio)

# Salvamento do vídeo final
final_video_with_audio.write_videofile("video_with_audio.mp4", codec="libx264", audio_codec="aac")