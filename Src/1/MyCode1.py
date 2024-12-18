import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

class ImageConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Converter")
        self.master.geometry("600x400")

        self.image_path = None

        self.info_label = tk.Label(master, text="Здесь будет информация о действиях пользователя\\n", justify='left')
        self.info_label.pack(side='left', padx=10, pady=10)

        self.img_label = tk.Label(master)
        self.img_label.pack(side='right', padx=10, pady=10)

        self.load_button = tk.Button(master, text="Загрузить изображения", command=self.load_image)
        self.load_button.pack(side='top', padx=10, pady=10)

        self.convert_button = tk.Button(root, text="Изменить расширение (PNG to JPG, JPG to PNG)", command=self.convert_image)
        self.convert_button.pack(padx=10, pady=10)

        self.image_label = tk.Label(root)
        self.image_label.grid(row=0, column=1, rowspan=4)
        
    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if self.image_path:
            self.info_label.config(text=f"Загружено изображение: {os.path.basename(self.image_path)}\\n")
            self.show_image(self.image_path)
            self.convert_button.config(state=tk.NORMAL)

    def show_image(self, path):
        img = Image.open(path)
        img.thumbnail((30, 30))
        self.img = img
        self.img_photo = tk.PhotoImage(img)
        self.img_label.config(image=self.img_photo)

    def convert_image(self):
        if self.image_path:
            if self.image_path.lower().endswith('.png'):
                new_path = self.image_path[:-4] + '.jpg'
                self.img.convert('RGB').save(new_path)
                self.info_label.config(text=f"Изображение сохранено как: {os.path.basename(new_path)}\\n")
            elif self.image_path.lower().endswith('.jpg'):
                new_path = self.image_path[:-4] + '.png'
                self.img.save(new_path)
                self.info_label.config(text=f"Изображение сохранено как: {os.path.basename(new_path)}\\n")
            else:
                messagebox.showerror("Ошибка", "Неверный формат изображения.")
        else:
            messagebox.showerror("Ошибка", "Сначала загрузите изображение.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverterApp(root)
    root.mainloop()
