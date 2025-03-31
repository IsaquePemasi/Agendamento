import os
import ffmpeg

def add_subtitle_to_video(video_path, subtitle_text, output_dir):
    # Obter a duração do vídeo
    probe = ffmpeg.probe(video_path)
    video_duration = float(probe['format']['duration'])

    # Temporário: criar um arquivo de legendas SRT
    subtitle_file = 'temp_subtitle.srt'
    with open(subtitle_file, 'w') as f:
        f.write(f"1\n00:00:00,000 --> {int(video_duration // 3600):02}:{int((video_duration % 3600) // 60):02}:{int(video_duration % 60):02},000\n{subtitle_text}\n")

    # Obter o nome do arquivo de vídeo de entrada
    video_filename = os.path.basename(video_path)

    # Criar o caminho completo do arquivo de saída
    output_path = os.path.join(output_dir, video_filename)

    # Usar ffmpeg para adicionar legendas ao vídeo
    (
        ffmpeg
        .input(video_path)
        .output(output_path, vf='subtitles={}'.format(subtitle_file))
        .run(overwrite_output=True)
    )

    # Remover o arquivo temporário de legendas
    os.remove(subtitle_file)

# Uso
video_path = r'C:\Users\USUARIO\Desktop\Agendamento\instagram\entrada\SophieRain.mp4'
subtitle_text = 'Sua legenda aqui'
output_dir = r'C:\Users\USUARIO\Desktop\Agendamento\instagram\saida'

add_subtitle_to_video(video_path, subtitle_text, output_dir)