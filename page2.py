import tkinter as tk
from tkinter import ttk

class Page2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self, text="Welcome to Page 2")
        self.label.pack(pady=20)

        self.back_button = ttk.Button(self, text="Go back to Page 1", command=self.go_to_page1)
        self.back_button.pack()

    def go_to_page1(self):
        from page1 import Page1  # Import Page1 here to avoid circular import
        self.master.switch_frame(Page1)
