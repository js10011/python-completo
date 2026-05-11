from moviepy.editor import VideoFileClip
from PIL import Image
import os

# Caminho para o vídeo de entrada e arquivo GIF de saída
video_path = 'input_video.mp4'  # Indique o caminho para o seu arquivo de vídeo
output_gif = 'animation.gif'

# Carregando o vídeo
clip = VideoFileClip(video_path)
frames = []

# Extraindo cada décimo frame
for i, frame in enumerate(clip.iter_frames(fps=clip.fps, dtype="uint8")):
    if i % 10 == 0:  # Cada décimo frame
        frame_image = Image.fromarray(frame)
        frames.append(frame_image)

# Processamento dos frames: redimensionamento e conversão para preto e branco
processed_frames = []
for frame in frames:
    frame = frame.resize((150, 150)).convert('L')
    processed_frames.append(frame)

# Criando uma animação GIF a partir dos frames processados
if processed_frames:
    processed_frames[0].save(output_gif, save_all=True, append_images=processed_frames[1:], loop=0, duration=200, format='GIF')