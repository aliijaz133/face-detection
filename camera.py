import cv2
import sys
import tkinter as tk
from tkinter import Canvas, PhotoImage


class FaceDetectionApp:
    def __init__(self, master, cascPath):
        self.master = master
        self.master.title("Face Detection App")

        self.cascPath = cascPath
        self.faceCascade = cv2.CascadeClassifier(self.cascPath)

        self.video_capture = cv2.VideoCapture(0)

        self.canvas = Canvas(self.master, width=640, height=480)
        self.canvas.pack()

        self.video_loop()

    def video_loop(self):
        ret, frame = self.video_capture.read()
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

        self.photo = self.convert_to_tk_image(frame)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        self.master.after(10, self.video_loop)

    def convert_to_tk_image(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, channels = rgb_frame.shape
        image = PhotoImage(width=width, height=height)
        image.put(rgb_frame.flatten(), to=(0, 0, width, height, 3))
        return image


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
