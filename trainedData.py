import cv2
import os
from tkinter import messagebox


class Image_Data_Trained:
    def detect_faces(image_path, output_folder):

        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        # Loop through all files in the specified folder
        for filename in os.listdir(image_path):
            if filename.lower().endswith((".png", ".jpg", ".jpeg")):

                image = cv2.imread(os.path.join(image_path, filename))

                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                faces = face_cascade.detectMultiScale(
                    gray, scaleFactor=1.3, minNeighbors=5
                )

                for x, y, w, h in faces:
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

                output_path = os.path.join(output_folder, "detected_" + filename)
                cv2.imwrite(output_path, image)

    if __name__ == "__main__":

        input_folder = (
            "./asset/student-image"
        )

        output_folder = (
            "./asset/trained-data"
        )

        detect_faces(input_folder, output_folder)
        messagebox.showinfo("Detected", "Face detection completed")
        # print("Face detection completed.")
