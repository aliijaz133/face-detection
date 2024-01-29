from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Student:
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
        self.bg_img_path = '/home/usamaumer/PycharmProjects/pythonProject/asset/images/background_image.png'
        self.update_bg_image()

        # Create a title label with a specified font
        self.title_text = "Student Management System"
        self.title_lbl = Label(text=self.title_text, font=("Times New Roman", 25, "bold"), bg="black", fg="white")
        self.title_lbl.place(x=0, y=0, relwidth=1.0)

        # Configure column weights to allow for responsive resizing
        self.canvas.columnconfigure(0, weight=1)
        self.canvas.columnconfigure(1, weight=1)

        # Bind the window resize event to update the background image and title label
        self.root.bind("<Configure>", self.on_resize)

        # Left label Frame
        Left_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Student Details", font=("Times New Roman", 15, "bold"))
        Left_frame.place(x=50, y=100, width=660, height=580)

        Left_sec_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Current Course Information", font=("Times New Roman", 15))
        Left_sec_frame.place(x=70, y=140, width=620, height=120)

        #Add Department
        department_label = Label(Left_sec_frame, text="Department", font=("Cursive", 13))
        department_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(Left_sec_frame, font=("Times New Roman", 13), width=17, state='readonly')
        dep_combo['value'] = ('Please select', 'Computer Science', 'Management Science', 'Software Engineering', 'Media Science', 'Geo Physics')
        dep_combo.configure(background='white', foreground='black')
        dep_combo.current(0)
        dep_combo.place(y=30, x=10, height=35)
        dep_combo.grid(row=0, column=1, padx=2, sticky=W)

        #Add Years
        department_year = Label(Left_sec_frame, text="Year", font=("Cursive", 13))
        department_year.grid(row=0, column=2, padx=10, sticky=W)

        dep_year = ttk.Combobox(Left_sec_frame, font=("Times New Roman", 13), width=17, state='readonly')
        dep_year['value'] = ('Please select', 2019, 2020, 2021, 2022, 2023, 2024)
        dep_year.configure(background='white', foreground='black')
        dep_year.current(0)
        dep_year.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        #Add Semester
        department_sems = Label(Left_sec_frame, text="Semester", font=("Cursive", 13))
        department_sems.grid(row=2, column=0, padx=10, sticky=W)

        dep_sems = ttk.Combobox(Left_sec_frame, font=("Times New Roman", 13), width=17, state='readonly')
        dep_sems['value'] = ('Please select', '1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th')
        dep_sems.configure(background='white', foreground='black')
        dep_sems.current(0)
        dep_sems.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        #Add Course
        department_course = Label(Left_sec_frame, text="Courses", font=("Cursive", 13))
        department_course.grid(row=2, column=2, padx=10, sticky=W)

        dep_course = ttk.Combobox(Left_sec_frame, font=("Times New Roman", 13), width=17, state='readonly')
        dep_course['value'] = ('Please select', 'PF', 'SE', 'OOP', 'DSA', 'Web-Tech', 'Python', 'Data Science')
        dep_course.configure(background='white', foreground='black')
        dep_course.current(0)
        dep_course.grid(row=2, column=3, padx=2, pady=10, sticky=W)


        #Class Student Information
        Left_3rd_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Class Student Information", font=("Times New Roman", 15))
        Left_3rd_frame.place(x=70, y=270, width=620, height=280)
        #Student ID:
        student_id_lbl = Label(Left_3rd_frame, text="Student Id:", font=("Cursive", 13))
        student_id_lbl.grid(row=0, column=0, padx=5, sticky=W)
        student_id_entry = Entry(Left_3rd_frame, font=("Times New Roman",), bd=2)
        student_id_entry.grid(row=0, column=1)

        #Student Name:
        student_name_lbl = Label(Left_3rd_frame, text="Student name:", font=("Cursive", 13))
        student_name_lbl.grid(row=0, column=2, padx=5, sticky=W)
        student_name_entry = Entry(Left_3rd_frame, font=("Times New Roman",), bd=2)
        student_name_entry.grid(row=0, column=3)

        #Student Roll No:
        student_rollNo_lbl = Label(Left_3rd_frame, text="Student Roll No:", font=("Cursive", 13))
        student_rollNo_lbl.grid(row=2, column=0, padx=5, pady=15, sticky=W)
        student_rollNo_entry = Entry(Left_3rd_frame, font=("Times New Roman",), bd=2)
        student_rollNo_entry.grid(row=2, column=1, padx=5, pady=15, sticky=W)

        # Student Gender:
        student_gender_lbl = Label(Left_3rd_frame, text="Gender:", font=("Cursive", 13))
        student_gender_lbl.grid(row=2, column=2, padx=5, pady=15, sticky=W)
        student_gender_entry = Entry(Left_3rd_frame, font=("Times New Roman",), bd=2)
        student_gender_entry.grid(row=2, column=3, padx=5, pady=15, sticky=W)

        # Student DOB:
        student_dob_lbl = Label(Left_3rd_frame, text="Student DOB:", font=("Cursive", 13))
        student_dob_lbl.grid(row=3, column=0, padx=5, sticky=W)
        student_dob_entry = Entry(Left_3rd_frame, font=("Times New Roman",), bd=2)
        student_dob_entry.grid(row=3, column=1, padx=5, sticky=W)

        # Student Phone Number:
        student_ph_lbl = Label(Left_3rd_frame, text="Mobile Number:", font=("Cursive", 13))
        student_ph_lbl.grid(row=3, column=2, padx=5, pady=3, sticky=W)
        student_ph_entry = Entry(Left_3rd_frame, font=("Times New Roman",), bd=2)
        student_ph_entry.grid(row=3, column=3, padx=5, pady=3, sticky=W)

        # Student Email Address:
        student_email_lbl = Label(Left_3rd_frame, text="Student Email:", font=("Cursive", 13))
        student_email_lbl.grid(row=5, column=0, padx=5, sticky=W)
        student_email_entry = Entry(Left_3rd_frame, font=("Times New Roman",), bd=2)
        student_email_entry.grid(row=5, column=1, padx=5, sticky=W)

        # Student Address:
        student_address_lbl = Label(Left_3rd_frame, text="Address:", font=("Cursive", 13))
        student_address_lbl.grid(row=5, column=2, padx=5, pady=15, sticky=W)
        student_address_entry = Entry(Left_3rd_frame, font=("Times New Roman",), bd=2)
        student_address_entry.grid(row=5, column=3, padx=5, pady=15, sticky=W)

        # Add radio Button for Taking Picture
        radio_btn_1 = ttk.Radiobutton(Left_3rd_frame, text='Take Sample Photo', value=1)
        radio_btn_1.grid(row=6, column=0, padx=5, pady=5, sticky=W)

        radio_btn_2 = ttk.Radiobutton(Left_3rd_frame, text='Take Not Sample Photo', value=2)
        radio_btn_2.grid(row=6, column=1, padx=5, pady=5, sticky=W)

        # Cancel Button
        cancel_btn = Button(Left_3rd_frame, text="Cancel", font=("Times New Roman", 13), cursor="hand2", bg="LightBlue")
        cancel_btn.grid(row=7, column=2, padx=5, pady=5, sticky=W)

        # Submit Button
        save_btn = Button(Left_3rd_frame, text="Save", font=("Times New Roman", 13), cursor='hand2', bg="LightGreen")
        save_btn.grid(row=7, column=3, padx=5, pady=5, sticky=W)

        # Right label Frame
        Right_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Student Records", font=("Times New Roman", 15, "bold"))
        Right_frame.place(x=750, y=100, width=660, height=580)

        search_lbl = LabelFrame(Right_frame, bd=2, relief=RIDGE, text="Search Student", font=("Times New Roman", 14))
        search_lbl.place(x=0, y=10, width=660, height=100, )
        search_lbl.configure(bg="white")

        #Search Student By Name or Roll No
        search_by = Label(search_lbl, text="Search Student By:", font=("Cursive", 13), bg="white")
        search_by.grid(row=0, column=0, padx=10, sticky=W)

        search_student = ttk.Combobox(search_lbl, font=("Times New Roman", 13), width=17, state='readonly')
        search_student['value'] = ('Please select', 'Name', 'Roll No', 'Phone No')
        search_student.current(0)
        search_student.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = Entry(search_lbl, bd=2, font=('Times New Roman', 13))
        search_entry.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        # Table frame
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=4, y=120, width=650, height=300)
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

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
    obj = Student(root)
    root.geometry("1440x1080")  # Set an initial size for the window
    root.mainloop()
