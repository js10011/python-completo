from moviepy.editor import VideoFileClip, TextClip, concatenate_videoclips, CompositeVideoClip

# Carregar arquivos de vídeo
video1 = VideoFileClip("video1.mp4")
video2 = VideoFileClip("video2.mp4")
video3 = VideoFileClip("video3.mp4")

# Criar título
title = TextClip("My First Video", fontsize=70, color='white', size=video1.size)
title = title.set_duration(5).set_position('top')

# Criar videoclipe com título
title_clip = CompositeVideoClip([title.set_duration(5)]).set_duration(5)

# Concatenar todos os clipes
final_clip = concatenate_videoclips([title_clip, video1, video2, video3])

# Salvar vídeo final
final_clip.write_videofile("my_first_video.mp4", codec='libx264')