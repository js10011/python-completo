from moviepy.editor import VideoClip, TextClip, ImageClip, CompositeVideoClip, AudioFileClip

# Parâmetros temporais
duration = 5  # Duração do videoclipe
text_animation_duration = 5  # Duração da animação do texto
logo_animation_duration = 3  # Duração da animação do logotipo

# Criando a animação do texto
def make_text_clip():
    txt_clip = TextClip("Enjoy the Moments", fontsize=70, color='white', bg_color='black', size=(640, 480))
    txt_clip = txt_clip.set_position(lambda t: ('center', 480 - t * 96))  # Movimento de baixo para cima
    txt_clip = txt_clip.set_duration(text_animation_duration)
    return txt_clip

# Criando a animação do logotipo
def make_logo_clip():
    logo_clip = ImageClip("logo.png").set_duration(duration)
    logo_clip = logo_clip.set_position(lambda t: ('right', 'bottom'))  # Posicionamento no canto inferior direito
    logo_clip = logo_clip.resize(lambda t: 0.5 + 0.5 * t / logo_animation_duration)  # Aumento de tamanho
    return logo_clip

# Adicionando música de fundo com volume reduzido
def add_background_music(clip):
    audio = AudioFileClip("background_music.mp3").subclip(0, duration)  # Supondo que o arquivo existe
    audio = audio.volumex(0.1)  # Redução do volume
    return clip.set_audio(audio)

# Criando o videoclipe
def create_video():
    text_clip = make_text_clip()
    logo_clip = make_logo_clip()
    
    # Criando o videoclipe principal
    video = CompositeVideoClip([text_clip, logo_clip], size=(640, 480)).set_duration(duration)
    
    # Adicionando o áudio
    video = add_background_music(video)
    
    # Salvando o videoclipe
    video.write_videofile("animated_video.mp4", fps=24)

# Criação do vídeo
create_video()