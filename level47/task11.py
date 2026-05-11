from moviepy.editor import VideoFileClip, concatenate_videoclips

# Caminhos para os arquivos de vídeo de origem
video_paths = ["clip1.mp4", "clip2.mp4", "clip3.mp4"]

# Caminho para salvar o vídeo final combinado
output_path = "compiled_video.mp4"

# Carregamento dos videoclipes
clips = [VideoFileClip(video) for video in video_paths]

# Combinar clipes sem transições
final_clip = concatenate_videoclips(clips, method="compose")

# Salvar o vídeo final no formato MP4
final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

# Fechar todos os clipes para liberar recursos
for clip in clips:
    clip.close()