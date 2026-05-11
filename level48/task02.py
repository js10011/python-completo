from moviepy.editor import TextClip, VideoClip

# Parâmetros do clipe
text = "Horizontal Move"
duration = 5
video_width = 640
video_height = 480

# Criar um clipe de texto
text_clip = TextClip(text, fontsize=70, color='white', size=(video_width, video_height))

# Definir posições inicial e final do texto
start_pos = -text_clip.w
end_pos = video_width

# Aplicar animação de movimento do texto da esquerda para a direita com set_position
pos_t_duration_center_ = lambda t: (start_pos + (end_pos - start_pos) * (t / duration), 'center')
animated_text = text_clip.set_position(pos_t_duration_center_).set_duration(duration)

# Criar um videoclipe de fundo vazio e sobrepor o texto com animação
animated_clip = VideoClip(lambda t: animated_text.get_frame(t), duration=duration)

# Salvar a animação em um arquivo
animated_clip.write_videofile("output_task2.mp4", fps=24)