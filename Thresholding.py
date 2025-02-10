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
# cv.imshow('Gray', resizeImage(gray, 0.1))

# Simple Thresholding

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', resizeImage(thresh, 0.1))

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse', resizeImage(thresh_inv, 0.1))

# Adaptive Thresholding

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Threshold', resizeImage(adaptive_thresh, 0.1))

# Adaptive Thresholding Gaussian
adaptive_thresh1 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Threshold Gaussian', resizeImage(adaptive_thresh1, 0.1))

cv.waitKey(0)