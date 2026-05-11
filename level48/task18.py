from moviepy.editor import VideoFileClip

# Caminho para os arquivos de vídeo de entrada e saída
input_path = "input_video.mp4"
output_path = "resized_video.mp4"

# Novas dimensões do vídeo e FPS desejado
new_width = 1280
new_height = 720
fps = 30

# Carregar o arquivo de vídeo
clip = VideoFileClip(input_path)

# Alterar o tamanho do vídeo
resized_clip = clip.resize(newsize=(new_width, new_height))

# Exportar o vídeo com os parâmetros desejados
resized_clip.write_videofile(
    output_path,
    codec='libx264',
    fps=fps
)

print(f"Vídeo salvo como {output_path} com resolução {new_width}x{new_height} e taxa de {fps} quadros por segundo.")