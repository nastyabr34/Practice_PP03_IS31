import os
import time
import sys
from tkinter import Tk, Label, Button, Entry, StringVar, filedialog
from PIL import Image
import psutil  

def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss

def select_image():
    file_path = filedialog.askopenfilename(title="Выберите изображение", filetypes=[("Images", "*.jpg;*.png;*.jpeg")])
    if file_path:
        image_path.set(file_path)
        load_image(file_path)

def load_image(file_path):
    start_time = time.time()
    img = Image.open(file_path)
    img.thumbnail((200, 200)) 
    image_label.config(image=img)
    image_label.image = img 
    end_time = time.time()
    print(f"Время загрузки изображения: {end_time - start_time:.5f} секунд")
    print(f"Используемая память: {get_memory_usage()} байт")

def select_destination_folder():
    folder_path = filedialog.askdirectory(title="Выберите папку для сохранения")
    if folder_path:
        destination_path.set(folder_path)

def convert_image():
    src_path = image_path.get()
    dest_folder = destination_path.get()
    conversion_type = conv_type.get()

    if not src_path or not dest_folder or not conversion_type:
        info.set("Пожалуйста, заполните все поля.")
        return

    try:
        start_time = time.time()
        img = Image.open(src_path)
        base_name = os.path.basename(src_path)
        new_file_name = os.path.splitext(base_name)[0] + f'.{conversion_type.lower()}'
        new_file_path = os.path.join(dest_folder, new_file_name)

        if conversion_type.lower() == 'jpg':
            img.convert('RGB').save(new_file_path, 'JPEG')
        elif conversion_type.lower() == 'png':
            img.save(new_file_path, 'PNG')

        end_time = time.time()
        info.set(f"Изображение сохранено: {new_file_path}")
        print(f"Время конвертации изображения: {end_time - start_time:.5f} секунд")
        print(f"Используемая память: {get_memory_usage()} байт")
    except Exception as e:
        info.set(f"Ошибка: {str(e)}")

root = Tk()
root.title("Конвертер изображений")

image_path = StringVar()
destination_path = StringVar()
conv_type = StringVar()
info = StringVar()

Label(root, text="Путь к изображению:").grid(row=0, column=0, padx=10, pady=10)
Entry(root, textvariable=image_path, width=50).grid(row=0, column=1, padx=10, pady=10)
Button(root, text="Выбрать изображение", command=select_image).grid(row=0, column=2, padx=10, pady=10)

Label(root, text="Тип конвертации:").grid(row=1, column=0, padx=10, pady=10)
Entry(root, textvariable=conv_type, width=5).grid(row=1, column=1, padx=10, pady=10)

Label(root, text="Выбрать папку:").grid(row=2, column=0, padx=10, pady=10)
Entry(root, textvariable=destination_path, width=50).grid(row=2, column=1, padx=10, pady=10)
Button(root, text="Выбрать папку", command=select_destination_folder).grid(row=2, column=2, padx=10, pady=10)

Button(root, text="Конвертировать", command=convert_image).grid(row=3, column=0, columnspan=3, pady=10)

image_label = Label(root)
image_label.grid(row=0, column=3, rowspan=4, padx=10, pady=10)

Label(root, textvariable=info, fg="green").grid(row=4, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
