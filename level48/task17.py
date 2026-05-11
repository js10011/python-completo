from moviepy.editor import VideoFileClip

# Carregamento do arquivo de vídeo
input_video_path = "input_video.mp4"
video_clip = VideoFileClip(input_video_path)

# Exportação de vídeo usando o codec H.264 e taxa de quadros de 24 fps
output_video_path = "basic_export.mp4"
video_clip.write_videofile(output_video_path, codec='libx264', fps=24)

# Fechamento do arquivo de vídeo para liberar recursos
video_clip.close()