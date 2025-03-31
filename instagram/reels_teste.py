import os
import random
import ffmpeg

def add_subtitle_and_music_to_video(video_path, subtitle_text, music_path, output_dir):
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

    # Usar ffmpeg para adicionar legendas ao vídeo e remover música original
    ffmpeg.input(video_path).output(
        'temp_video.mp4', 
        vf='subtitles={}'.format(subtitle_file), 
        map_metadata=-1, 
        an=True
    ).run(overwrite_output=True)

    # Usar ffmpeg para adicionar a nova música ao vídeo
    ffmpeg.concat(
        ffmpeg.input('temp_video.mp4').video,
        ffmpeg.input(music_path).audio,
        v=1, a=1
    ).output(output_path, map_metadata=-1).run(overwrite_output=True)

    # Remover arquivos temporários
    os.remove(subtitle_file)
    os.remove('temp_video.mp4')

def process_videos_in_directory(input_dir, subtitles_dir, music_dir, output_dir):
    # Verificar se o diretório de saída existe, caso contrário, criar
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Obter todos os arquivos de legenda .txt no diretório de legendas
    subtitle_files = [f for f in os.listdir(subtitles_dir) if f.endswith('.txt')]

    # Obter todos os arquivos de música .mp3 ou .wav no diretório de músicas
    music_files = [f for f in os.listdir(music_dir) if f.endswith('.mp3') or f.endswith('.wav')]

    # Processar todos os arquivos .mp4 no diretório de entrada
    for filename in os.listdir(input_dir):
        if filename.endswith('.mp4'):
            video_path = os.path.join(input_dir, filename)
            
            # Selecionar um arquivo de legenda aleatório
            selected_subtitle_file = random.choice(subtitle_files)
            subtitle_path = os.path.join(subtitles_dir, selected_subtitle_file)
            
            # Ler o conteúdo do arquivo de legenda
            with open(subtitle_path, 'r') as f:
                subtitle_text = f.read()

            # Selecionar um arquivo de música aleatório
            selected_music_file = random.choice(music_files)
            music_path = os.path.join(music_dir, selected_music_file)
            
            # Adicionar legenda e música ao vídeo
            add_subtitle_and_music_to_video(video_path, subtitle_text, music_path, output_dir)

# Uso
input_dir = r'C:\Users\USUARIO\Desktop\Agendamento\instagram\entrada'
subtitles_dir = r'C:\Users\USUARIO\Desktop\Agendamento\instagram\legendas'
music_dir = r'C:\Users\USUARIO\Desktop\Agendamento\instagram\musicas'
output_dir = r'C:\Users\USUARIO\Desktop\Agendamento\instagram\saida'

process_videos_in_directory(input_dir, subtitles_dir, music_dir, output_dir)