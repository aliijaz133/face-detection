import bcrypt
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymongo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import os

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

        #=======================================================================
        #============================ LEFT FRAME ===============================
        #=======================================================================

        Right_Frame = Frame(self.root, bd=2)
        Right_Frame.config(background='white')
        Right_Frame.place(x=150, y=70, width=600, height=600, )

        Right_sec_Frame  = LabelFrame(Right_Frame, bd=2, text="User Login", font=("Times New Roman", 15, "bold"), cursor="hand2")
        Right_sec_Frame.config(background="LightBlue")
        Right_sec_Frame.place( x=10, y=10, width=580, height=580)

        # Labels and Entry for user login
        self.email_label = Label(Right_sec_Frame, text="Email:")
        self.email_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.email_entry = Entry(Right_sec_Frame)
        self.email_entry.grid(row=0, column=1, padx=10, pady=10)

        self.password_label = Label(Right_sec_Frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.password_entry = Entry(Right_sec_Frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        self.login_button = Button(Right_sec_Frame, text="Login", command=self.login)
        self.login_button.grid(row=2, columnspan=2, pady=10)

        self.forgot_password_button = Button(Right_sec_Frame, text="Forgot Password?", command=self.forgot_password)
        self.forgot_password_button.grid(row=3, columnspan=2)

        # MongoDB connection
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["student-login"]  # Replace "your_database_name" with your database name
        self.users_collection = self.db["users"]

    def login(self):
        # Get user input
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Find user by email
        user = self.users_collection.find_one({"email": email})

        if user:
            # Check if password matches
            if bcrypt.checkpw(password.encode('utf-8'), user['password']):
                messagebox.showinfo("Success", "Login successful!")
                self.root.destroy()  # Close the current window
                os.system("python student.py")  # Open student.py
            else:
                messagebox.showerror("Error", "Invalid email or password.")
        else:
            messagebox.showerror("Error", "Invalid email or password.")

    def forgot_password(self):
        # Get user input
        email = self.email_entry.get()

        # Find user by email
        user = self.users_collection.find_one({"email": email})

        if user:
            # Generate a new random password
            new_password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))

            # Update user's password in the database
            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
            self.users_collection.update_one({"email": email}, {"$set": {"password": hashed_password}})

            # Send email with new password
            self.send_email(email, new_password)

            messagebox.showinfo("Success", "New password sent to your email.")
        else:
            messagebox.showerror("Error", "Email not found.")

    def send_email(self, email, new_password):
        # Email configuration
        sender_email = "aliejaz0072@gmail.com"
        sender_password = "your_password"
        smtp_server = "smtp.example.com"

        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = "Password Recovery"
        body = f"Your new password is: {new_password}"
        msg.attach(MIMEText(body, 'plain'))

        # Send email
        with smtplib.SMTP(smtp_server, 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)

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
    root.geometry("1440x1080")
    root.mainloop()
