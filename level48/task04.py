from moviepy.editor import VideoClip, TextClip, ImageClip, CompositeVideoClip
from moviepy.video.tools.drawing import color_split
from moviepy.video.fx.resize import resize
from moviepy.video.fx.fadein import fadein

# Constantes
duration = 10  # Duração do vídeo em segundos
width, height = 640, 480  # Largura e altura do vídeo

# Criação do fundo com gradiente
background = color_split(
    size=(width, height),
    p1=(0, height // 2),               # Fronteira do gradiente
    p2=(0, height // 2),               # Fronteira do gradiente
    color1=(255, 255, 255),            # Cor superior (branco)
    color2=(200, 200, 200)             # Cor inferior (cinza)
).set_duration(duration)                # Duração do fundo

# Texto 1 com movimento horizontal
moving_text_1 = TextClip("Moving Text 1", fontsize=40, color='black')
moving_text_1 = moving_text_1.set_position(lambda t: (width * t / duration, 50)).set_duration(duration)

# Texto 2 com movimento vertical
moving_text_2 = TextClip("Moving Text 2", fontsize=40, color='black')
moving_text_2 = moving_text_2.set_position(lambda t: (50, height * t / duration)).set_duration(duration)

# Carregar o logo e aplicar transformações
logo = ImageClip("logo.png")
logo = logo.set_start(0).set_duration(duration)
logo = logo.resize(lambda t: 1 + 0.5 * t/duration)  # Aumentar o tamanho do logo ao longo do tempo
logo = logo.set_position(lambda t: (width * t / duration, height * t / duration))
logo = fadein(logo, duration=1).fadeout(duration=duration-9)  # Aparecer e desaparecer do logo

# Criação do clipe final com composição
final_clip = CompositeVideoClip([background, moving_text_1, moving_text_2, logo])

# Salvar o resultado em um arquivo
final_clip.write_videofile("output_task4.mp4", fps=24)