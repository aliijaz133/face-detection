from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")

        # Create a Canvas widget as the background
        self.canvas = Canvas(self.root)
        self.canvas.pack(fill=BOTH, expand=YES)

        # Load and set the background image
        self.bg_img_path = '/home/usamaumer/PycharmProjects/pythonProject/asset/images/background_image.png'
        self.update_bg_image()

        # Create and set up the first image label
        img1 = Image.open('/home/usamaumer/PycharmProjects/pythonProject/asset/images/fav_icon.png')
        img1 = img1.resize((100, 100), Image.BICUBIC)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.canvas, image=self.photoImg1, bg='white')
        f_lbl1.grid(row=0, column=0, padx=10, pady=10)

        # Create and set up the second image label
        img2 = Image.open('/home/usamaumer/PycharmProjects/pythonProject/dataset/images/aliijaz.jpg')
        img2 = img2.resize((100, 100), Image.BICUBIC)
        self.photoImg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.canvas, image=self.photoImg2, bg='white')
        f_lbl2.grid(row=0, column=1, padx=10, pady=10)

        # Create a title label with a specified font
        self.title_text = "Face Recognition System"
        self.title_lbl = Label(text=self.title_text, font=("Times New Roman", 35, "bold"), bg="black", fg="white")
        self.title_lbl.place(x=0, y=110, relwidth=1.0)  # Use relwidth to make the label span the full width

        # Configure column weights to allow for responsive resizing
        self.canvas.columnconfigure(0, weight=1)
        self.canvas.columnconfigure(1, weight=1)

        # Bind the window resize event to update the background image and title label
        self.root.bind("<Configure>", self.on_resize)

        # Student Detail Button
        img4 = Image.open(r"/home/usamaumer/PycharmProjects/pythonProject/asset/images/detail_icon.png")
        img4 = img4.resize((100, 100), Image.BICUBIC)
        self.photoImg4 = ImageTk.PhotoImage(img4)

        b1 = Button(image=self.photoImg4, cursor="hand2")
        b1.place(x=50, y=200, width=220, height=220)

        b1 = Button(text="Student Details", cursor="hand2")
        b1.place(x=50, y=400, width=220, height=50)

    def update_bg_image(self, event=None):
        # Resize and update the background image based on the window size
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
    obj = Face_Recognition_System(root)
    root.geometry("800x150")  # Set an initial size for the window
    root.mainloop()
