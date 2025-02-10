import cv2 as cv
import numpy as np

def resizeImage(img, scale=0.09):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dim = (width, height)
    return cv.resize(img, dim, interpolation = cv.INTER_AREA)

img = cv.imread('Photos/dog1.jpg')
cv.imshow('Dog', resizeImage(img))

blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', resizeImage(mask))

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', resizeImage(masked))

cv.waitKey(0)