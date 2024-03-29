from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from tkinter import messagebox
import os

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")

        # Create a Canvas widget as the background
        self.canvas = Canvas(self.root)
        self.canvas.pack(fill=BOTH, expand=YES)

        # Create a Vertical Scrollbar
        scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Load and set the background image
        self.bg_img_path = "./asset/images/background_image.png"
        self.update_bg_image()

        self.title_text = "Face Recognition System"
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

        #=======================================================================
        #============================ LEFT FRAME ===============================
        #=======================================================================

              # Student Detail Button
        img4 = Image.open(
            r"./asset/images/detail_icon.png"
        )
        img4 = img4.resize((200, 200), Image.BICUBIC)
        self.photoImg4 = ImageTk.PhotoImage(img4)

        b1 = Button(image=self.photoImg4, command=self.open_student, cursor="hand2")
        b1.place(x=300, y=200, width=220, height=220)

        b2 = Button(
            text="Student Details",
            command=self.open_student,
            bg="blue",
            font=("Arival", 14),
            fg="white",
            cursor="hand2",
        )
        b2.place(x=300, y=418, width=220, height=50)

        # Face Detector
        img5 = Image.open(
            r"./asset/images/face_detector.png"
        )
        img5 = img5.resize((200, 200), Image.BICUBIC)
        self.photoImg5 = ImageTk.PhotoImage(img5)

        b3 = Button(
            image=self.photoImg5, command=self.open_face_detector, cursor="hand2"
        )
        b3.place(x=550, y=200, width=220, height=220)

        b3 = Button(
            text="Face Detector",
            command=self.open_face_detector,
            bg="blue",
            font=("Arival", 14),
            fg="white",
            cursor="hand2",
        )
        b3.place(x=550, y=418, width=220, height=50)

        # Show Attendance
        img6 = Image.open(
            r"./asset/images/attendance.jpg"
        )
        img6 = img6.resize((200, 200), Image.BICUBIC)
        self.photoImg6 = ImageTk.PhotoImage(img6)

        b4 = Button(image=self.photoImg6, cursor="hand2")
        b4.place(x=800, y=200, width=220, height=220)

        b5 = Button(
            text="Attendance",
            bg="blue",
            font=("Arival", 14),
            fg="white",
            cursor="hand2",
        )
        b5.place(x=800, y=418, width=220, height=50)

        # Help Desk Center
        img7 = Image.open(
            r"./asset/images/help-desk.png"
        )
        img7 = img7.resize((200, 200), Image.BICUBIC)
        self.photoImg7 = ImageTk.PhotoImage(img7)

        b6 = Button(image=self.photoImg7, command=self.open_developer, cursor="hand2")
        b6.place(x=1050, y=200, width=220, height=220)

        b7 = Button(
            text="Help Desk",
            command=self.open_developer,
            bg="blue",
            font=("Arival", 14),
            fg="white",
            cursor="hand2",
        )
        b7.place(x=1050, y=418, width=220, height=50)

        # BELOW IMAGE CONTAINER

        # Train Data
        img8 = Image.open(
            r"./asset/images/train_data.jpg"
        )
        img8 = img8.resize((200, 200), Image.BICUBIC)
        self.photoImg8 = ImageTk.PhotoImage(img8)

        b8 = Button(image=self.photoImg8, comman=self.trained_data, cursor="hand2")
        b8.place(x=300, y=500, width=220, height=220)

        b9 = Button(
            text="Train Data",
            comman=self.trained_data,
            bg="blue",
            font=("Arival", 14),
            fg="white",
            cursor="hand2",
        )
        b9.place(x=300, y=718, width=220, height=50)

        # Photos
        img9 = Image.open(
            r"./asset/images/photos.png"
        )
        img9 = img9.resize((200, 200), Image.BICUBIC)
        self.photoImg9 = ImageTk.PhotoImage(img9)

        b10 = Button(image=self.photoImg9, cursor="hand2")
        b10.place(x=550, y=500, width=220, height=220)

        b11 = Button(
            text="Photos", bg="blue", font=("Arival", 14), fg="white", cursor="hand2"
        )
        b11.place(x=550, y=718, width=220, height=50)

        # Developers
        img10 = Image.open(
            r"./asset/images/developer_image.png"
        )
        img10 = img10.resize((200, 200), Image.BICUBIC)
        self.photoImg10 = ImageTk.PhotoImage(img10)

        b12 = Button(image=self.photoImg10, command=self.open_developer, cursor="hand2")
        b12.place(x=800, y=500, width=220, height=220)

        b13 = Button(
            text="Developers",
            command=self.open_developer,
            bg="blue",
            font=("Arival", 14),
            fg="white",
            cursor="hand2",
        )
        b13.place(x=800, y=718, width=220, height=50)

        # Exiting
        
        img11 = Image.open(
            r"./asset/images/exit_image.png"
        )
        img11 = img11.resize((200, 200), Image.BICUBIC)
        self.photoImg11 = ImageTk.PhotoImage(img11)

        b14 = Button(image=self.photoImg11, command=root.quit, cursor="hand2")
        b14.place(x=1050, y=500, width=220, height=220)
        
        b15 = Button(
            text="Exit", command=root.quit, bg="blue", font=("Arival", 14), fg="white", cursor="hand2"
        )
        b15.place(x=1050, y=718, width=220, height=50)

    def open_student(self):
        self.root.destroy()  # Close the current window
        os.system("python student.py")

    def open_face_detector(self):
        self.root.destroy()
        os.system("python camera.py")

    def open_developer(self):
        self.root.destroy()
        os.system("python developer.py")

    def open_helpdesk(self):
        self.root.destroy()
        os.system("python helpdesk.py")

    def trained_data(self):
        from trainedData import Image_Data_Trained

        image_data_trained_instance = Image_Data_Trained()
        image_data_trained_instance.detect_faces()
        if hasattr(image_data_trained_instance):
            messagebox.showinfo("Image data trained")
        else:
            messagebox.showinfo("Image data not trained")

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
    root.geometry("1440x1080")  # Set an initial size for the window
    root.mainloop()
