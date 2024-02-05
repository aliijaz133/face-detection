from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from PIL import Image as PILImage

from tkinter import messagebox
from tkinter import filedialog
import pymongo
from bson import ObjectId
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
import qrcode
import io
import datetime
import os
import tempfile


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System - Student Details")

        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = self.client["student_management"]
        self.collection = self.database["students"]

        # Declare Variables
        self.var_dep = StringVar()
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_batch = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()
        self.var_status = StringVar()
        self.var_image = StringVar()
        self.var_photo = StringVar()
        self.var_id = StringVar()
        self.var_id.set("Auto Generated ID")
        self.var_gender = StringVar()
        self.var_radio1 = StringVar()

        # Create a Canvas widget as the background
        self.canvas = Canvas(self.root)
        self.canvas.pack(fill=BOTH, expand=YES)

        # Create a Vertical Scrollbar
        scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Load and set the background image
        self.bg_img_path = "./asset/images/background_image.png"
        self.update_bg_image()

        # Create a title label with a specified font
        self.title_text = "Student Management System"
        self.title_lbl = Label(
            text=self.title_text,
            font=("Times New Roman", 25, "bold"),
            bg="black",
            fg="white",
        )
        self.title_lbl.place(x=0, y=0, relwidth=1.0)

        # Configure column weights to allow for responsive resizing
        self.canvas.columnconfigure(0, weight=1)
        self.canvas.columnconfigure(1, weight=1)

        # Bind the window resize event to update the background image and title label
        self.root.bind("<Configure>", self.on_resize)

        # Student Detail Button
        img4 = PILImage.open(
            r"./asset/images/back-btn.png"
        )
        img4 = img4.resize((100, 40), PILImage.BICUBIC)
        self.photoImg4 = ImageTk.PhotoImage(img4)

        b1 = Button(image=self.photoImg4, command=self.dashboard, cursor="hand2")
        b1.place(x=50, y=50, width=100, height=40)

        # Left label Frame
        Left_frame = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="Student Details",
            font=("Times New Roman", 15, "bold"),
        )
        Left_frame.place(x=50, y=100, width=660, height=580)

        Left_sec_frame = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="Current Course Information",
            font=("Times New Roman", 15),
        )
        Left_sec_frame.place(x=70, y=140, width=620, height=120)

        # Add Department
        department_label = Label(
            Left_sec_frame, text="Department", font=("Cursive", 13)
        )
        department_label.grid(row=0, column=0, padx=10, sticky=W)
        dep_combo = ttk.Combobox(
            Left_sec_frame,
            textvariable=self.var_dep,
            font=("Times New Roman", 13),
            width=17,
            state="readonly",
        )
        dep_combo["value"] = (
            "Please select",
            "Computer Science",
            "Management Science",
            "Software Engineering",
            "Media Science",
            "Geo Physics",
        )
        dep_combo.configure(background="white", foreground="black")
        dep_combo.current(0)
        dep_combo.place(y=30, x=10, height=35)
        dep_combo.grid(row=0, column=1, padx=2, sticky=W)

        # Add Years
        department_year = Label(Left_sec_frame, text="Year", font=("Cursive", 13))
        department_year.grid(row=0, column=2, padx=10, sticky=W)
        dep_year = ttk.Combobox(
            Left_sec_frame,
            textvariable=self.var_year,
            font=("Times New Roman", 13),
            width=17,
            state="readonly",
        )
        dep_year["value"] = ("Please select", 2019, 2020, 2021, 2022, 2023, 2024)
        dep_year.configure(background="white", foreground="black")
        dep_year.current(0)
        dep_year.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Add Semester
        department_sems = Label(Left_sec_frame, text="Semester", font=("Cursive", 13))
        department_sems.grid(row=2, column=0, padx=10, sticky=W)
        dep_sems = ttk.Combobox(
            Left_sec_frame,
            textvariable=self.var_batch,
            font=("Times New Roman", 13),
            width=17,
            state="readonly",
        )
        dep_sems["value"] = (
            "Please select",
            "1st",
            "2nd",
            "3rd",
            "4th",
            "5th",
            "6th",
            "7th",
            "8th",
        )
        dep_sems.configure(background="white", foreground="black")
        dep_sems.current(0)
        dep_sems.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        # Add Course
        department_course = Label(Left_sec_frame, text="Courses", font=("Cursive", 13))
        department_course.grid(row=2, column=2, padx=10, sticky=W)
        dep_course = ttk.Combobox(
            Left_sec_frame,
            textvariable=self.var_course,
            font=("Times New Roman", 13),
            width=17,
            state="readonly",
        )
        dep_course["value"] = (
            "Please select",
            "PF",
            "SE",
            "OOP",
            "DSA",
            "Web-Tech",
            "Python",
            "Data Science",
        )
        dep_course.configure(background="white", foreground="black")
        dep_course.current(0)
        dep_course.grid(row=2, column=3, padx=2, pady=10, sticky=W)

        # Class Student Information
        Left_3rd_frame = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="Class Student Information",
            font=("Times New Roman", 15),
        )
        Left_3rd_frame.place(x=70, y=270, width=620, height=320)

        # Student ID:
        student_id_lbl = Label(Left_3rd_frame, text="Student Id:", font=("Cursive", 13))
        student_id_lbl.grid(row=0, column=0, padx=5, sticky="W")

        student_id_entry = Entry(
            Left_3rd_frame, textvariable=self.var_id, font=("Times New Roman",), bd=2, state="readonly", cursor="hand2"
        )
        student_id_entry.grid(row=0, column=1)

        # Set placeholder text and its color
        place_holder = "Auto Generated"
        student_id_entry.insert(0, place_holder)
        student_id_entry.config(fg="gray", bg="white")

        # Student Name:
        student_name_lbl = Label(
            Left_3rd_frame, text="Student name:", font=("Cursive", 13)
        )
        student_name_lbl.grid(row=0, column=2, padx=5, sticky=W)
        student_name_entry = Entry(
            Left_3rd_frame, textvariable=self.var_name, font=("Times New Roman",), bd=2
        )
        student_name_entry.grid(row=0, column=3)

        # Student Roll No:
        student_roll_lbl = Label(
            Left_3rd_frame, text="Student Roll No:", font=("Cursive", 13)
        )
        student_roll_lbl.grid(row=2, column=0, padx=5, pady=15, sticky=W)
        student_roll_entry = Entry(
            Left_3rd_frame, textvariable=self.var_roll, font=("Times New Roman",), bd=2
        )
        student_roll_entry.grid(row=2, column=1, padx=5, pady=15, sticky=W)

        # Student Gender:
        student_gender_lbl = Label(Left_3rd_frame, text="Gender:", font=("Cursive", 13))
        student_gender_lbl.grid(row=2, column=2, padx=5, pady=15, sticky=W)
        student_gender_entry = Entry(
            Left_3rd_frame,
            textvariable=self.var_gender,
            font=("Times New Roman",),
            bd=2,
        )
        student_gender_entry.grid(row=2, column=3, padx=5, pady=15, sticky=W)

        # Student DOB:
        student_dob_lbl = Label(
            Left_3rd_frame, text="Student DOB:", font=("Cursive", 13)
        )
        student_dob_lbl.grid(row=3, column=0, padx=5, sticky=W)
        student_dob_entry = Entry(
            Left_3rd_frame, textvariable=self.var_date, font=("Times New Roman",), bd=2
        )
        student_dob_entry.grid(row=3, column=1, padx=5, sticky=W)

        # Student Phone Number:
        student_ph_lbl = Label(
            Left_3rd_frame, text="Mobile Number:", font=("Cursive", 13)
        )
        student_ph_lbl.grid(row=3, column=2, padx=5, pady=3, sticky=W)
        student_ph_entry = Entry(
            Left_3rd_frame, textvariable=self.var_phone, font=("Times New Roman",), bd=2
        )
        student_ph_entry.grid(row=3, column=3, padx=5, pady=3, sticky=W)

        # Student Email Address:
        student_email_lbl = Label(
            Left_3rd_frame, text="Student Email:", font=("Cursive", 13)
        )
        student_email_lbl.grid(row=5, column=0, padx=5, sticky=W)
        student_email_entry = Entry(
            Left_3rd_frame, textvariable=self.var_email, font=("Times New Roman",), bd=2
        )
        student_email_entry.grid(row=5, column=1, padx=5, sticky=W)

        # Student Address:
        student_address_lbl = Label(
            Left_3rd_frame, text="Address:", font=("Cursive", 13)
        )
        student_address_lbl.grid(row=5, column=2, padx=5, pady=15, sticky=W)
        student_address_entry = Entry(
            Left_3rd_frame,
            textvariable=self.var_address,
            font=("Times New Roman",),
            bd=2,
        )
        student_address_entry.grid(row=5, column=3, padx=5, pady=15, sticky=W)

        # Add radio Button for Taking Picture
        radio_btn_1 = ttk.Radiobutton(
            Left_3rd_frame,
            textvariable=self.var_radio1,
            text="Take Sample Photo",
            value=1,
        )
        radio_btn_1.grid(row=6, column=0, padx=5, pady=5, sticky=W)

        radio_btn_2 = ttk.Radiobutton(
            Left_3rd_frame,
            textvariable=self.var_radio1,
            text="Take Not Sample Photo",
            value=2,
        )
        radio_btn_2.grid(row=6, column=1, padx=5, pady=5, sticky=W)

        # Delete Button
        delete_btn = Button(
            Left_3rd_frame,
            text="Delete",
            command=self.delete_data,
            font=("Times New Roman", 13),
            cursor="hand2",
            bg="Red",
        )
        delete_btn.grid(row=7, column=0, padx=5, pady=5, sticky=W)

        # Update Button
        update_btn = Button(
            Left_3rd_frame,
            text="Update",
            command=self.update_data,
            font=("Times New Roman", 13),
            cursor="hand2",
            bg="Gray",
        )
        update_btn.grid(row=7, column=1, padx=5, pady=5, sticky=W)

        # Reset Button
        reset_btn = Button(
            Left_3rd_frame,
            text="Reset",
            command=self.reset_data,
            font=("Times New Roman", 13),
            cursor="hand2",
            bg="LightBlue",
        )
        reset_btn.grid(row=7, column=2, padx=5, pady=5, sticky=W)

        # Submit Button
        save_btn = Button(
            Left_3rd_frame,
            text="Save",
            command=self.add_data,
            font=("Times New Roman", 13),
            cursor="hand2",
            bg="LightGreen",
        )
        save_btn.grid(row=7, column=3, padx=5, pady=5, sticky=W)

        # Add Photo Button
        add_photo_btn = Button(
            Left_3rd_frame,
            text="Add Photo",
            command=self.add_photo_during_update,
            font=("Times New Roman", 13),
            cursor="hand2",
            bg="Blue",
            fg="white",
        )
        add_photo_btn.grid(row=8, column=0, padx=5, pady=5, sticky=W)

        #Generate Pdf File
        pdf_gen_btn = Button(
            Left_3rd_frame,
            text="Generate PDF",
            command=self.generate_pdf,
            font=("Times New Roman", 13),
            cursor="hand2",
            bg="Orange",
            fg="white",
        )
        pdf_gen_btn.grid(row=8, column=1, padx=5, pady=5, sticky=W)

        # Right label Frame
        Right_frame = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="Student Records",
            font=("Times New Roman", 15, "bold"),
        )
        Right_frame.place(x=750, y=100, width=660, height=580)

        search_lbl = LabelFrame(
            Right_frame,
            bd=2,
            relief=RIDGE,
            text="Search Student",
            font=("Times New Roman", 14),
        )
        search_lbl.place(
            x=0,
            y=10,
            width=660,
            height=100,
        )
        search_lbl.configure(bg="white")

        # Search Student By Name or Roll No
        search_by = Label(
            search_lbl, text="Search Student By:", font=("Cursive", 13), bg="white"
        )
        search_by.grid(row=0, column=0, padx=10, sticky=W)

        search_student = ttk.Combobox(
            search_lbl, font=("Times New Roman", 13), width=17, state="readonly"
        )
        search_student["value"] = ("Please select", "Name", "Roll No", "Phone No")
        search_student.current(0)
        search_student.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = Entry(search_lbl, bd=2, font=("Times New Roman", 13))
        search_entry.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        # Table frame
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=4, y=120, width=650, height=300)
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            columns=(
                "ID",
                "Name",
                "Roll No",
                "Gender",
                "DOB",
                "Phone No",
                "Email",
                "Address",
            ),
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set,
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ID", text="ID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Roll No", text="Roll No")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Phone No", text="Phone No")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Address", text="Address")
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.bind("<ButtonRelease-1>", self.get_selected_data)

        self.show_data()

    # ------------------------------------------------------------------------------------------------------------------------
    def dashboard(self):
        from dashboard import Face_Recognition_System

        dashboard_window = Toplevel(self.root)
        dashboard_frame = Face_Recognition_System(dashboard_window)
        dashboard_window.geometry("1440x1080")
        dashboard_window.mainloop()

    # =========================================================================
    # ========================== FETCH DATA FROM SERVER =======================
    # =========================================================================
    def show_data(self):
        for item in self.student_table.get_children():
            self.student_table.delete(item)

        cursor = self.collection.find()

        for record in cursor:
            self.student_table.insert(
                "",
                "end",
                values=(
                    record["_id"],
                    record["name"],
                    record["roll"],
                    record["gender"],
                    record["dob"],
                    record["phone"],
                    record["email"],
                    record["address"],
                    record.get("department", ""),
                ),
            )

    # =========================================================================
    # ========================== SAVE DATA IN SERVER ==========================
    # =========================================================================

    def add_data(self):
        if (
            self.var_name.get() == ""
            or self.var_roll.get() == ""
            or self.var_gender.get() == ""
            or self.var_date.get() == "" or self.var_phone.get() == ""
            or self.var_email.get() == ""
            or self.var_address.get() == ""
            or self.var_year.get() == ""
            or self.var_batch.get() == ""
            or self.var_course.get() == ""
            or self.var_id.get() == ""
        ):
            messagebox.showerror(
                "Error", "Please fill all the fields", parent=self.root
            )
        else:
            student_data = {
                "name": self.var_name.get(),
                "roll": self.var_roll.get(),
                "gender": self.var_gender.get(),
                "dob": self.var_date.get(),
                "phone": self.var_phone.get(),
                "email": self.var_email.get(),
                "address": self.var_address.get(),
                "department": self.var_dep.get(),
                "year": self.var_year.get(),
                "batch": self.var_batch.get(),
                "course": self.var_course.get(),
                "id": self.var_id.get(),
            }

            result = self.collection.insert_one(student_data)

            messagebox.showinfo(
                "Success",
                "Successfully added to MongoDB with ID: {}".format(result.inserted_id),
            )
            self.var_name.set("")
            self.var_roll.set("")
            self.var_gender.set("")
            self.var_date.set("")
            self.var_phone.set("")
            self.var_email.set("")
            self.var_address.set("")
            self.var_dep.set("Please select")
            self.var_year.set("Please select")
            self.var_batch.set("Please select")
            self.var_course.set("Please select")
            self.var_id.set("Auto Generated ID")
            self.var_radio1.set(None)

            # Update the table immediately after saving new data
            self.show_data()

    def get_selected_data(self, event):
        selected_item = self.student_table.selection()
        if selected_item:
            data = self.student_table.item(selected_item)["values"]
            # Populate the form fields with the selected data
            self.var_id.set(data[0])
            self.var_name.set(data[1])
            self.var_roll.set(data[2])
            self.var_gender.set(data[3])
            self.var_date.set(data[4])
            self.var_phone.set(data[5])
            self.var_email.set(data[6])
            self.var_address.set(data[7])

    # =========================================================================
    # =========================== RESET USER FORM =============================
    # =========================================================================

    def reset_data(self):
        self.var_name.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_date.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_dep.set("Please select")
        self.var_year.set("Please select")
        self.var_batch.set("Please select")
        self.var_course.set("Please select")
        self.var_id.set("Auto Generated ID")
        self.var_radio1.set(None)

    # =========================================================================
    # ========================== UPDATE DATA IN SERVER ========================
    # =========================================================================

    def update_data(self):
        selected_item = self.student_table.selection()
        if not selected_item:
            messagebox.showerror(
                "Error", "Please select a record to update", parent=self.root
            )
            return

        data_id = ObjectId(self.var_id.get())
        data = self.student_table.item(selected_item)["values"]

        if any(value == "" for value in data):
            messagebox.showerror(
                "Error", "Please fill all the fields", parent=self.root
            )
            return

        updated_data = {
            "name": self.var_name.get(),
            "roll": self.var_roll.get(),
            "gender": self.var_gender.get(),
            "dob": self.var_date.get(),
            "phone": self.var_phone.get(),
            "email": self.var_email.get(),
            "address": self.var_address.get(),
            "department": self.var_dep.get(),
            "year": self.var_year.get(),
            "batch": self.var_batch.get(),
            "course": self.var_course.get(),
            "id": self.var_id.get(),
        }

        update_result = self.collection.update_one(
            {"_id": data_id}, {"$set": updated_data}
        )

        if update_result.modified_count > 0:
            messagebox.showinfo(
                "Success", "Record updated successfully", parent=self.root
            )
            self.show_data()
        else:
            messagebox.showerror("Error", "Failed to update record", parent=self.root)

    # =========================================================================
    # ========================== DELETE DATA FROM SERVER ======================
    # =========================================================================
    def delete_data(self):
        selected_item = self.student_table.selection()
        if not selected_item:
            messagebox.showerror(
                "Error", "Please select a record to delete", parent=self.root
            )
            return

        # Convert the ID to ObjectId
        data_id = ObjectId(self.var_id.get())

        # Ask for confirmation before deleting
        confirmation = messagebox.askyesno(
            "Confirmation",
            f"Do you want to delete the record of {self.var_name.get()}?",
            parent=self.root,
        )

        if confirmation:
            # Delete the record from the database
            delete_result = self.collection.delete_one({"_id": data_id})

            if delete_result.deleted_count > 0:
                messagebox.showinfo(
                    "Success", "Record deleted successfully", parent=self.root
                )
                self.show_data()  # Refresh the table
            else:
                messagebox.showerror(
                    "Error", "Failed to delete record", parent=self.root
                )

    # =========================================================================
    # ============================= ADD PHOTO =================================
    # =========================================================================
    def add_photo_during_update(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*")])

        if file_path:
            # Update the record in the database with the file path
            update_result = self.collection.update_one(
                {"_id": ObjectId(self.var_id.get())}, {"$set": {"photo": file_path}}
            )

            if update_result.modified_count > 0:
                messagebox.showinfo(
                    "Success",
                    "Photo added successfully during update",
                    parent=self.root,
                )
                self.show_data()  # Refresh the table
            else:
                messagebox.showerror(
                    "Error", "Failed to add photo during update", parent=self.root
                )

    # =========================================================================
    # =========================== SEARCH STUDENT ==============================
    # =========================================================================
    # def search_data(self):
    #     search_criteria = search_student.get()
    #     search_value = search_entry.get()

    #     if search_criteria == "Please select" or not search_value:
    #         messagebox.showerror("Error", "Please select search criteria and enter search value", parent=self.root)
    #         return

    #     # Clear existing data in the table
    #     for item in self.student_table.get_children():
    #         self.student_table.delete(item)

    #     # Perform search based on selected criteria and value
    #     if search_criteria == "Name":
    #         cursor = self.collection.find({"name": {"$regex": f".*{search_value}.*", "$options": "i"}})
    #     elif search_criteria == "Roll No":
    #         cursor = self.collection.find({"roll": {"$regex": f".*{search_value}.*", "$options": "i"}})
    #     elif search_criteria == "Phone No":
    #         cursor = self.collection.find({"phone": {"$regex": f".*{search_value}.*", "$options": "i"}})

    #     # Populate the table with search results
    #     for record in cursor:
    #         self.student_table.insert(
    #             "",
    #             "end",
    #             values=(
    #                 record["_id"],
    #                 record["name"],
    #                 record["roll"],
    #                 record["gender"],
    #                 record["dob"],
    #                 record["phone"],
    #                 record["email"],
    #                 record["address"],
    #                 record.get("department", ""),
    #             )
    #         )

    # --------------------------------------------------------------------------------------------------------------------------------

    #==================================================================
    #================ GENERATE PDF AND QRCODE =========================
    #==================================================================

    def generate_qr_code(self, data):
        data_str = str(data)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data_str)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")

        # Save QR code image to a temporary file
        temp_dir = tempfile.mkdtemp()
        temp_qr_path = os.path.join(temp_dir, "temp_qr.png")
        qr_img.save(temp_qr_path)

        # Return the path to the saved QR code image
        return temp_qr_path

    def generate_pdf(self):
        selected_item = self.student_table.selection()
        if not selected_item:
            messagebox.showerror(
                "Error", "Please select a record to generate PDF", parent=self.root
            )
            return

        # Get selected data
        data = self.student_table.item(selected_item)["values"]

        # Create a PDF file
        pdf_file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Save PDF",
        )

        if pdf_file_path:
            # Create PDF document
            pdf = SimpleDocTemplate(pdf_file_path, pagesize=letter)
            styles = getSampleStyleSheet()

            # Header
            header_style = ParagraphStyle(
                'Header1',
                parent=styles['Heading1'],
                fontName='Helvetica-Bold',
                spaceAfter=6,
                fontSize=14,
                textColor=colors.navy,
            )
            header = Paragraph("Student Details", header_style)

            # Content
            content_style = ParagraphStyle(
                'BodyText',
                parent=styles['BodyText'],
                fontName='Helvetica',
                fontSize=12,
                spaceAfter=12,
            )

            content = [
                Paragraph(f"<b>Name:</b> {data[1]}", content_style),
                Paragraph(f"<b>Roll No:</b> {data[2]}", content_style),
                Paragraph(f"<b>Date of Birth:</b> {data[4]}", content_style),
                Paragraph(f"<b>Mobile:</b> {data[5]}", content_style),
                Paragraph(f"<b>Email:</b> {data[6]}", content_style),
                Paragraph(f"<b>Gender:</b> {data[3]}", content_style),
                Paragraph(f"<b>Address:</b> {data[7]}", content_style),
                Paragraph(f"<b>ID:</b> {data[0]}", content_style),
                Paragraph(f"<b>QR Code:</b>", content_style),
            ]

            # Add QR Code for ID
            qr_code_path = self.generate_qr_code(data[0])
            qr_code_img = Image(qr_code_path, width=100, height=100)
            content.append(qr_code_img)

            # Add date, time, and generated by information
            now = datetime.datetime.now()
            date_time_info = [
                f"<b>Date:</b> {now.strftime('%d-%b-%Y')}",
                f"<b>Time:</b> {now.strftime('%I:%M %p')}",
                f"<b>Generated By:</b> Ali Ijaz",  # Assuming data[1] contains the name
            ]
            content += [Paragraph(info, content_style) for info in date_time_info]

            # Build PDF
            pdf.build([header] + content)

            messagebox.showinfo(
                "Success", f"PDF generated successfully at {pdf_file_path}", parent=self.root
            )

    #-----------------------------------------------------------------------------------------------------------------------------

    def update_bg_image(self, event=None):
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()

        bg_img = PILImage.open(self.bg_img_path)
        bg_img = bg_img.resize((window_width, window_height), PILImage.BICUBIC)
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
    app = Student(root)
    root.geometry("1440x800")  # Set an initial size for the window
    root.bind("<Configure>", app.on_resize)
    root.mainloop()
