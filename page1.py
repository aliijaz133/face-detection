import tkinter as tk
from tkinter import ttk

class Page1(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()



    def create_widgets(self):
        self.button = ttk.Button(self, text="Go to Page 2", command=self.go_to_page2)
        self.button.pack(pady=20)

    def go_to_page2(self):
        from page2 import Page2  # Import Page2 here to avoid circular import
        self.master.switch_frame(Page2)
