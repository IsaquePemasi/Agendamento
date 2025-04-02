# pip install pillow ffmpeg-python

import os
import random
from PIL import Image, ImageDraw, ImageFont
import ffmpeg

def create_subtitle_images(subtitle_texts, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for i, text in enumerate(subtitle_texts):
        img = Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 50)
        text_width, text_height = draw.textsize(text, font=font)
        position = ((1920 - text_width) / 2, (1080 - text_height) / 2)
        draw.text(position, text, font=font, fill="white")
        
        img_path = os.path.join(output_dir, f"subtitle_{i}.png")
        img.save(img_path)

def create_instagram_subtitle_image(text, output_dir):
    img = Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 50)
    text_width, text_height = draw.textsize(text, font=font)
    position = ((1920 - text_width) / 2, 50)
    draw.text(position, text, font=font, fill="white")
    
    img_path = os.path.join(output_dir, "instagram_subtitle.png")
    img.save(img_path)

def add_images_to_video(video_path, subtitle_images_dir, middle_image_path, output_path):
    input_video = ffmpeg.input(video_path)
    video_duration = float(ffmpeg.probe(video_path)['format']['duration'])

    subtitle_images = [os.path.join(subtitle_images_dir, img) for img in sorted(os.listdir(subtitle_images_dir)) if img.endswith(".png")]
    video_streams = [input_video]

    for i, img_path in enumerate(subtitle_images):
        start_time = (video_duration / len(subtitle_images)) * i
        end_time = start_time + (video_duration / len(subtitle_images))
        video_streams.append(
            ffmpeg.input(img_path, stream_loop=-1, t=end_time-start_time)
            .filter('scale', 1920, 1080)
            .filter('overlay', x=0, y=0, enable=f'between(t,{start_time},{end_time})')
        )

    video_streams.append(
        ffmpeg.input(middle_image_path, stream_loop=-1, t=video_duration)
        .filter('scale', 1920, 1080)
        .filter('overlay', x=0, y=0, enable=f'between(t,0,{video_duration})')
    )

    ffmpeg.concat(*video_streams, v=1, a=1).output(output_path).run(overwrite_output=True)

def process_videos_in_directory(input_dir, subtitles_dir, instagram_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    subtitle_files = [f for f in os.listdir(subtitles_dir) if f.endswith('.txt')]

    with open(instagram_file, 'r', encoding='utf-8') as f:
        middle_text = f.read().strip()

    for filename in os.listdir(input_dir):
        if filename.endswith('.mp4'):
            video_path = os.path.join(input_dir, filename)
            selected_subtitle_file = random.choice(subtitle_files)
            subtitle_path = os.path.join(subtitles_dir, selected_subtitle_file)
            
            with open(subtitle_path, 'r', encoding='utf-8') as f:
                subtitle_texts = f.read().splitlines()
            
            subtitle_images_dir = os.path.join(output_dir, "subtitles")
            create_subtitle_images(subtitle_texts, subtitle_images_dir)
            middle_image_path = os.path.join(output_dir, "instagram_subtitle.png")
            create_instagram_subtitle_image(middle_text, output_dir)
            
            output_video_path = os.path.join(output_dir, filename)
            add_images_to_video(video_path, subtitle_images_dir, middle_image_path, output_video_path)

input_dir = r'C:\Users\USUARIO\Desktop\Agendamento\instagram\entrada'
subtitles_dir = r'C:\Users\USUARIO\Desktop\Agendamento\instagram\legendas'
instagram_file = r'C:\Users\USUARIO\Desktop\Agendamento\instagram\instagram.txt'
output_dir = r'C:\Users\USUARIO\Desktop\Agendamento\instagram\saida'

process_videos_in_directory(input_dir, subtitles_dir, instagram_file, output_dir)