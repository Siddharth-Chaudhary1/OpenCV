import cv2 as cv
import numpy as np
# import matplotlib.pyplot as plt

def resizeImage(img, scale=0.09):
    width = int(img.shape[1] * scale)   
    height = int(img.shape[0] * scale)
    dim = (width, height)
    
    return cv.resize(img, dim, interpolation = cv.INTER_AREA)

img = cv.imread('Photos/cat1.jpg')
cv.imshow('Cat', resizeImage(img))

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', resizeImage(gray))

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', resizeImage(hsv))

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', resizeImage(lab))

# BGR to RGB
# BGR is inverse of RGB
# so to convert BGR to RGB, we need to use cv.COLOR_BGR2RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', resizeImage(rgb))

# plt.imshow(rgb)
# plt.show()

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR', resizeImage(hsv_bgr))

cv.waitKey(0)

# python color_space.py