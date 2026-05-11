from moviepy.editor import VideoFileClip

def transform_video(input_file, output_file):
    # Carrega o vídeo
    clip = VideoFileClip(input_file)
    
    # Redimensiona o vídeo para 75% do original
    resized_clip = clip.resize(0.75)
    
    # Rotaciona o vídeo em 180 graus
    rotated_clip = resized_clip.rotate(180)
    
    # Salva o vídeo transformado
    rotated_clip.write_videofile(output_file, codec='libx264')

# Define os arquivos de entrada e saída
input_video = "sample_video.mp4"
output_video = "transformed_video.mp4"

# Realiza a transformação do vídeo
transform_video(input_video, output_video)