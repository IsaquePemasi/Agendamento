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

def generate_instagram_srt(video_duration, middle_text):
    return f"1\n00:00:00,000 --> {int(video_duration // 3600):02}:{int((video_duration % 3600) // 60):02}:{int(video_duration % 60):02},000\n{middle_text}\n"

def add_subtitle_to_video(video_path, subtitle_texts, middle_text, output_dir):
    # Obter a duração do vídeo
    probe = ffmpeg.probe(video_path)
    video_duration = float(probe['format']['duration'])

    # Temporário: criar arquivos de legendas SRT
    subtitle_file = 'temp_subtitle.srt'
    instagram_subtitle_file = 'temp_instagram_subtitle.srt'

    srt_content = generate_srt(subtitle_texts, video_duration)
    with open(subtitle_file, 'w', encoding='utf-8') as f:
        f.write(srt_content)

    instagram_srt_content = generate_instagram_srt(video_duration, middle_text)
    with open(instagram_subtitle_file, 'w', encoding='utf-8') as f:
        f.write(instagram_srt_content)

    # Obter o nome do arquivo de vídeo de entrada
    video_filename = os.path.basename(video_path)

    # Criar o caminho completo do arquivo de saída
    output_path = os.path.join(output_dir, video_filename)

    # Usar ffmpeg para adicionar legendas ao vídeo
    (
        ffmpeg
        .input(video_path)
        .filter('subtitles', subtitle_file)
        .filter('subtitles', instagram_subtitle_file, force_style='Alignment=6')  # Alinha as legendas ao topo central
        .output(output_path)
        .run(overwrite_output=True)
    )

    # Remover os arquivos temporários de legendas
    os.remove(subtitle_file)
    os.remove(instagram_subtitle_file)

def process_videos_in_directory(input_dir, subtitles_dir, instagram_file, output_dir):
    # Verificar se o diretório de saída existe, caso contrário, criar
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Obter todos os arquivos de legenda .txt no diretório de legendas
    subtitle_files = [f for f in os.listdir(subtitles_dir) if f.endswith('.txt')]

    # Ler o conteúdo do arquivo Instagram.txt
    with open(instagram_file, 'r', encoding='utf-8') as f:
        middle_text = f.read().strip()

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
            add_subtitle_to_video(video_path, subtitle_texts, middle_text, output_dir)

# Uso
input_dir = r'C:\Users\USUARIO\Desktop\Agendamento\instagram\entrada'
subtitles_dir = r'C:\Users\USUARIO\Desktop\Agendamento\instagram\legendas'
instagram_file = r'C:\Users\USUARIO\Desktop\Agendamento\instagram\instagram.txt'
output_dir = r'C:\Users\USUARIO\Desktop\Agendamento\instagram\saida'

process_videos_in_directory(input_dir, subtitles_dir, instagram_file, output_dir)