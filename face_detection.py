import cv2 as cv
import numpy as np

# face detection with haar cascades
# it detects presence of face 

img = cv.imread('Photos/lady.webp')
# cv.imshow('Lady ', img)

# no need of color so convert img to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# reading haar_cascade.xml file
haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=9)

print(f"Number of face found = {len(faces_rect)}")

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)