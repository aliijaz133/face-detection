import cv2
import sys
import tkinter as tk
from tkinter import Canvas, PhotoImage, Button, messagebox
from datetime import datetime
import os

class FaceDetectionApp:
    def __init__(self, master, cascPath):
        self.master = master
        self.master.title("Face Detection App")

        self.cascPath = cascPath
        self.faceCascade = cv2.CascadeClassifier(self.cascPath)

        # Check if camera is available
        self.video_capture = cv2.VideoCapture(0)
        if not self.video_capture.isOpened():
            messagebox.showerror("Error", "Camera is not detected. Please check your camera.")
            sys.exit(1)

        self.canvas = Canvas(self.master, width=640, height=480)
        self.canvas.pack()

        self.save_button = Button(self.master, text="Save Image", command=self.save_image)
        self.save_button.pack()

        self.video_loop()

    def video_loop(self):
        ret, frame = self.video_capture.read()
        if not ret:
            messagebox.showerror("Error", "Failed to capture video. Please check your camera.")
            sys.exit(1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE,
        )

        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.photo = self.convert_to_tk_image(rgb_frame)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        self.master.after(10, self.video_loop)

    def convert_to_tk_image(self, rgb_frame):
        height, width, channels = rgb_frame.shape
        image = PhotoImage(width=width, height=height)
        image.put(rgb_frame.flatten(), to=(0, 0, width, height, 3))
        return rgb_frame

    def save_image(self):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"face_{timestamp}.png"
        folder_path = "./asset/student-image"

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        cv2.imwrite(os.path.join(folder_path, filename), cv2.cvtColor(self.photo, cv2.COLOR_RGB2BGR))
        print(f"Image saved as {filename} in {folder_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tkinter_app.py <path_to_haarcascades_xml>")
        sys.exit(1)

    cascPath = sys.argv[1]

    root = tk.Tk()
    app = FaceDetectionApp(root, cascPath)
    root.mainloop()

# Release the video capture when the Tkinter window is closed
app.video_capture.release()
