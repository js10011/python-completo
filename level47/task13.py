from moviepy.editor import VideoFileClip, concatenate_videoclips

# Exemplo de arquivos de vídeo de entrada
input_files = ["clip1.mp4", "clip2.mp4", "clip3.mp4"]
output_file = "video_with_transitions.mp4"
fade_duration = 1  # Duração do efeito de surgimento e desvanecimento

# Carregamento dos clipes de vídeo
clips = [VideoFileClip(file) for file in input_files]

# Adição de efeitos de surgimento e desvanecimento
clips_with_transitions = []
for i, clip in enumerate(clips):
    clip = clip.fadein(fade_duration).fadeout(fade_duration)
    clips_with_transitions.append(clip)

# Combinação de todos os clipes em um único com transições
final_clip = concatenate_videoclips(clips_with_transitions, method="compose")

# Salvamento do arquivo de vídeo final
final_clip.write_videofile(output_file, codec='libx264', fps=24)