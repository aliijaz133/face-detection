from flask import Flask, render_template, request
import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

def detect_faces(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    image = cv2.imread(image_path)

    with open('./dataset/label/labels.txt', 'r') as file:
        usernames = [line.strip() for line in file]

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=5)

    image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image_pil)

    font = ImageFont.load_default()

    for idx, (x, y, w, h) in enumerate(faces):
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 2)

        # Get the username for the current face
        if idx < len(usernames):
            username = usernames[idx]
        else:
            username = "Unknown"

        # Add label text directly from 'labels.txt'
        label = f' {idx + 1}: {username}'
        draw.text((x, y - 10), label, (255, 255, 255), font=font)

    annotated_image_path = f'./static/annotated_{os.path.basename(image_path)}'
    cv2.imwrite(annotated_image_path, cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR))

    return annotated_image_path

@app.route('/')
def index():
    return render_template('index.html')

# Flask application
@app.route('/show_image', methods=['POST'])
def show_image():
    enter_name = request.form['image_name']
    images_folder = './database/images/'

    # Check if the entered image file exists
    image_path = os.path.join(images_folder, enter_name)
    if not os.path.isfile(image_path):
        return "Image not found!"

    annotated_image_path = detect_faces(image_path)

    # Specify the correct template file
    return render_template('show_image.html', image_path=annotated_image_path)

if __name__ == '__main__':
    app.run(debug=True)
