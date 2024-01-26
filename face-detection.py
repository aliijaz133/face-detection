import cv2
import numpy as np
import face_recognition


img_bgr = face_recognition.load_image_file('./dataset/images/aliijaz.jpg')
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
img_org_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# --------- Detecting Face -------
face_locations = face_recognition.face_locations(img_org_rgb)
face = face_locations[0]

# ------ Drawing bounding boxes around Faces------------------------
detect_face = img_org_rgb.copy()
cv2.rectangle(detect_face, (face[3], face[0]), (face[1], face[2]), (0, 255, 65), 2)

cv2.imshow('Detect face', detect_face)
cv2.imshow('Original Image', img_org_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()  # Close all OpenCV windows after the key is pressed
