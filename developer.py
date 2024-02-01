from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System - Developer")

        # Create a Canvas widget as the background
        self.canvas = Canvas(self.root)
        self.canvas.pack(fill=BOTH, expand=YES)

        # Create a Vertical Scrollbar
        scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Load and set the background image
        self.bg_img_path = "/home/usamaumer/PycharmProjects/pythonProject/asset/images/background_image.png"
        self.update_bg_image()

        self.title_text = "Developer"
        self.title_lbl = Label(
            text=self.title_text,
            font=("Times New Roman", 35, "bold"),
            bg="black",
            fg="white",
        )
        self.title_lbl.place(
            x=0, y=0, relwidth=1.0
        )  # Use relwidth to make the label span the full width

        # Configure column weights to allow for responsive resizing
        self.canvas.columnconfigure(0, weight=1)
        self.canvas.columnconfigure(1, weight=1)

        # Bind the window resize event to update the background image and title label
        self.root.bind("<Configure>", self.on_resize)

        # =========================================================================
        # ===================== Right Frame For Portifilo =========================
        # =========================================================================

        Main_Frame = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="Portifilo",
            font=("Times New Roman", 14),
            bg="white",
        )
        Main_Frame.place(x=40, y=70, width=660, height=600)
        Main_Frame.config(background="white")

        # +----------------------------IMAGE--------------------------------+

        Image_Frame = Frame(Main_Frame, bg="white")
        Image_Frame.place(x=10, y=5, width=200, height=200)
        img_path = "/home/usamaumer/PycharmProjects/pythonProject/asset/images/ali_ijaz.png"
        my_image = Image.open(img_path)
        my_image = my_image.resize((150, 150), Image.BICUBIC)
        mask = self.create_circle_mask((150, 150))
        my_image.putalpha(mask)
        my_image = ImageTk.PhotoImage(my_image)
        image_label = Label(Image_Frame, image=my_image, bg="white", cursor="hand2")
        image_label.image = my_image
        image_label.pack(pady=5)


        # =========================== DETAIL FRAME =============================
        Detail_Frame = LabelFrame(Main_Frame, text="▌│█║▌│█║▌║▌║║▌║▌║█│▌▌║▌║║▌▌│█║▌║▌█║█│▌▌║▌║█│▌║▌║▌║", font=("",14))
        Detail_Frame.place(x=10, y=170, width=640, height=400)

        # =========================================================================
        # ===================== Right Frame For Portifilo =========================
        # =========================================================================

        Main_Frame = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="Projects",
            font=("Times New Roman", 14),
            bg="white",
        )
        Main_Frame.place(x=740, y=70, width=660, height=600)
        Main_Frame.config(background="white")

        # =========================== DETAIL FRAME =============================
        Detail_Frame = LabelFrame(Main_Frame, text="", font=("",14))
        Detail_Frame.place(x=10, y=2, width=640, height=570)

    # =========================================================================
    # ============================== FUNCTIONS ================================
    # =========================================================================

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

    def create_circle_mask(self, size):
        mask = Image.new("L", size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size[0], size[1]), fill=255)
        return mask
    

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.geometry("1440x1080")
    root.mainloop()
