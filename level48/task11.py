from moviepy.editor import VideoFileClip, CompositeVideoClip

# Carregando os videoclipes
clipA = VideoFileClip("clipA.mp4")
clipB = VideoFileClip("clipB.mp4")

# Duração da transição
transition_duration = 1.5

# Criando a parte inicial do clipA antes do início da transição
clipA_initial = clipA.subclip(0, clipA.duration - transition_duration)

# Criando a parte do clipA para a transição
clipA_transition = clipA.subclip(clipA.duration - transition_duration, clipA.duration)

# Aplicando rotação e deslocamento ao clipA_transition
def rotation_angle(t):
    return -90 * (t / transition_duration) ** 2  # Alteração da velocidade de rotação

def position_shift(t):
    x = - clipA.w * (t / transition_duration) ** 0.5  # Alteração da velocidade de deslocamento
    return (x, 0)

clipA_transformed = clipA_transition.rotate(rotation_angle).set_position(position_shift)

# Preparando clipB para aparição suave durante a transição
clipB_faded = clipB.set_start(clipA.duration - transition_duration).fadein(transition_duration)

# Criando o clipe final
final_clip = CompositeVideoClip([
    clipA_initial,
    clipA_transformed.set_start(clipA.duration - transition_duration),
    clipB_faded
], size=clipA.size).set_duration(clipA.duration + clipB.duration - transition_duration)

# Exportando o vídeo final
final_clip.write_videofile("spin_and_slide_transition.mp4", fps=24)