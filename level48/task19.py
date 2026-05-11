from moviepy.editor import VideoFileClip

# Carregamos o vídeo de origem
input_path = "input_video.mp4"
video = VideoFileClip(input_path)

# Definimos os parâmetros para exportação
output_path = "web_export.webm"
target_resolution = (854, 480)  # Resolução especificada
target_bitrate = "1000k"        # Taxa de bits para limitar o tamanho do arquivo
fps = 24                        # Taxa de quadros

# Aplicamos a alteração de resolução
video = video.resize(target_resolution)

# Exportamos o vídeo no formato WebM com os parâmetros especificados
video.write_videofile(
    output_path,
    codec='libvpx',          # Codec VP8 para WebM
    audio_codec='libvorbis', # Codec de áudio para WebM
    bitrate=target_bitrate,  # Limitação da taxa de bits
    fps=fps,                 # Taxa de quadros
    threads=4,               # Número de threads para otimização
    preset='medium'          # Configuração do parâmetro preset para compromisso entre qualidade e velocidade
)