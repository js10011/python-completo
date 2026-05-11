from moviepy.editor import VideoClip, TextClip, CompositeVideoClip

# Parâmetros do texto
text = "Hello World"
fontsize = 70
color = 'white'
duration = 10
video_size = (640, 480)

# Criar clipe de texto
text_clip = TextClip(text, fontsize=fontsize, color=color, size=video_size, method='caption')

# Configurar duração e posição do clipe de texto
text_clip = text_clip.set_duration(duration).set_position('center')

# Criar um clipe de vídeo vazio com tamanho e duração especificados
video_clip = VideoClip(lambda t: (255, 255, 255), duration=duration).set_size(video_size)

# Sobrepor clipe de texto no clipe de vídeo
final_clip = CompositeVideoClip([video_clip, text_clip])

# Salvar clipe final em um arquivo
final_clip.write_videofile("output_task1.mp4", fps=24)