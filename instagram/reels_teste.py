import os
import random
import ffmpeg

def generate_srt(subtitle_texts, video_duration):
    srt_content = []
    for i, text in enumerate(subtitle_texts, start=1):
        start_time = 0
        end_time = video_duration
        srt_content.append(f"{i}\n00:00:00,000 --> {int(video_duration // 3600):02}:{int((video_duration % 3600) // 60):02}:{int(video_duration % 60):02},000\n{text}\n")
    return "\n".join(srt_content)

def add_subtitle_to_video(video_path, subtitle_texts, watermark_text, output_dir):
    try:
        # Obter a duração do vídeo
        probe = ffmpeg.probe(video_path)
        video_duration = float(probe['format']['duration'])

        # Temporário: criar um arquivo de legendas SRT
        subtitle_file = 'temp_subtitle.srt'
        srt_content = generate_srt(subtitle_texts, video_duration)
        with open(subtitle_file, 'w') as f:
            f.write(srt_content)

        # Obter o nome do arquivo de vídeo de entrada
        video_filename = os.path.basename(video_path)

        # Criar o caminho completo do arquivo de saída
        output_path = os.path.join(output_dir, video_filename)

        # Filtros de texto para adicionar legendas e marca d'água
        subtitle_filter = f"subtitles={subtitle_file}"
        watermark_filter = f"drawtext=text='{watermark_text}':fontcolor=white:fontsize=24:alpha=0.5:x=(w-text_w)/2:y=(h-text_h)/2:enable='between(t,0,{video_duration})'"

        # Usar ffmpeg para adicionar legendas e marca d'água ao vídeo
        (
            ffmpeg
            .input(video_path)
            .output(output_path, vf=f"{subtitle_filter},{watermark_filter}")
            .run(overwrite_output=True)
        )

        print(f"Vídeo salvo com sucesso em {output_path}")

        # Remover o arquivo temporário de legendas
        os.remove(subtitle_file)

    except ffmpeg.Error as e:
        print(f"Erro ao processar o vídeo: {e}")
        print(f"Saída de erro do ffmpeg: {e.stderr.decode('utf8')}")

def process_videos_in_directory(input_dir, subtitles_dir, output_dir, watermark_text):
    # Verificar se o diretório de saída existe, caso contrário, criar
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Obter todos os arquivos de legenda .txt no diretório de legendas
    subtitle_files = [f for f in os.listdir(subtitles_dir) if f.endswith('.txt')]

    # Processar todos os arquivos .mp4 no diretório de entrada
    for filename in os.listdir(input_dir):
        if filename.endswith('.mp4'):
            video_path = os.path.join(input_dir, filename)
            
            # Selecionar um arquivo de legenda aleatório
            selected_subtitle_file = random.choice(subtitle_files)
            subtitle_path = os.path.join(subtitles_dir, selected_subtitle_file)
            
            # Ler o conteúdo do arquivo de legenda
            with open(subtitle_path, 'r') as f:
                subtitle_texts = f.read().splitlines()
            
            # Adicionar legenda e marca d'água ao vídeo
            add_subtitle_to_video(video_path, subtitle_texts, watermark_text, output_dir)

# Uso
input_dir = r'C:\Users\USUARIO\Desktop\Agendamento\instagram\entrada'
subtitles_dir = r'C:\Users\USUARIO\Desktop\Agendamento\instagram\legendas'
output_dir = r'C:\Users\USUARIO\Desktop\Agendamento\instagram\saida'
watermark_text = '@SeuPerfilInstagram'

process_videos_in_directory(input_dir, subtitles_dir, output_dir, watermark_text)