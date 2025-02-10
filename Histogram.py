import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def resizeImage(img, scale=0.09):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dim = (width, height)
    return cv.resize(img, dim, interpolation = cv.INTER_AREA)

img = cv.imread('Photos/dog2.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('Dog', resizeImage(img))

gray_hist = cv.calcHist([img], [0], None, [256], [0, 256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

cv.waitKey(0)
