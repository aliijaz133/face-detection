from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Help_Desk:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System - Helpdesk")

        # Create a Canvas widget as the background
        self.canvas = Canvas(self.root)
        self.canvas.pack(fill=BOTH, expand=YES)

        # Create a Vertical Scrollbar
        scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Load and set the background image
        self.bg_img_path = "./asset/images/background_image.png"
        self.update_bg_image()

        self.title_text = "Helpdesk"
        self.title_lbl = Label(
            text=self.title_text,
            font=("Times New Roman", 35, "bold"),
            bg="black",
            fg="white",
        )
        self.title_lbl.place(x=0, y=0, relwidth=1.0)

        self.canvas.columnconfigure(0, weight=1)
        self.canvas.columnconfigure(1, weight=1)

        self.root.bind("<Configure>", self.on_resize)


	
        # root = Tk()
        # menu = Menu(root)
        # root.config(menu=menu)
        # filemenu = Menu(menu)
        # menu.add_cascade(label='File', menu=filemenu)
        # filemenu.add_command(label='New')
        # filemenu.add_command(label='Open...')
        # filemenu.add_separator()
        # filemenu.add_command(label='Exit', command=root.quit)
        # helpmenu = Menu(menu)
        # menu.add_cascade(label='Help', menu=helpmenu)
        # helpmenu.add_command(label='About')



        #=======================================================================
        #============================ LEFT FRAME ===============================
        #=======================================================================

        Right_Frame = Frame(self.root, bd=2)
        Right_Frame.config(background='white')
        Right_Frame.place(x=150, y=70, width=600, height=600, )

        Right_sec_Frame  = LabelFrame(Right_Frame, bd=2, text="User Registration", font=("Times New Roman", 15, "bold"), cursor="hand2")
        Right_sec_Frame.config(background="LightBlue")
        Right_sec_Frame.place( x=10, y=10, width=580, height=580)

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
    obj = Help_Desk(root)
    root.geometry("1440x1080")  # Set an initial size for the window
    root.mainloop()
