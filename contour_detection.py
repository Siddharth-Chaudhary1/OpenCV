import cv2 as cv
import numpy as np

def resizeImage(img, scale=0.09):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Photos/cat1.jpg')
cv.imshow('Cat', resizeImage(img))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grey', resizeImage(gray))

canny = cv.Canny(img, 125, 125)
# cv.imshow('Canny', resizeImage(canny))

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(f'{len(contours)} contour(s) found!')

# other ways to find contour using threshold
ret, thresh = cv.threshold(gray, 125, 125, cv.THRESH_BINARY)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')
# cv.imshow('contour', resizeImage(thresh))

blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow('Blank', resizeImage(blank))

# this draws contours over image -1 for all contours
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', resizeImage(blank))

cv.waitKey(0)