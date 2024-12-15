import os
import time
from PIL import Image

def load_image(file_path):
    start_time = time.time()
    img = Image.open(file_path)
    load_time = time.time() - start_time
    print(f"Загрузка изображения: {load_time:.4f} секунды")
    return img

def convert_image(src_path, dest_folder, conversion_type):
    start_time = time.time()
    img = load_image(src_path)
    base_name = os.path.basename(src_path)
    new_file_name = os.path.splitext(base_name)[0] + f'.{conversion_type.lower()}'
    new_file_path = os.path.join(dest_folder, new_file_name)

    if conversion_type.lower() == 'jpg':
        img.convert('RGB').save(new_file_path, 'JPEG')
    elif conversion_type.lower() == 'png':
        img.save(new_file_path, 'PNG')

    conversion_time = time.time() - start_time
    print(f"Конвертация изображения: {conversion_time:.4f} секунды")

    src_size = os.path.getsize(src_path)
    dest_size = os.path.getsize(new_file_path)
    print(f"Размер исходного файла: {src_size / 1024:.2f} КБ")
    print(f"Размер нового файла: {dest_size / 1024:.2f} КБ")

    return new_file_path

