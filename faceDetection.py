from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog
import pymongo


class Face_Detector:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")

        self.canvas = Canvas(self.root)
        self.canvas.pack(fill=BOTH, expand=YES)

        # Create a Vertical Scrollbar
        scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Load and set the background image
        self.bg_img_path = "/home/usamaumer/PycharmProjects/pythonProject/asset/images/background_image.png"
        self.update_bg_image()

        # Create a title label with a specified font
        self.title_text = "Onlive Face Detection"
        self.title_lbl = Label(
            text=self.title_text,
            font=("Times New Roman", 25, "bold"),
            bg="black",
            fg="white",
        )
        self.title_lbl.place(x=0, y=0, relwidth=1.0)

        # Configure column weights to allow for responsive resizing
        self.canvas.columnconfigure(0, weight=1)
        self.canvas.columnconfigure(1, weight=1)

        # Bind the window resize event to update the background image and title label
        self.root.bind("<Configure>", self.on_resize)


    def update_bg_image(self, event=None):
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()

        bg_img = Image.open(self.bg_img_path)
        bg_img = bg_img.resize((window_width, window_height), Image.BICUBIC)
        self.bg_photo = ImageTk.PhotoImage(bg_img)
        self.canvas.config(width=window_width, height=window_height)
        self.canvas.create_image(0, 0, anchor=NW, image=self.bg_photo)

    def on_resize(self, event):
        # Update the title label width on window resize
        window_width = self.root.winfo_width()
        self.title_lbl.config(width=window_width)
        self.update_bg_image()


if __name__ == "__main__":
    root = Tk()
    app = Face_Detector(root)
    root.geometry("1440x800")
    root.bind("<Configure>", app.on_resize)
    root.mainloop()