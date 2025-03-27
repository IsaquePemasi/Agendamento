# # pip install moviepy
# # pip install imageio[ffmpeg]
# import moviepy
# from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# def add_subtitle_to_video(video_path, subtitle_text, output_path):
#     # Carregar o vídeo
#     video = VideoFileClip(video_path)

#     # Criar o clipe de texto para a legenda
#     subtitle = TextClip(subtitle_text, fontsize=24, color='white', bg_color='black')
    
#     # Definir a duração da legenda igual à duração do vídeo
#     subtitle = subtitle.set_duration(video.duration)
    
#     # Posicionar a legenda na parte inferior do vídeo
#     subtitle = subtitle.set_position(('center', 'bottom'))
    
#     # Combinar o vídeo original com a legenda
#     final_video = CompositeVideoClip([video, subtitle])
    
#     # Salvar o vídeo editado
#     final_video.write_videofile(output_path, codec='libx264')

# # Uso
# video_path = r'C:\Users\a925216\OneDrive - ATOS\Desktop\Agendamento\insta_legenda\entrada\Sophie Rain - Tell Your GF Recoil Dance #shorts.mp4'
# subtitle_text = 'Sua legenda aqui'
# output_path = r'C:\Users\a925216\OneDrive - ATOS\Desktop\Agendamento\insta_legenda\saida\video_editado.mp4'

# add_subtitle_to_video(video_path, subtitle_text, output_path)

import moviepy
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

print("moviepy está instalado corretamente.")