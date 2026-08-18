import tkinter as tk
from PIL import Image, ImageTk
import os

IMAGE_FILENAME = "santa-yadon.png"  # 今のファイル名に合わせる

def show_window():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, IMAGE_FILENAME)

    while True:
        root = tk.Tk()
        root.title("閉じられません")

        img = Image.open(image_path)
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(root, image=photo)
        label.image = photo
        label.pack()

        def on_close():
            root.destroy()

        root.protocol("WM_DELETE_WINDOW", on_close)
        root.mainloop()

show_window()