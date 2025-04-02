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

def add_subtitle_to_video(video_path, subtitle_texts, middle_text, output_dir):
    # Obter a duração do vídeo
    probe = ffmpeg.probe(video_path)
    video_duration = float(probe['format']['duration'])

    # Temporário: criar um arquivo de legendas SRT
    subtitle_file = 'temp_subtitle.srt'
    srt_content = generate_srt(subtitle_texts, video_duration)
    with open(subtitle_file, 'w', encoding='utf-8') as f:
        f.write(srt_content)

    # Obter o nome do arquivo de vídeo de entrada
    video_filename = os.path.basename(video_path)

    # Criar o caminho completo do arquivo de saída
    output_path = os.path.join(output_dir, video_filename)

    # Adicionar as legendas e o texto centralizado ao vídeo
    (
        ffmpeg
        .input(video_path)
        .output(
            output_path,
            vf=[
                f"subtitles={subtitle_file}",
                f"drawtext=textfile={middle_text}:fontcolor=white:fontsize=24:x=(w-text_w)/2:y=(h-text_h)/2"
            ]
        )
        .run(overwrite_output=True)
    )

    # Remover o arquivo temporário de legendas
    os.remove(subtitle_file)

def process_videos_in_directory(input_dir, subtitles_dir, instagram_file, output_dir):
    # Verificar se o diretório de saída existe, caso contrário, criar
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Obter todos os arquivos de legenda .txt no diretório de legendas
    subtitle_files = [f for f in os.listdir(subtitles_dir) if f.endswith('.txt')]

    # Ler o conteúdo do arquivo Instagram.txt
    with open(instagram_file, 'r', encoding='utf-8') as f:
        middle_text = f.read().strip()

    # Salvar o texto do Instagram em um arquivo temporário
    middle_text_file = 'middle_text.txt'
    with open(middle_text_file, 'w', encoding='utf-8') as f:
        f.write(middle_text)

    # Processar todos os arquivos .mp4 no diretório de entrada
    for filename in os.listdir(input_dir):
        if filename.endswith('.mp4'):
            video_path = os.path.join(input_dir, filename)
            
            # Selecionar um arquivo de legenda aleatório
            selected_subtitle_file = random.choice(subtitle_files)
            subtitle_path = os.path.join(subtitles_dir, selected_subtitle_file)
            
            # Ler o conteúdo do arquivo de legenda
            with open(subtitle_path, 'r', encoding='utf-8') as f:
                subtitle_texts = f.read().splitlines()
            
            # Adicionar legenda ao vídeo
            add_subtitle_to_video(video_path, subtitle_texts, middle_text_file, output_dir)

    # Remover o arquivo temporário de texto do Instagram
    os.remove(middle_text_file)

# Uso
input_dir = r'C:\Users\USUARIO\Desktop\Agendamento\instagram\entrada'
subtitles_dir = r'C:\Users\USUARIO\Desktop\Agendamento\instagram\legendas'
instagram_file = r'C:\Users\USUARIO\Desktop\Agendamento\instagram\instagram.txt'
output_dir = r'C:\Users\USUARIO\Desktop\Agendamento\instagram\saida'

process_videos_in_directory(input_dir, subtitles_dir, instagram_file, output_dir)