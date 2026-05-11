from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.fx.all import fadein, fadeout

# Parâmetros de transição
transition_duration = 2

# Carregamento dos clipes
clipA = VideoFileClip("clipA.mp4")
clipB = VideoFileClip("clipB.mp4")

# Aplicação do efeito fadeout no clipA
clipA_fadeout = fadeout(clipA, duration=transition_duration)

# Aplicação do efeito de aumento de brilho no clipB
clipB_fadein = fadein(clipB, duration=transition_duration)

# Combinação dos clipes com transição
final_video = concatenate_videoclips([clipA_fadeout, clipB_fadein], method="compose")

# Salvamento do vídeo
final_video.write_videofile("fade_brightness_transition.mp4", codec="libx264", audio_codec="aac")