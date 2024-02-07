from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymongo
import bcrypt

class Help_Desk:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System - Helpdesk")

        # Create MongoDB client
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")  # Update with your MongoDB connection URI
        self.db = self.client["student-login"]  # Replace "your_database_name" with your database name
        self.users_collection = self.db["users"]

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
        
        #=======================================================================
        #============================ LEFT FRAME ===============================
        #=======================================================================

        Right_Frame = Frame(self.root, bd=2)
        Right_Frame.config(background='white')
        Right_Frame.place(x=150, y=70, width=600, height=600, )

        Right_sec_Frame  = LabelFrame(Right_Frame, bd=2, text="User Registration", font=("Times New Roman", 15, "bold"), cursor="hand2")
        Right_sec_Frame.config(background="LightBlue")
        Right_sec_Frame.place( x=10, y=10, width=580, height=580)

        # Labels and Entry for user signup
        self.username_label = Label(Right_sec_Frame, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.username_entry = Entry(Right_sec_Frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        self.email_label = Label(Right_sec_Frame, text="Email:")
        self.email_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.email_entry = Entry(Right_sec_Frame)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10)

        self.password_label = Label(Right_sec_Frame, text="Password:")
        self.password_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        self.password_entry = Entry(Right_sec_Frame, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

        self.signup_button = Button(Right_sec_Frame, text="Sign Up", command=self.signup)
        self.signup_button.grid(row=3, columnspan=2, pady=10)

    def signup(self):
        # Get user input
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()

        # Check if email is unique
        if self.users_collection.find_one({"email": email}):
            messagebox.showerror("Error", "Email already exists. Please use a different email.")
            return

        # Hash the password using bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Insert user data into MongoDB
        user_data = {"username": username, "password": hashed_password, "email": email}
        self.users_collection.insert_one(user_data)

        # Show success message
        messagebox.showinfo("Success", "User registered successfully.")

        # Clear input fields after signup
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.email_entry.delete(0, END)

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
