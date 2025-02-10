import cv2 as cv
import numpy as np

def resizeImage(img, scale=0.09):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Photos/cat2.jpg')
# cv.imshow('Cat', resizeImage(img))

b,g,r = cv.split(img)

# white is high concentration of that color
cv.imshow('Blue', resizeImage(b))
cv.imshow('Green', resizeImage(g))
cv.imshow('Red', resizeImage(r))

# merge the channels
merged = cv.merge([b,g,r])
cv.imshow('Merged', resizeImage(merged))

# visiuallize the channels
blank = np.zeros(img.shape[:2], dtype='uint8')

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', resizeImage(blue))
cv.imshow('Green', resizeImage(green))
cv.imshow('Red', resizeImage(red))

cv.waitKey(0)