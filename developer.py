from tkinter import *
from tkinter import ttk, Label, Frame
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
        img_path = (
            "/home/usamaumer/PycharmProjects/pythonProject/asset/images/ali_ijaz.png"
        )
        my_image = Image.open(img_path)
        my_image = my_image.resize((150, 150), Image.BICUBIC)
        mask = self.create_circle_mask((150, 150))
        my_image.putalpha(mask)
        my_image = ImageTk.PhotoImage(my_image)
        image_label = Label(Image_Frame, image=my_image, bg="white", cursor="hand2")
        image_label.image = my_image
        image_label.pack(pady=5)

        # =========================== DETAIL FRAME =============================
        Detail_Frame = LabelFrame(
            Main_Frame,
            text="▌│█║▌│█║▌║▌║║▌║▌║█│▌▌║▌║║▌▌│█║▌║▌█║█│▌▌║▌║█│▌║▌║▌║",
            font=("", 14),
        )
        Detail_Frame.place(x=10, y=170, width=640, height=400)

        # =========================================================================
        # ===================== Left Below Frame For Skills =======================
        # =========================================================================

        Below_Frame = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="Skills",
            font=("Times New Roman", 14),
            bg="white",
        )
        Below_Frame.place(x=40, y=680, width=660, height=290)
        Below_Frame.config(background="white")

        # =========================== DETAIL FRAME =============================
        Below_Sec_Frame = LabelFrame(Below_Frame, text="", font=("", 14))
        Below_Sec_Frame.place(x=10, y=2, width=640, height=260)

        # ======================== Python =================================
        dot1 = Label(
            Below_Sec_Frame, text="•", font=("Times New Roman", 15), cursor="xterm"
        )
        dot1.grid(row=0, column=0, padx=5, pady=5)
        label1 = Label(
            Below_Sec_Frame, text="Python", font=("Times New Roman", 14), cursor="xterm"
        )
        label1.grid(row=0, column=1, padx=0, pady=5, sticky=W)

        # ======================== Tkinter =================================
        dot2 = Label(
            Below_Sec_Frame, text="•", font=("Times New Roman", 15), cursor="xterm"
        )
        dot2.grid(row=1, column=0, padx=5, pady=5)
        label2 = Label(
            Below_Sec_Frame,
            text="Tkinter",
            font=("Times New Roman", 14),
            cursor="xterm",
        )
        label2.grid(row=1, column=1, padx=0, pady=5, sticky=W)

        # ======================== HTML5 =================================
        dot3 = Label(
            Below_Sec_Frame, text="•", font=("Times New Roman", 15), cursor="xterm"
        )
        dot3.grid(row=2, column=0, padx=5, pady=5)
        label3 = Label(
            Below_Sec_Frame, text="HTML5", font=("Times New Roman", 14), cursor="xterm"
        )
        label3.grid(row=2, column=1, padx=0, pady=5, sticky=W)

        # ======================== CSS =================================
        dot4 = Label(
            Below_Sec_Frame, text="•", font=("Times New Roman", 15), cursor="xterm"
        )
        dot4.grid(row=3, column=0, padx=5, pady=5)
        label4 = Label(
            Below_Sec_Frame, text="CSS", font=("Times New Roman", 14), cursor="xterm"
        )
        label4.grid(row=3, column=1, padx=0, pady=5, sticky=W)

        # ========================Javascript=================================
        dot5 = Label(
            Below_Sec_Frame, text="•", font=("Times New Roman", 15), cursor="xterm"
        )
        dot5.grid(row=4, column=0, padx=5, pady=5)
        label5 = Label(
            Below_Sec_Frame,
            text="Javascript",
            font=("Times New Roman", 14),
            cursor="xterm",
        )
        label5.grid(row=4, column=1, padx=0, pady=5, sticky=W)

        # ======================== Typescript =================================
        dot6 = Label(
            Below_Sec_Frame, text="•", font=("Times New Roman", 15), cursor="xterm"
        )
        dot6.grid(row=5, column=0, padx=5, pady=5)
        label6 = Label(
            Below_Sec_Frame,
            text="Typescript",
            font=("Times New Roman", 14),
            cursor="xterm",
        )
        label6.grid(row=5, column=1, padx=0, pady=5, sticky=W)

        # ======================== C++ =================================
        dot7 = Label(
            Below_Sec_Frame, text="•", font=("Times New Roman", 15), cursor="xterm"
        )
        dot7.grid(row=6, column=0, padx=5, pady=5)
        label7 = Label(
            Below_Sec_Frame, text="C++", font=("Times New Roman", 14), cursor="xterm"
        )
        label7.grid(row=6, column=1, padx=0, pady=5, sticky=W)

        # ======================== Angular Material =================================
        dot8 = Label(
            Below_Sec_Frame, text="•", font=("Times New Roman", 15), cursor="xterm"
        )
        dot8.grid(row=0, column=2, padx=5, pady=5)
        label8 = Label(
            Below_Sec_Frame,
            text="Angular Material",
            font=("Times New Roman", 14),
            cursor="xterm",
        )
        label8.grid(row=0, column=3, padx=0, pady=5, sticky=W)

        # ======================== Ant Design Material =================================
        dot9 = Label(
            Below_Sec_Frame, text="•", font=("Times New Roman", 15), cursor="xterm"
        )
        dot9.grid(row=1, column=2, padx=5, pady=5)
        label9 = Label(
            Below_Sec_Frame,
            text="Ant Design Material",
            font=("Times New Roman", 14),
            cursor="xterm",
        )
        label9.grid(row=1, column=3, padx=0, pady=5, sticky=W)

        # ======================== Ng-Prime Material =================================
        dot10 = Label(
            Below_Sec_Frame, text="•", font=("Times New Roman", 15), cursor="xterm"
        )
        dot10.grid(row=2, column=2, padx=5, pady=5)
        label10 = Label(
            Below_Sec_Frame,
            text="Ng-Prime Material",
            font=("Times New Roman", 14),
            cursor="xterm",
        )
        label10.grid(row=2, column=3, padx=0, pady=5, sticky=W)

        # ======================== Ng-Zorro Material =================================
        dot11 = Label(
            Below_Sec_Frame, text="•", font=("Times New Roman", 15), cursor="xterm"
        )
        dot11.grid(row=3, column=2, padx=5, pady=5)
        label11 = Label(
            Below_Sec_Frame,
            text="Ng-Zorro Material",
            font=("Times New Roman", 14),
            cursor="xterm",
        )
        label11.grid(row=3, column=3, padx=0, pady=5, sticky=W)

        # ======================== Adobe Photoshop =================================
        dot12 = Label(
            Below_Sec_Frame, text="•", font=("Times New Roman", 15), cursor="xterm"
        )
        dot12.grid(row=4, column=2, padx=5, pady=5)
        label12 = Label(
            Below_Sec_Frame,
            text="Adobe Photoshop",
            font=("Times New Roman", 14),
            cursor="xterm",
        )
        label12.grid(row=4, column=3, padx=0, pady=5, sticky=W)

        # ======================== Adobe Illustrator =================================
        dot13 = Label(
            Below_Sec_Frame, text="•", font=("Times New Roman", 15), cursor="xterm"
        )
        dot13.grid(row=5, column=2, padx=5, pady=5)
        label13 = Label(
            Below_Sec_Frame,
            text="Adobe Illustrator",
            font=("Times New Roman", 14),
            cursor="xterm",
        )
        label13.grid(row=5, column=3, padx=0, pady=5, sticky=W)

        # ======================== Adobe After Effects =================================
        dot14 = Label(
            Below_Sec_Frame, text="•", font=("Times New Roman", 15), cursor="xterm"
        )
        dot14.grid(row=6, column=2, padx=5, pady=5)
        label14 = Label(
            Below_Sec_Frame,
            text="Adobe After Effects",
            font=("Times New Roman", 14),
            cursor="xterm",
        )
        label14.grid(row=6, column=3, padx=0, pady=5, sticky=W)

        # ======================== Adobe Premier =================================
        dot15 = Label(
            Below_Sec_Frame, text="•", font=("Times New Roman", 15), cursor="xterm"
        )
        dot15.grid(row=0, column=4, padx=5, pady=5)
        label15 = Label(
            Below_Sec_Frame,
            text="Adobe Premier",
            font=("Times New Roman", 14),
            cursor="xterm",
        )
        label15.grid(row=0, column=5, padx=0, pady=5, sticky=W)

        # ======================== Ms-Office =================================
        dot16 = Label(
            Below_Sec_Frame, text="•", font=("Times New Roman", 15), cursor="xterm"
        )
        dot16.grid(row=1, column=4, padx=5, pady=5)
        label16 = Label(
            Below_Sec_Frame,
            text="Ms-Office",
            font=("Times New Roman", 14),
            cursor="xterm",
        )
        label16.grid(row=1, column=5, padx=0, pady=5, sticky=W)

        # ======================== In-Page =================================
        dot17 = Label(
            Below_Sec_Frame, text="•", font=("Times New Roman", 15), cursor="xterm"
        )
        dot17.grid(row=2, column=4, padx=5, pady=5)
        label17 = Label(
            Below_Sec_Frame,
            text="In-Page",
            font=("Times New Roman", 14),
            cursor="xterm",
        )
        label17.grid(row=2, column=5, padx=0, pady=5, sticky=W)

        # =========================================================================
        # ===================== Right Frame For Projects ==========================
        # =========================================================================

        Right_Frame = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="Projects",
            font=("Times New Roman", 14),
            bg="white",
        )
        Right_Frame.place(x=740, y=70, width=660, height=900)
        Right_Frame.config(background="white")

        # =========================== DETAIL FRAME =============================
        Right_sec_Frame = LabelFrame(Right_Frame, text="", font=("", 14))
        Right_sec_Frame.place(x=10, y=2, width=640, height=870)

        # ======================== Sign Language Recognizer =================================
        heading_project_1 = Label(
            Right_sec_Frame,
            text="Sign Language Recognizer:",
            font=("Times New Roman", 15, "bold"),
            cursor="xterm",
        )
        heading_project_1.place(x=10, y=10)
        sign_langauge_detail = "In this project we proposed a method for recognizing hand gesture. Sign language Recognizer is the task of recognizing sign language gloses from video stream. It is very important research area since it can bridge communication gap between hearing and Deep people, facilitating the social inclusion of hearing impaired people. This type of gesture-based language allows people to convey ideas and thoughts easily overcoming the barries caused by difficulties from hearing issues."
        project_desc_1 = Label(
            Right_sec_Frame,
            text=sign_langauge_detail,
            font=("Times New Roman", 13),
            cursor="xterm",
            wraplength=600,
        )
        project_desc_1.place(x=20, y=40)
        project_dot_1 = Label(
            Right_sec_Frame, text="•", font=("Times New Roman", 15), cursor="xterm"
        )
        project_dot_1.place(x=30, y=170)
        project_bullet_point_1 = Label(
            Right_sec_Frame,
            text="SLR Capture signs",
            font=("Times New Roman", 13),
            cursor="xterm",
        )
        project_bullet_point_1.place(x=50, y=170)
        project_dot_2 = Label(
            Right_sec_Frame, text="•", font=("Times New Roman", 15), cursor="xterm"
        )
        project_dot_2.place(x=30, y=205)
        project_bullet_point_2 = Label(
            Right_sec_Frame,
            text="Convert the signs to text",
            font=("Times New Roman", 13),
            cursor="xterm",
        )
        project_bullet_point_2.place(x=50, y=205)

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
