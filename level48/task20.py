from moviepy.editor import VideoFileClip

# Carregar o arquivo de vídeo
video_clip = VideoFileClip("input_video.mp4")

# Cortar o vídeo até os primeiros 5 segundos
video_clip = video_clip.subclip(0, 5)

# Exportar o vídeo para GIF com taxa de quadros de 12 fps e aplicar otimização
video_clip.write_gif("optimized_gif.gif", fps=12, opt='OptimizePlus', fuzz=5)