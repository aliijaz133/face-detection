import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

enterName = input("Enter the name of the image: ")

image_path = f'./dataset/images/{enterName}'

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

image_cv2 = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)

cv2.imshow('Face Detection', image_cv2)
cv2.waitKey(0)
cv2.destroyAllWindows()
