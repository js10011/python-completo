from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip, ImageClip

# Carregamento do fundo principal como um arquivo de vídeo
background_clip = VideoFileClip("path_to_background_video.mp4")

# Criação do título inicial "Adventure Begins"
start_title = (TextClip("Adventure Begins", fontsize=70, color='white', bg_color='black', size=background_clip.size)
               .set_duration(3)
               .set_position("center"))

# Criação do título final "Thanks for Watching"
end_title = (TextClip("Thanks for Watching", fontsize=70, color='white', bg_color='black', size=background_clip.size)
             .set_duration(3)
             .set_position("center"))

# Carregamento do arquivo de áudio e corte com duração do vídeo de fundo
audio_clip = AudioFileClip("path_to_music.mp3").subclip(0, background_clip.duration)

# Criação do texto animado "Exploring the World"
animated_text = (TextClip("Exploring the World", fontsize=50, color='white')
                 .set_position(lambda t: (t * 100, 'center'))
                 .set_start(7)
                 .set_duration(4))

# Carregamento do logotipo e configuração de sua animação para diminuir
logo = (ImageClip("path_to_logo.png")
        .set_duration(background_clip.duration)
        .set_position(('left', 'top'))
        .resize(lambda t: 1 - 0.5 * (t / background_clip.duration)))  # O logotipo diminui de tamanho 50% do inicial

# Criação do clipe de vídeo composto que une o fundo, os títulos, a animação do texto e o logotipo
video = CompositeVideoClip([
    background_clip,
    start_title.set_start(0),           # Título inicial desde o começo
    animated_text,                      # Texto animado "Exploring the World" a partir do 7º segundo
    logo,                               # Logotipo no canto superior esquerdo com redução de tamanho
    end_title.set_start(background_clip.duration - 3)  # Título final no final do vídeo
])

# Atribuição da trilha de áudio ao clipe de vídeo
video = video.set_audio(audio_clip)

# Exportação do vídeo final para arquivo
video.write_videofile("complex_video.mp4", codec='libx264', audio_codec='aac', fps=24)