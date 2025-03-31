import ffmpeg

def add_subtitle_to_video(video_path, subtitle_text, output_path):
    # Temporário: criar um arquivo de legendas SRT
    subtitle_file = 'temp_subtitle.srt'
    # r'C:\Users\a925216\OneDrive - ATOS\Desktop\Agendamento\instagram\Sophie Rain - Tell Your GF Recoil Dance #shorts.mp4'
    with open(subtitle_file, 'w') as f:
        f.write(f"1\n00:00:00,000 --> 00:00:10,000\n{subtitle_text}\n")

    # Usar ffmpeg para adicionar legendas ao vídeo
    (
        ffmpeg
        .input(video_path)
        .output(output_path, vf='subtitles={}'.format(subtitle_file))
        .run(overwrite_output=True)
    )

# Uso
video_path = r'C:\Users\a925216\OneDrive - ATOS\Desktop\Agendamento\instagram\entrada\SophieRain.mp4'
subtitle_text = 'Sua legenda aqui'
output_path = r'C:\Users\a925216\OneDrive - ATOS\Desktop\Agendamento\instagram\saida\video_editado.mp4'

add_subtitle_to_video(video_path, subtitle_text, output_path)