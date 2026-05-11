from moviepy.editor import ColorClip

# Criamos um clipe de cor azul com tamanho de 640x360 pixels e duração de 10 segundos
blue_clip = ColorClip(size=(640, 360), color=(0, 0, 255), duration=10)

# Definimos a taxa de quadros em 24 FPS
blue_clip = blue_clip.set_fps(24)

# Salvamos o clipe no arquivo blue_clip.mp4
blue_clip.write_videofile("blue_clip.mp4", codec='libx264')