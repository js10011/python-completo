from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import pysrt

# Caminhos para os arquivos de vídeo, legendas e vídeo de saída
video_path = "sample_video.mp4"
subtitles_path = "subtitles.srt"
output_path = "video_with_srt_subtitles.mp4"

# Carregamento do clipe de vídeo
video = VideoFileClip(video_path)

# Carregamento das legendas usando pysrt
subs = pysrt.open(subtitles_path)

# Criação de uma lista para armazenar clipes com legendas
subtitle_clips = []

# Adicionando cada legenda como um clipe de texto
for sub in subs:
    # Criação de um clipe de texto para cada legenda
    text_clip = TextClip(
        sub.text, fontsize=24, color='white', bg_color='black', size=(video.w, None), method='caption'
    )

    # Definindo o início e a duração da exibição da legenda
    start_time = sub.start.seconds + sub.start.milliseconds / 1000.0
    end_time = sub.end.seconds + sub.end.milliseconds / 1000.0
    duration = end_time - start_time

    text_clip = text_clip.set_start(start_time)
    text_clip = text_clip.set_duration(duration)
    text_clip = text_clip.set_position(('center', 'bottom'))

    # Adicionando o clipe de texto à lista
    subtitle_clips.append(text_clip)

# Sobreposição de clipes com legendas no vídeo
final_video = CompositeVideoClip([video] + subtitle_clips)

# Gravação do resultado no arquivo
final_video.write_videofile(output_path, codec='libx264', fps=video.fps)

# Fechamento do clipe de vídeo
video.close()