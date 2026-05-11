from moviepy.editor import VideoFileClip, concatenate_videoclips

# Carregamento dos videoclipes
scene1 = VideoFileClip("scene1.mp4")
scene2 = VideoFileClip("scene2.mp4")

# Duração da transição
fade_duration = 2

# Aplicação do efeito de escurecimento a "scene1" (brilho vai para preto)
scene1 = scene1.fadeout(fade_duration)

# Aplicação do efeito de aparição do escuro a "scene2" (aparição suave do preto)
scene2 = scene2.fadein(fade_duration)

# Combinação dos clipes com transição através do escurecimento
final_clip = concatenate_videoclips([scene1, scene2], method="compose")

# Exportação do arquivo de vídeo final
final_clip.write_videofile("fade_to_black.mp4", codec="libx264", audio_codec="aac")