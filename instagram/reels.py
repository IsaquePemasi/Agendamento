import os
import ffmpeg

def add_subtitle_to_video(video_path, subtitle_text, output_dir):
    # Obter a duração do vídeo
    probe = ffmpeg.probe(video_path)
    video_duration = float(probe['format']['duration'])

    # Obter o nome do arquivo de entrada
    input_filename = os.path.basename(video_path)

    # Criar o caminho do arquivo de saída no diretório especificado
    output_path = os.path.join(output_dir, input_filename)

    # Criar filtro de legenda diretamente
    subtitle_lines = f"drawtext=text='{subtitle_text}':fontcolor=white:fontsize=24:x=(w-text_w)/2:y=h-50:enable='between(t,0,{video_duration})'"

    # Usar ffmpeg para adicionar legendas ao vídeo
    (
        ffmpeg
        .input(video_path)
        .output(output_path, vf=subtitle_lines)
        .run(overwrite_output=True)
    )

# Uso
video_path = r'C:\Users\USUARIO\Desktop\Agendamento\instagram\entrada\SophieRain.mp4'
subtitle_text = 'Sua legenda aqui'
output_dir = r'C:\Users\USUARIO\Desktop\Agendamento\instagram\saida'

add_subtitle_to_video(video_path, subtitle_text, output_dir)