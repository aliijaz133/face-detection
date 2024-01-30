# import tkinter as tk
# from tkinter import ttk
# from dashboard import Face_Recognition_System
#
# class MainApplication(tk.Tk):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.title("Face Recognition System")
#         self.geometry("1440x1080")
#         self.current_frame = None
#         self.switch_frame(Face_Recognition_System, self)  # Pass self as an argument
#
#     def switch_frame(self, frame_class, master):
#         new_frame = frame_class(master)
#         if self.current_frame:
#             self.current_frame.destroy()
#         self.current_frame = new_frame
#         self.current_frame.pack()
#
# if __name__ == "__main__":
#     app = MainApplication()
#     app.mainloop()


# import tkinter as tk
# from tkinter import ttk
# from page1 import Page1
# from page2 import Page2
#
# class MainApplication(tk.Tk):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.title("Tkinter Navigation Example")
#         self.geometry("300x200")
#         self.current_frame = None
#         self.switch_frame(Page1)
#
#     def switch_frame(self, frame_class):
#         new_frame = frame_class(self)
#         if self.current_frame:
#             self.current_frame.destroy()
#         self.current_frame = new_frame
#         self.current_frame.pack()
#
# if __name__ == "__main__":
#     app = MainApplication()
#     app.mainloop()
