from moviepy.editor import VideoClip, TextClip, ImageClip, CompositeVideoClip, ColorClip

# Parâmetros do vídeo
video_duration = 7  # Duração do vídeo em segundos
video_size = (640, 480)  # Tamanho do vídeo (largura, altura)

# Função para animação do texto
def animate_text(t):
    # Movimento diagonal do texto do canto superior direito para o canto inferior esquerdo
    x = video_size[0] * (1 - t / video_duration)
    y = video_size[1] * (t / video_duration)
    return (x, y)

# Função para animação do aumento da imagem
def animate_image_scale(t):
    # Aumento de escala de 50% para 100% durante o vídeo
    return 0.5 + 0.5 * (t / video_duration)

# Criação do clipe de texto
text_clip = TextClip("Diagonal Text", fontsize=40, color='white', font='Arial') \
    .set_duration(video_duration) \
    .set_position(animate_text)

# Criação do clipe com a imagem star.png, tamanho inicial 50%
image_clip = ImageClip("star.png").set_duration(video_duration).resize(0.5)
# Aplicação da função de mudança de escala
image_clip = image_clip.resize(lambda t: animate_image_scale(t)).set_position('center')

# Criação do fundo preto para o vídeo
background_clip = ColorClip(size=video_size, color=(0, 0, 0), duration=video_duration)

# Combinação do fundo, texto e imagem
final_clip = CompositeVideoClip([background_clip, text_clip, image_clip])

# Salvando o vídeo final
final_clip.write_videofile("output_task3.mp4", fps=24)