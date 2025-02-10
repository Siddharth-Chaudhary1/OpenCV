import cv2 as cv
import numpy as np

def resizeImage(img, scale):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dim = (width, height)
    return cv.resize(img, dim, interpolation = cv.INTER_AREA)

img = cv.imread('Photos/dog2.jpg')
# cv.imshow('Cat', resizeImage(img, 0.1))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', resizeImage(lap, 0.1))

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Sobel X', resizeImage(sobelx, 0.1))
cv.imshow('Sobel Y', resizeImage(sobely, 0.1))
cv.imshow('Combined Sobel', resizeImage(combined_sobel, 0.1))

# Canny
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', resizeImage(canny, 0.1))

cv.waitKey(0)
# python Edge_detection.py
